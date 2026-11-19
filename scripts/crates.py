"""Waylaid Crate -> Merchant's Favor calculator on our own TSM prices.

Each crate is filled with ONE bundle and handed in for Favor plus 50c per Favor
(5 Favor -> 2s50, 30 Favor -> 15s; Azeroth Plus and wow-professions agree).
Artisan Favor is unpublished; --artisan N assumes white=N, crafted=2N (pattern
of the lower tiers would be 20/40).

Prices: "cheap" uses the cheapest listing, "real" uses max(cheapest, TSM recent
market value), a better guess once you buy more than the first listing.
Crate listings (numAuctions) are about one crate each, so they cap how many of
a crate type you can buy at that price.

    crates.py                       ranking, best bundle per crate
    crates.py --target 6000         cheapest buy plan to reach 6000 Favor
    crates.py --budget 50           same, but spend up to 50g
    crates.py --all                 every bundle, not just the best one
    crates.py --craft               also price crafted bundles from raw mats
    crates.py --target 6000 --stack 10   assume 10 units per material listing (default 5)

The plan is greedy across every bundle. TSM gives the number of listings, not the
quantity, so a bundle's material is capped at listings x --stack units. Buying that
deep will cost more than market value; treat totals as a floor.
"""

from __future__ import annotations

import argparse
import sqlite3

from report import DB, SCOPE, money

REFUND_PER_FAVOR = 50  # copper

