"""Market report for US Forever PvP Horde from data/market.db.

    report.py                  watchlist, turn signals, movers, near-vendor buys
    report.py --item "iron"    history for items whose name contains the text
    report.py --all            movers over every item class, not just Trade Goods

Prices are copper in the database and shown as g/s/c. "x vend" is the cheapest
listing divided by the vendor sell price.
"""

from __future__ import annotations

import argparse
import sqlite3
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "data" / "market.db"
SCOPE = "realm1098-HORDE"
REGION = "region29"

WATCH = [
    "Iron Ore", "Iron Bar", "Steel Bar", "Mithril Ore", "Mithril Bar", "Truesilver Bar",
    "Thorium Bar", "Silk Cloth", "Mageweave Cloth", "Runecloth", "Heavy Leather",
    "Thick Leather", "Rugged Leather",
]
HOUR = 3600


def money(c: float | None) -> str:
    if c is None:
        return "-"
    c = int(round(c))
    g, s, cc = c // 10000, c // 100 % 100, c % 100
    if g:
        return f"{g}g{s:02d}s"
    if s:
        return f"{s}s{cc:02d}"
    return f"{cc}c"


def cnt(n: int | None) -> str:
    return "-" if n is None else str(n)


def pct(new: float | None, old: float | None) -> str:
    if not new or not old:
        return "-"
    return f"{(new / old - 1) * 100:+.0f}%"


class Market:
    def __init__(self, db: sqlite3.Connection) -> None:
        self.db = db
        self.snaps = [r[0] for r in db.execute(
            "SELECT DISTINCT ts FROM auctiondb_non_commodity_data WHERE scope=? ORDER BY ts", (SCOPE,))]
        if not self.snaps:
            raise SystemExit("No data yet: run scripts/run.sh")
        self.now = self.snaps[-1]
        self.items = {r[0]: r[1:] for r in db.execute("SELECT id, name, class, vendor FROM items")}
        sale = db.execute(
            "SELECT item, regionSoldPerDay FROM auctiondb_region_sale WHERE scope=? AND ts="
            "(SELECT max(ts) FROM auctiondb_region_sale WHERE scope=?)", (REGION, REGION))
        self.sold = {i: v / 1000 for i, v in sale}
        self._cache: dict[int, dict[str, tuple[int, int | None]]] = {}
        self._mv: dict[int, dict[str, int]] = {}

    def snap_at(self, ago_hours: float) -> int | None:
        """Newest snapshot at least ago_hours older than the latest (25% slack)."""
        target = self.now - ago_hours * HOUR
        older = [t for t in self.snaps if t <= target + ago_hours * HOUR * 0.25]
        if not older or older[-1] == self.now:
            return None
        return older[-1]

    def book(self, ts: int | None) -> dict[str, tuple[int, int | None]]:
        """{item: (cheapest, auctions)}; auctions is None for public-CSV snapshots."""
        if ts is None:
            return {}
        if ts not in self._cache:
            self._cache[ts] = {i: (b, n) for i, b, n in self.db.execute(
                "SELECT item, minBuyout, numAuctions FROM auctiondb_non_commodity_data "
                "WHERE scope=? AND ts=?", (SCOPE, ts))}
        return self._cache[ts]

    def recent(self, ts: int | None) -> dict[str, int]:
        """{item: TSM's recent market value} at ts."""
        if ts is None:
            return {}
        if ts not in self._mv:
            self._mv[ts] = {i: v for i, v in self.db.execute(
                "SELECT item, marketValueRecent FROM auctiondb_non_commodity_data "
                "WHERE scope=? AND ts=? AND marketValueRecent > 0", (SCOPE, ts))}
        return self._mv[ts]

    def name(self, item: str) -> str:
        return (self.items.get(item) or (item,))[0] or item

    def vendor(self, item: str) -> int | None:
        it = self.items.get(item)
        return it[2] if it else None

    def is_trade(self, item: str) -> bool:
        it = self.items.get(item)
        return bool(it and it[1] == "T")

    def xv(self, item: str, price: int) -> str:
        v = self.vendor(item)
        return f"{price / v:.2f}" if v and price else "-"


def turn_signal(m: Market, item: str, windows: list[int | None]) -> str:
    """'TURN' when the cheapest listing rose and supply tightened against every
    available earlier window; 'turn?' when only the newest window agrees.

    Supply is auctions down >10% when both snapshots have auction counts. The
    public CSV has none, so then it is TSM's recent market value up >5% instead
    (the whole book moving up, not just one cheap listing selling)."""
    now = m.book(m.now).get(item)
    if not now or not now[0]:
        return ""
    mv_now = m.recent(m.now).get(item)
    votes = []
    for ts in windows:
        old = m.book(ts).get(item)
        if not old or not old[0]:
            continue
        if now[1] is not None and old[1]:
            supply = now[1] < old[1] * 0.9
        elif mv_now and (mv_old := m.recent(ts).get(item)):
            supply = mv_now > mv_old * 1.05
        else:
            continue
        votes.append(supply and now[0] > old[0] * 1.05)
    if not votes:
        return ""
    if all(votes) and len(votes) >= 2:
        return "TURN"
    if votes[0]:
        return "turn?"
    return ""


