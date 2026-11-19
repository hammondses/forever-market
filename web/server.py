"""Azeroth Exchange: read-only web UI over data/market.db.

    GET /                 the page (web/index.html)
    GET /api/map?w=24     every tradeable material with % change over w hours
                          (w=hist compares with TSM's realm historical price)
    GET /api/item/<id>    snapshot history for one item
    GET /api/ah           every item listed in the latest snapshot
    GET /api/names        {id: [name, quality, ilvl, ...]} for the live AH
    GET /api/token        Blizzard token so the page can read the AH live

Run: .venv/bin/python web/server.py [port]   (systemd user unit wow-market-web)
"""

from __future__ import annotations

import gzip
import json
import re
import sqlite3
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from report import DB, SCOPE, Market, turn_signal

PAGE = Path(__file__).with_name("index.html")

SECTORS = [
    ("Metal & Stone", r"\b(bar|ore|stone|flux|blasting powder|grinding|coal|bauxite|pyrite|pitchblende|torbernite)\b"),
    ("Cloth", r"\b(cloth|mooncloth|bolt|runecloth|mageweave|felcloth|spider's silk|ironweb|shadow silk|silk)\b"),
    ("Parts", (
        r"\b(tube|casing|widget|trigger|adjustor|rod|converter|thread|dye|bleach|oil|salt|flour|"
        r"bolts|gears|powder|blasting|fuse|spices|vial|wire|wiring|frame|framework|modulator|gizmo|strut|"
        r"gyrochronatom|contact|cylinder|rocket fuel|buckle|stock|sandpaper|isospring)\b"
    )),
    ("Leather", r"\b(leather|hide|scale|scraps|pelt|dragonscale|feather)\b"),
    ("Enchanting", r"\b(dust|essence|shard|crystal|mote of magic)\b"),
    ("Elemental", (
        r"\b(elemental|of fire|of water|of earth|of air|of undeath|core|ichor|mojo|"
        r"heart of the wild|living essence|globe of water)\b"
    )),
    ("Gems", (
        r"\b(ruby|pearl|jade|citrine|agate|tigerseye|malachite|shadowgem|opal|sapphire|emerald|"
        r"diamond|moonstone|aquamarine|azerothian)\b"
    )),
    ("Cooking", (
        r"\b(raw|meat|egg|flesh|fish|clam|snapper|catfish|yellowtail|trout|smallfish|salmon|"
        r"sagefish|ribs|tail|leg|wing|tender|chunk|venison|bear|boar|wolf|crocolisk|"
        r"spider|stringy|haunch|steak|cheese|sausage|eel|lobster|mightfish)\b"
    )),
    ("Herbs", (
        r"\b(peacebloom|silverleaf|earthroot|mageroyal|briarthorn|stranglekelp|bruiseweed|"
        r"wild steelbloom|grave moss|kingsblood|liferoot|fadeleaf|goldthorn|khadgar's whisker|"
        r"wintersbite|firebloom|purple lotus|arthas' tears|sungrass|blindweed|ghost mushroom|"
        r"gromsblood|golden sansam|dreamfoil|mountain silversage|plaguebloom|icecap|"
        r"black lotus|swiftthistle|bloodthistle|wildvine|frilled lichen|rosecap|demonsage|marefoil|stranglevine|lotus|weed|bloom|moss|root|leaf)\b"
    )),
]
TICKERS = {
    "Iron Bar": "IRON", "Iron Ore": "IORE", "Mithril Bar": "MITH", "Mithril Ore": "MORE",
    "Truesilver Bar": "TRUE", "Thorium Bar": "THOR", "Thorium Ore": "TORE", "Copper Bar": "COPR",
    "Bronze Bar": "BRNZ", "Steel Bar": "STEL", "Tin Bar": "TIN", "Silver Bar": "SILV",
    "Gold Bar": "GOLD", "Silk Cloth": "SILK", "Mageweave Cloth": "MAGE", "Runecloth": "RUNE",
    "Wool Cloth": "WOOL", "Linen Cloth": "LINN", "Heavy Leather": "HVYL", "Thick Leather": "THKL",
    "Rugged Leather": "RUGL", "Medium Leather": "MEDL", "Light Leather": "LTL",
    "Arcanite Bar": "ARCN", "Arcane Crystal": "ACRY", "Dark Iron Bar": "DKIR",
}