# crate: (tier, favor, [(qty, item), ...]). Bundles from the in-game crate tooltips
# as listed by Azeroth Plus; unverified ones (Gold Power Core, Wool Cloth) left out.
CRATES = {
    "Apprentice Ingots": ("Apprentice", 10, [(20, "Copper Bar"), (20, "Tin Bar"), (10, "Bronze Bar")]),
    "Apprentice Fabrics": ("Apprentice", 10, [(2, "Cured Light Hide"), (20, "Bolt of Linen Cloth")]),
    "Apprentice Parts": ("Apprentice", 10, [(16, "Handful of Copper Bolts"), (16, "Copper Tube"),
                                            (4, "Copper Modulator")]),
    "Apprentice Textiles": ("Apprentice", 5, [(40, "Linen Cloth"), (20, "Light Leather")]),
    "Apprentice Curiosities": ("Apprentice", 5, [(20, "Strange Dust"), (4, "Greater Magic Essence"),
                                                 (6, "Small Glimmering Shard"), (2, "Large Glimmering Shard")]),
    "Apprentice Ore": ("Apprentice", 5, [(20, "Copper Ore"), (20, "Tin Ore")]),
    "Apprentice Herbs": ("Apprentice", 5, [(20, "Peacebloom"), (20, "Silverleaf"), (10, "Earthroot"),
                                           (10, "Mageroyal"), (10, "Briarthorn")]),
    "Journeyman Ingots": ("Journeyman", 20, [(10, "Silver Bar"), (20, "Iron Bar")]),
    "Journeyman Fabrics": ("Journeyman", 20, [(6, "Bolt of Woolen Cloth"), (10, "Bolt of Silk Cloth"),
                                              (2, "Cured Medium Hide")]),
    "Journeyman Parts": ("Journeyman", 20, [(8, "Bronze Tube"), (7, "Whirring Bronze Gizmo"),
                                            (4, "Bronze Framework")]),
    "Journeyman Textiles": ("Journeyman", 10, [(40, "Silk Cloth"), (20, "Medium Leather")]),
    "Journeyman Ore": ("Journeyman", 10, [(10, "Silver Ore"), (20, "Iron Ore")]),
    "Journeyman Herbs": ("Journeyman", 10, [(10, "Stranglekelp"), (10, "Bruiseweed"), (10, "Wild Steelbloom"),
                                            (10, "Grave Moss"), (10, "Kingsblood")]),
    "Journeyman Curiosities": ("Journeyman", 10, [(20, "Soul Dust"), (4, "Greater Astral Essence"),
                                                  (6, "Small Glowing Shard"), (2, "Large Glowing Shard")]),
    "Expert Ingots": ("Expert", 30, [(20, "Mithril Bar"), (15, "Steel Bar"), (10, "Gold Bar")]),
    "Expert Fabrics": ("Expert", 30, [(2, "Cured Heavy Hide")]),
    "Expert Parts": ("Expert", 30, [(8, "Iron Strut"), (5, "Mithril Tube"), (12, "Unstable Trigger"),
                                    (5, "Mithril Casing")]),
    "Expert Textiles": ("Expert", 15, [(40, "Mageweave Cloth"), (20, "Heavy Leather")]),
    "Expert Ore": ("Expert", 15, [(10, "Gold Ore"), (20, "Mithril Ore")]),
    "Earthly Expert Herbs": ("Expert", 15, [(20, "Liferoot"), (10, "Fadeleaf"), (10, "Goldthorn"),
                                            (10, "Khadgar's Whisker")]),
    "Flowering Expert Herbs": ("Expert", 15, [(10, "Wintersbite"), (10, "Firebloom"), (20, "Purple Lotus"),
                                              (10, "Arthas' Tears")]),
    "Expert Curiosities": ("Expert", 15, [(20, "Vision Dust"), (4, "Greater Mystic Essence"),
                                          (6, "Small Radiant Shard"), (2, "Large Radiant Shard")]),
    "Artisan Ingots": ("Artisan", None, [(2, "Dark Iron Bar"), (10, "Truesilver Bar"), (20, "Thorium Bar")]),
    "Artisan Fabrics": ("Artisan", None, [(8, "Bolt of Runecloth"), (2, "Cured Thick Hide")]),
    "Artisan Parts": ("Artisan", None, [(5, "Thorium Widget"), (5, "Truesilver Transformer"), (2, "Thorium Tube")]),
    "Artisan Textiles": ("Artisan", None, [(40, "Runecloth"), (20, "Thick Leather"), (20, "Rugged Leather")]),
    "Artisan Ore": ("Artisan", None, [(10, "Truesilver Ore"), (20, "Thorium Ore"), (20, "Dark Iron Ore")]),
    "Earthly Artisan Herbs": ("Artisan", None, [(10, "Golden Sansam"), (20, "Sungrass"), (10, "Blindweed"),
                                                (10, "Ghost Mushroom"), (10, "Gromsblood")]),
    "Flowering Artisan Herbs": ("Artisan", None, [(20, "Dreamfoil"), (20, "Mountain Silversage"),
                                                  (20, "Plaguebloom"), (20, "Icecap")]),
    "Artisan Curiosities": ("Artisan", None, [(20, "Dream Dust"), (4, "Greater Nether Essence"),
                                              (6, "Small Brilliant Shard"), (2, "Large Brilliant Shard")]),
}
CRAFTED = ("Ingots", "Fabrics", "Parts")

# Crafted bundle items made from raw mats: item -> (yield, [(qty, input)]).
# Only simple, well-known conversions; needs the right profession.
RECIPES = {
    "Copper Bar": (1, [(1, "Copper Ore")]), "Tin Bar": (1, [(1, "Tin Ore")]),
    "Bronze Bar": (2, [(1, "Copper Bar"), (1, "Tin Bar")]),
    "Silver Bar": (1, [(1, "Silver Ore")]), "Iron Bar": (1, [(1, "Iron Ore")]),
    "Gold Bar": (1, [(1, "Gold Ore")]), "Mithril Bar": (1, [(1, "Mithril Ore")]),
    "Truesilver Bar": (1, [(1, "Truesilver Ore")]), "Thorium Bar": (1, [(1, "Thorium Ore")]),
    "Bolt of Linen Cloth": (1, [(2, "Linen Cloth")]), "Bolt of Woolen Cloth": (1, [(3, "Wool Cloth")]),
    "Bolt of Silk Cloth": (1, [(4, "Silk Cloth")]), "Bolt of Runecloth": (1, [(5, "Runecloth")]),
}