def report(m: Market, all_classes: bool) -> None:
    span = (m.now - m.snaps[0]) / HOUR
    print(f"Latest TSM scan {time.strftime('%Y-%m-%d %H:%M', time.localtime(m.now))}, "
          f"{len(m.snaps)} snapshots over {span:.0f}h")
    if span < 6:
        print("History is under 6 hours: changes and turn signals fill in as hourly snapshots arrive.")
    w = {h: m.snap_at(h) for h in (6, 24, 72, 168)}
    windows = [w[6], w[24], w[72]]
    now = m.book(m.now)
    by_name = {}
    for item in now:
        by_name.setdefault(m.name(item), item)

    print("\nWATCHLIST")
    print(f"{'item':<17}{'cheapest':>9}{'x vend':>7}{'auct':>6}{'6h':>6}{'24h':>6}{'3d':>6}{'7d':>6}"
          f"{'auct24h':>8}{'sold/d':>8}  signal")
    for nm in WATCH:
        item = by_name.get(nm)
        if not item:
            continue
        b, n = now[item]
        ch = [pct(b, m.book(w[h]).get(item, (None,))[0]) for h in (6, 24, 72, 168)]
        a24 = pct(n, m.book(w[24]).get(item, (None, None))[1])
        sold = m.sold.get(item)
        print(f"{nm:<17}{money(b):>9}{m.xv(item, b):>7}{cnt(n):>6}{ch[0]:>6}{ch[1]:>6}{ch[2]:>6}{ch[3]:>6}"
              f"{a24:>8}{(f'{sold:,.0f}' if sold else '-'):>8}  {turn_signal(m, item, windows)}")

    pool = [i for i in now if all_classes or m.is_trade(i)]
    turns = [(i, turn_signal(m, i, windows)) for i in pool]
    turns = [(i, s) for i, s in turns if s and (now[i][1] is None or now[i][1] >= 3) and m.sold.get(i, 0) >= 20]
    print("\nTURN SIGNALS (cheapest up >5% and auctions down >10%, or market value up >5% where "
          "auction counts are missing; TURN = every window agrees)")
    if not turns:
        print("  none yet")
    for i, s in sorted(turns, key=lambda x: (x[1] != "TURN", -m.sold.get(x[0], 0)))[:25]:
        b, n = now[i]
        old = m.book(w[24] or w[6]).get(i, (0, 0))
        print(f"  {s:<6}{m.name(i):<28}{money(old[0]):>8} -> {money(b):<8} auctions {cnt(old[1])} -> {cnt(n)}"
              f"  sold/d {m.sold.get(i, 0):,.0f}")

    ref = w[24] or w[6]
    if ref:
        old = m.book(ref)
        hrs = (m.now - ref) / HOUR
        moves = []
        for i in pool:
            if i in old and old[i][0] and now[i][0] and (now[i][1] is None or now[i][1] >= 5) and m.sold.get(i, 0) >= 20:
                moves.append((now[i][0] / old[i][0] - 1, i))
        moves.sort()
        print(f"\nMOVERS over {hrs:.0f}h ({'all classes' if all_classes else 'Trade Goods'}, "
              f"5+ auctions, 20+ sold/day region)")
        for label, part in (("up", moves[::-1][:12]), ("down", moves[:12])):
            print(f"  {label}:")
            for ch, i in part:
                print(f"    {ch * 100:+5.0f}%  {m.name(i):<28}{money(old[i][0]):>8} -> {money(now[i][0]):<8}"
                      f" auct {cnt(old[i][1])}->{cnt(now[i][1])}")

    print("\nNEAR VENDOR FLOOR (Trade Goods, cheapest <= 1.5x vendor, 50+ sold/day region)")
    floor = []
    for i in now:
        v = m.vendor(i)
        b, n = now[i]
        if m.is_trade(i) and v and b and b <= 1.5 * v and m.sold.get(i, 0) >= 50:
            floor.append((b / v, i))
    for r, i in sorted(floor)[:25]:
        print(f"  {r:4.2f}x  {m.name(i):<28}{money(now[i][0]):>8}  vendor {money(m.vendor(i)):<7}"
              f" auct {cnt(now[i][1]):<5} sold/d {m.sold.get(i, 0):,.0f}")


def item_history(m: Market, text: str) -> None:
    ids = [i for i, v in m.items.items() if v[0] and text.lower() in v[0].lower()]
    if not ids:
        raise SystemExit(f"No item matches {text!r}")
    for i in ids[:8]:
        rows = m.db.execute(
            "SELECT ts, minBuyout, numAuctions, marketValueRecent FROM auctiondb_non_commodity_data "
            "WHERE scope=? AND item=? ORDER BY ts", (SCOPE, i)).fetchall()
        if not rows:
            continue
        print(f"\n{m.name(i)} ({i})  vendor {money(m.vendor(i))}  region sold/d {m.sold.get(i, 0):,.0f}")
        step = max(1, len(rows) // 40)
        for ts, b, n, mv in rows[::step] + ([rows[-1]] if (len(rows) - 1) % step else []):
            print(f"  {time.strftime('%m-%d %H:%M', time.localtime(ts))}  cheapest {money(b):>8}"
                  f"  x vend {m.xv(i, b):>5}  auctions {cnt(n):>5}  recent mv {money(mv):>8}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--item")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    m = Market(sqlite3.connect(DB))
    if a.item:
        item_history(m, a.item)
    else:
        report(m, a.all)


if __name__ == "__main__":
    main()