def sector(name: str, profs: str) -> str:
    n = name.lower()
    for sec, pat in SECTORS:
        if re.search(pat, n):
            return sec
    if "alchemy" in profs:
        return "Herbs"
    if "cooking" in profs:
        return "Cooking"
    return "Other"


def ticker(name: str) -> str:
    if name in TICKERS:
        return TICKERS[name]
    words = re.findall(r"[A-Za-z]+", name)
    if not words:
        return name[:5].upper()
    if len(words) == 1:
        return words[0][:5].upper()
    return (words[0][:3] + "".join(w[0] for w in words[1:3])).upper()


def open_market() -> Market:
    return Market(sqlite3.connect(f"file:{DB}?mode=ro", uri=True))


def market_map(window: str) -> dict:
    m = open_market()
    now = m.book(m.now)
    useful = {i: (pp, by) for i, pp, by in m.db.execute("SELECT id, per_player, professions FROM useful")}
    hist: dict[str, int] = {}
    if window == "hist":
        hist = {i: h for i, h in m.db.execute(
            "SELECT item, historical FROM auctiondb_non_commodity_historical WHERE scope=? AND ts="
            "(SELECT max(ts) FROM auctiondb_non_commodity_historical WHERE scope=?)", (SCOPE, SCOPE))}
        ref_ts, prev = None, {}
    else:
        hours = float(window)
        ref_ts = m.snap_at(hours)
        prev = m.book(ref_ts)
    windows = [m.snap_at(6), m.snap_at(24), m.snap_at(72)]
    rows = []
    for i, (b, n) in now.items():
        if not b or not (m.is_trade(i) or i in useful):
            continue
        sold = m.sold.get(i, 0)
        if sold < 5:
            continue
        name = m.name(i)
        pp, by = useful.get(i, (0, ""))
        if window == "hist":
            old_b, old_n = hist.get(i), None
        else:
            old_b, old_n = prev.get(i, (None, None))
        rows.append({
            "id": i, "name": name, "ticker": ticker(name), "sector": sector(name, by),
            "price": b, "prev": old_b, "chg": (b / old_b - 1) * 100 if old_b else None,
            "auctions": n, "auctionsPrev": old_n, "sold": round(sold),
            "volume": round(sold * b), "vendor": m.vendor(i), "perPlayer": round(pp), "usedBy": by,
            "signal": turn_signal(m, i, windows),
        })
    return {
        "latest": m.now, "snapshots": len(m.snaps), "first": m.snaps[0], "window": window,
        "refTs": ref_ts, "items": rows, "server": int(time.time()),
    }


def item_history(item: str) -> dict:
    m = open_market()
    rows = m.db.execute(
        "SELECT ts, minBuyout, numAuctions, marketValueRecent, numUnits FROM auctiondb_non_commodity_data "
        "WHERE scope=? AND item=? ORDER BY ts", (SCOPE, item)).fetchall()
    useful = m.db.execute("SELECT per_player, professions FROM useful WHERE id=?", (item,)).fetchone()
    return {
        "id": item, "name": m.name(item), "vendor": m.vendor(item), "sold": m.sold.get(item),
        "perPlayer": useful[0] if useful else 0, "usedBy": useful[1] if useful else "",
        "series": [{"ts": t, "price": b, "auctions": n, "mv": mv, "units": u} for t, b, n, mv, u in rows],
    }


RESET_WINDOWS = (3, 24, 72)
RESET_BUY_BELOW = 0.9   # a reset buys every listing under 90% of the resale price
RESET_FLAT = 15         # price "holding" means within +/-15% of the earlier snapshot
RESET_DRAIN = -15       # supply "draining" means units (or listings) down 15% or more
AH_CUT = 0.05
RESET_MEDIAN_DAYS = 7


def latest_ladders() -> dict[str, list[list[int]]]:
    """{item: [[unit price, units], ...] cheapest first} from the newest Blizzard commodities file."""
    from blizzard_collect import OUT
    files = sorted(OUT.glob("blizzard-113-*-commodities.json.gz"))
    if not files:
        return {}
    steps: dict[str, dict[int, int]] = {}
    for a in json.loads(gzip.decompress(files[-1].read_bytes())).get("auctions", []):
        if a.get("unit_price"):
            d = steps.setdefault(str(a["item"]["id"]), {})
            d[a["unit_price"]] = d.get(a["unit_price"], 0) + a["quantity"]
    return {i: sorted([p, q] for p, q in d.items()) for i, d in steps.items()}