class Prices:
    def __init__(self, db: sqlite3.Connection):
        self.ts = db.execute("SELECT max(ts) FROM auctiondb_non_commodity_data WHERE scope=?", (SCOPE,)).fetchone()[0]
        self.by_name: dict[str, tuple[int, int | None, int]] = {}
        for name, b, n, mv in db.execute(
                "SELECT i.name, d.minBuyout, d.numAuctions, d.marketValueRecent FROM auctiondb_non_commodity_data d "
                "JOIN items i ON i.id = d.item WHERE d.scope=? AND d.ts=? AND d.minBuyout > 0", (SCOPE, self.ts)):
            self.by_name.setdefault(name, (b, n, mv or b))
        self.last_count: dict[str, int] = dict(db.execute(
            "SELECT i.name, d.numAuctions FROM auctiondb_non_commodity_data d JOIN items i ON i.id = d.item "
            "WHERE d.scope=? AND d.ts=(SELECT max(ts) FROM auctiondb_non_commodity_data "
            "WHERE scope=? AND numAuctions IS NOT NULL)", (SCOPE, SCOPE)))

    def get(self, name: str, real: bool) -> int | None:
        p = self.by_name.get(name)
        if not p:
            return None
        return max(p[0], p[2]) if real else p[0]

    def listings(self, name: str) -> int:
        """Auction count; the public CSV has none, so fall back to the last count
        the push feed recorded (stale, before 18 Nov 2026), else 0."""
        p = self.by_name.get(name)
        if p and p[1] is not None:
            return p[1]
        return self.last_count.get(name, 0)

    def unit(self, name: str, real: bool, craft: bool) -> tuple[int | None, str]:
        """Cheapest way to get one unit: buy it, or (with craft) make it from raw mats."""
        buy = self.get(name, real)
        if not craft or name not in RECIPES:
            return buy, "buy"
        yld, ins = RECIPES[name]
        parts = [self.unit(i, real, craft)[0] for _, i in ins]
        if any(p is None for p in parts):
            return buy, "buy"
        made = sum(q * p for (q, _), p in zip(ins, parts)) / yld
        if buy is None or made < buy:
            return round(made), "craft"
        return buy, "buy"


def favor_of(crate: str, artisan: int | None) -> int | None:
    _, fav, _ = CRATES[crate]
    if fav is not None:
        return fav
    if artisan is None:
        return None
    return artisan * (2 if crate.split()[-1] in CRAFTED else 1)


def options(p: Prices, artisan: int | None, craft: bool) -> list[dict]:
    out = []
    for crate, (tier, _, bundles) in CRATES.items():
        fav = favor_of(crate, artisan)
        cname = f"Waylaid Crate: {crate}"
        for qty, item in bundles:
            row = {"crate": crate, "tier": tier, "favor": fav, "bundle": f"{qty} x {item}",
                   "avail": p.listings(cname), "item": item, "qty": qty, "mat_listings": p.listings(item)}
            for mode in ("cheap", "real"):
                c = p.get(cname, mode == "real")
                u, how = p.unit(item, mode == "real", craft)
                if c is None or u is None:
                    row[mode] = None
                    continue
                net = c + qty * u - (fav or 0) * REFUND_PER_FAVOR
                row[mode] = {"upfront": c + qty * u, "net": net, "per": net / fav if fav else None,
                             "crate": c, "mats": qty * u, "how": how}
            out.append(row)
    return out