def resets() -> dict:
    """Materials ranked for a market reset.

    For each commodity on our AH: what buying every listing under RESET_BUY_BELOW x the
    resale price costs and returns, and how supply (units, else listings) and the cheapest
    price moved over RESET_WINDOWS. "Ripe" = supply draining while the price holds: the
    population has levelled past the item, so a reset sticks.
    """
    m = open_market()
    ladders = latest_ladders()
    catalog = item_names()
    hist = {i: h for i, h in m.db.execute(
        "SELECT item, historical FROM auctiondb_non_commodity_historical WHERE scope=? AND ts="
        "(SELECT max(ts) FROM auctiondb_non_commodity_historical WHERE scope=?)", (SCOPE, SCOPE))}
    region = {i: v for i, v in m.db.execute(
        "SELECT item, regionMarketValue FROM auctiondb_region_stat WHERE ts="
        "(SELECT max(ts) FROM auctiondb_region_stat)")}

    # resale price: median cheapest listing over the last RESET_MEDIAN_DAYS, not a peak or TSM average
    series: dict[str, list[int]] = {}
    for i, b in m.db.execute(
            "SELECT item, minBuyout FROM auctiondb_non_commodity_data WHERE scope=? AND ts>=? AND minBuyout>0",
            (SCOPE, time.time() - RESET_MEDIAN_DAYS * 86400)):
        series.setdefault(i, []).append(b)
    median = {i: sorted(v)[len(v) // 2] for i, v in series.items() if len(v) >= 3}

    def supply(ts: int | None) -> dict[str, tuple]:
        if ts is None:
            return {}
        return {i: (b, n, u) for i, b, n, u in m.db.execute(
            "SELECT item, minBuyout, numAuctions, numUnits FROM auctiondb_non_commodity_data "
            "WHERE scope=? AND ts=?", (SCOPE, ts))}

    # compare Blizzard snapshots only: the TSM CSV ones carry no counts
    snaps = [t for (t,) in m.db.execute("SELECT ts FROM files WHERE tag='BLIZZARD' ORDER BY ts")]
    latest = snaps[-1] if snaps else m.now

    def ago(w: int) -> int | None:
        older = [t for t in snaps if t <= latest - w * 3600 * 0.75]
        return older[-1] if older else None

    now = supply(latest)
    then = {w: supply(ago(w)) for w in RESET_WINDOWS}
    rows = []
    for i, ladder in ladders.items():
        cur = now.get(i)
        # median of our own history; TSM's lower realm/region average until there are 3 snapshots
        target = median.get(i) or (min(v for v in (hist.get(i), region.get(i)) if v) if (hist.get(i) or region.get(i)) else None)
        if not cur or not target:
            continue
        units = sum(q for _, q in ladder)
        buy = [(p, q) for p, q in ladder if p < target * RESET_BUY_BELOW]
        cost = sum(p * q for p, q in buy)
        got = sum(q for _, q in buy)
        trend = {}
        for w in RESET_WINDOWS:
            old = then[w].get(i)
            if not old:
                continue
            ob, on, ou = old
            if ou and cur[2] is not None:
                sup, basis = (cur[2] / ou - 1) * 100, "units"
            elif on and cur[1] is not None:
                sup, basis = (cur[1] / on - 1) * 100, "listings"
            else:
                continue
            trend[w] = {"hours": round((latest - ago(w)) / 3600), "supply": round(sup, 1), "basis": basis,
                        "price": round((cur[0] / ob - 1) * 100, 1) if ob else None}
        row = catalog.get(i) or [m.name(i)]
        ilvl = row[2] if len(row) > 2 and row[2] else None
        rows.append({
            "id": i, "name": row[0] or m.name(i), "q": row[1] if len(row) > 1 else 1, "ilvl": ilvl,
            "price": cur[0], "target": target, "units": units, "listings": cur[1],
            "cost": cost, "buyUnits": got, "profit": round(got * target * (1 - AH_CUT) - cost),
            "sold": round(m.sold.get(i, 0)), "vendor": m.vendor(i), "trend": trend,
            "ripe": any(t["supply"] <= RESET_DRAIN and t["price"] is not None and abs(t["price"]) <= RESET_FLAT
                        for w, t in trend.items() if w >= 24),  # a 3h dip is noise
            "ladder": ladder[:40],
        })
    return {"latest": latest, "windows": RESET_WINDOWS, "buyBelow": RESET_BUY_BELOW, "flat": RESET_FLAT,
            "drain": RESET_DRAIN, "medianDays": RESET_MEDIAN_DAYS, "items": rows}


HIST_BUCKETS = 64
HIST_DAYS = 14


def hist_buckets() -> list[dict]:
    """Price history for every item, split into HIST_BUCKETS files by int(id) % HIST_BUCKETS.

    {id: [[ts, cheapest, auctions, units], ...]} over the last HIST_DAYS; the AH tab charts these.
    """
    out: list[dict] = [{} for _ in range(HIST_BUCKETS)]
    rows = open_market().db.execute(
        "SELECT item, ts, minBuyout, numAuctions, numUnits FROM auctiondb_non_commodity_data "
        "WHERE scope=? AND ts>=? AND minBuyout>0 ORDER BY ts", (SCOPE, time.time() - HIST_DAYS * 86400))
    for i, t, b, n, u in rows:
        if not i.isdigit():
            continue  # TSM variant keys like i:285282::i1
        out[int(i) % HIST_BUCKETS].setdefault(i, []).append([t, b, n, u])
    return out


_token: dict = {}


def blizzard_token() -> dict:
    """Same as the Pages Function web/functions/api/token.js, for the local server."""
    from blizzard_collect import token
    if _token.get("expires", 0) - time.time() * 1000 < 3600e3:
        _token.update(token=token(), expires=(time.time() + 86000) * 1000)
    return _token


def item_names() -> dict:
    """{id: [name, quality, ilvl, reqLevel, class, subclass, slot, vendorSell]} for the live AH.

    Blizzard metadata from item_catalog.py where we have it, otherwise just TSM's name.
    """
    cat = ROOT / "data" / "catalog" / "items.json"
    out = json.loads(cat.read_text()) if cat.exists() else {}
    for i, n in open_market().db.execute("SELECT id, name FROM items WHERE name IS NOT NULL"):
        if not out.get(i):
            out[i] = [n]
    return {i: r for i, r in out.items() if r and r[0]}


def ah_book() -> dict:
    """Every item on our auction house in the latest snapshot: [id, name, price, listings, vendor]."""
    m = open_market()
    rows = [[i, m.name(i), b, n, m.vendor(i)] for i, (b, n) in m.book(m.now).items() if b]
    rows.sort(key=lambda r: r[1] or "")
    return {"latest": m.now, "items": rows}


class Handler(BaseHTTPRequestHandler):
    def _send(self, code: int, body: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        url = urlparse(self.path)
        try:
            if url.path == "/":
                self._send(200, PAGE.read_bytes(), "text/html; charset=utf-8")
            elif url.path == "/api/map":
                w = parse_qs(url.query).get("w", ["24"])[0]
                if w != "hist" and not re.fullmatch(r"\d+(\.\d+)?", w):
                    raise ValueError("bad window")
                self._send(200, json.dumps(market_map(w)).encode(), "application/json")
            elif url.path == "/api/resets":
                self._send(200, json.dumps(resets()).encode(), "application/json")
            elif url.path == "/api/token":
                self._send(200, json.dumps(blizzard_token()).encode(), "application/json")
            elif url.path == "/api/names":
                self._send(200, json.dumps(item_names()).encode(), "application/json")
            elif m := re.fullmatch(r"/api/hist/(\d+)", url.path):
                self._send(200, json.dumps(hist_buckets()[int(m.group(1)) % HIST_BUCKETS]).encode(), "application/json")
            elif url.path == "/api/icons":
                f = ROOT / "data" / "catalog" / "icons.json"
                self._send(200, f.read_bytes() if f.exists() else b"{}", "application/json")
            elif url.path == "/api/ah":
                self._send(200, json.dumps(ah_book()).encode(), "application/json")
            elif m := re.fullmatch(r"/api/item/(\d+)", url.path):
                self._send(200, json.dumps(item_history(m.group(1))).encode(), "application/json")
            else:
                self._send(404, b"not found", "text/plain")
        except (ValueError, SystemExit) as e:
            self._send(400, str(e).encode(), "text/plain")

    def log_message(self, fmt: str, *args: object) -> None:
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8790
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