def best_per_crate(opts: list[dict]) -> list[dict]:
    best: dict[str, dict] = {}
    for o in opts:
        if o["real"] is None or o["real"]["per"] is None:
            continue
        cur = best.get(o["crate"])
        if cur is None or o["real"]["per"] < cur["real"]["per"]:
            best[o["crate"]] = o
    return sorted(best.values(), key=lambda o: o["real"]["per"])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=int, help="Favor to reach")
    ap.add_argument("--budget", type=float, help="gold to spend")
    ap.add_argument("--artisan", type=int, help="assume Artisan white crates give N Favor (crafted 2N)")
    ap.add_argument("--craft", action="store_true", help="make bars/bolts from raw mats when cheaper")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--stack", type=int, default=5, help="assumed units per material listing")
    a = ap.parse_args()

    p = Prices(sqlite3.connect(f"file:{DB}?mode=ro", uri=True))
    opts = options(p, a.artisan, a.craft)
    print(f"Prices from TSM scan at ts {p.ts}. Net = crate + mats - {REFUND_PER_FAVOR}c x Favor refund.")
    print("'real' prices use max(cheapest, recent market value).")
    if any(v[1] is None for v in p.by_name.values()):
        print("Listing counts are the last ones the push feed saw (before 18 Nov); the public CSV has none.")
    print()

    rows = sorted((o for o in opts if o["real"]), key=lambda o: (o["real"]["per"] is None, o["real"]["per"] or 0))
    if not a.all:
        rows = best_per_crate(opts) + [o for o in best_unranked(opts)]
    print(f"{'crate':24} {'fav':>3} {'bundle':30} {'crate$':>8} {'mats':>9} {'net/Favor':>10} "
          f"{'cheapest/F':>10} {'listed':>6}")
    for o in rows:
        r, c = o["real"], o["cheap"]
        per = money(r["per"]) if r["per"] is not None else "?"
        cper = money(c["per"]) if c and c["per"] is not None else "?"
        tag = " (craft)" if r["how"] == "craft" else ""
        print(f"{o['crate']:24} {o['favor'] or '?':>3} {o['bundle'] + tag:30} {money(r['crate']):>8} "
              f"{money(r['mats']):>9} {per:>10} {cper:>10} {o['avail']:>6}")

    if a.target or a.budget:
        plan(opts, a.target, a.budget * 10000 if a.budget else None, a.stack)


def best_unranked(opts: list[dict]) -> list[dict]:
    """Artisan crates without a Favor figure: cheapest upfront bundle each."""
    best: dict[str, dict] = {}
    for o in opts:
        if o["favor"] is None and o["real"]:
            cur = best.get(o["crate"])
            if cur is None or o["real"]["upfront"] < cur["real"]["upfront"]:
                best[o["crate"]] = o
    return sorted(best.values(), key=lambda o: o["real"]["upfront"])


def plan(opts: list[dict], target: int | None, budget: float | None, stack: int) -> None:
    """Greedy over every bundle by net per Favor, limited by crate and material listings."""
    print(f"\nBuy plan (first crate at cheapest, rest at market value; {stack} units per material listing):")
    ranked = sorted((o for o in opts if o["real"] and o["real"]["per"] is not None), key=lambda o: o["real"]["per"])
    crates_left = {o["crate"]: o["avail"] for o in ranked}
    mats_left = {o["item"]: o["mat_listings"] * stack for o in ranked}
    fav = spent = upfront = 0
    for o in ranked:
        if (target and fav >= target) or (budget and upfront >= budget):
            break
        r, c = o["real"], o["cheap"]
        n = min(crates_left[o["crate"]], mats_left[o["item"]] // o["qty"])
        if target:
            n = min(n, -(-(target - fav) // o["favor"]))
        if budget:
            n = min(n, int((budget - upfront) // r["upfront"]))
        if n <= 0:
            continue
        crates_left[o["crate"]] -= n
        mats_left[o["item"]] -= n * o["qty"]
        cost_up = c["upfront"] + (n - 1) * r["upfront"]
        cost_net = c["net"] + (n - 1) * r["net"]
        fav += n * o["favor"]
        spent += cost_net
        upfront += cost_up
        print(f"  {n:4} x {o['crate']:24} {o['bundle']:28} {money(r['per']):>6}/F  +{n * o['favor']:5} Favor  "
              f"{money(cost_up):>10} upfront   running {fav:5} Favor")
    print(f"\n  => {fav} Favor for {money(upfront)} upfront, {money(spent)} after refunds "
          f"({money(spent / fav) if fav else '?'} per Favor)")

if __name__ == "__main__":
    main()
