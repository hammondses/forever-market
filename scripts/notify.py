"""Push ntfy alerts for guide materials after each hourly ingest.

Only materials the levelling guides use (table `useful`, built by useful.py) with
at least MIN_PER_PLAYER per levelling player and MIN_SOLD sold a day in the region
are considered. Alerts:

    TURN   cheapest up >5% and auctions down >10% (or market value up >5% when
           auction counts are missing) against every earlier window
           (6h, 24h, 3d where available; needs at least two), see report.turn_signal
    CHEAP  cheapest listing at or under CHEAP_X times the vendor price
    SPIKE  cheapest up SPIKE_PCT or more over 24h (a chance to sell holdings)

An alert fires when its condition becomes true, at most once per COOLDOWN for the
same item and kind; state is kept in the alert_state table. All alerts from one
run go out as a single notification.

    notify.py            send
    notify.py --dry-run  print what would be sent, change nothing
    notify.py --test     send a test notification
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
import urllib.request
from pathlib import Path

from report import DB, HOUR, Market, cnt, money, turn_signal

NTFY_URL = "http://192.168.1.34/wow-market"
TOKEN_FILE = Path.home() / ".config" / "wow-market" / "ntfy.token"
MIN_PER_PLAYER = 20
MIN_SOLD = 100
CHEAP_X = 1.15
SPIKE_PCT = 50
COOLDOWN = 24 * HOUR


def send(title: str, body: str, priority: str = "default", tags: str = "moneybag") -> None:
    req = urllib.request.Request(
        NTFY_URL,
        data=body.encode(),
        method="POST",
        headers={
            "Authorization": f"Bearer {TOKEN_FILE.read_text().strip()}",
            "Title": title,
            "Priority": priority,
            "Tags": tags,
        },
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        resp.read()


def candidates(m: Market) -> dict[str, tuple[float, str]]:
    return {
        i: (pp, by)
        for i, pp, by in m.db.execute("SELECT id, per_player, professions FROM useful WHERE per_player >= ?",
                                      (MIN_PER_PLAYER,))
        if m.sold.get(i, 0) >= MIN_SOLD
    }


def conditions(m: Market, items: dict[str, tuple[float, str]]) -> dict[tuple[str, str], str]:
    """{(item, kind): message line} for every condition true right now."""
    now = m.book(m.now)
    w6, w24, w72 = m.snap_at(6), m.snap_at(24), m.snap_at(72)
    day = m.book(w24 or w6)
    out = {}
    for i in items:
        if i not in now or not now[i][0]:
            continue
        b, n = now[i]
        name, v = m.name(i), m.vendor(i)
        old = day.get(i)
        if turn_signal(m, i, [w6, w24, w72]) == "TURN" and old:
            out[(i, "TURN")] = (f"TURN {name}: {money(old[0])} -> {money(b)}, auctions {cnt(old[1])} -> {cnt(n)}"
                                f" ({m.xv(i, b)}x vendor, {m.sold.get(i, 0):,.0f}/day)")
        if v and b <= CHEAP_X * v:
            out[(i, "CHEAP")] = (f"CHEAP {name}: {money(b)} = {b / v:.2f}x vendor ({money(v)}),"
                                 f" {cnt(n)} auctions, {m.sold.get(i, 0):,.0f}/day")
        if w24 and old and old[0] and b >= old[0] * (1 + SPIKE_PCT / 100):
            out[(i, "SPIKE")] = (f"SPIKE {name}: {money(old[0])} -> {money(b)} "
                                 f"(+{(b / old[0] - 1) * 100:.0f}% in 24h), auctions {cnt(old[1])} -> {cnt(n)}")
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    if a.test:
        send("WoW market alerts are on", "Turn signals, near-vendor buys and price spikes for guide materials.",
             tags="white_check_mark")
        print("sent test")
        return

    db = sqlite3.connect(DB)
    db.execute("CREATE TABLE IF NOT EXISTS alert_state(item TEXT, kind TEXT, active INTEGER, "
               "last_sent INTEGER, PRIMARY KEY(item, kind))")
    m = Market(db)
    items = candidates(m)
    current = conditions(m, items)
    state = {(i, k): (act, sent) for i, k, act, sent in db.execute("SELECT * FROM alert_state")}

    fire = []
    for key, line in current.items():
        active, last_sent = state.get(key, (0, 0))
        if not active and m.now - (last_sent or 0) >= COOLDOWN:
            fire.append((key, line))
    order = {"TURN": 0, "SPIKE": 1, "CHEAP": 2}
    fire.sort(key=lambda x: (order[x[0][1]], -items[x[0][0]][0]))

    if a.dry_run:
        print(f"{len(items)} materials watched; {len(current)} conditions true; would send {len(fire)}:")
        for _, line in fire:
            print(" ", line)
        return

    if fire:
        kinds = [k for (_, k), _ in fire]
        title = "WoW market: " + ", ".join(f"{kinds.count(k)} {k.lower()}" for k in order if k in kinds)
        send(title, "\n".join(line for _, line in fire),
             priority="high" if "TURN" in kinds else "default",
             tags="chart_with_upwards_trend" if "TURN" in kinds else "moneybag")
    fired = {k for k, _ in fire}
    keys = set(state) | set(current)
    for key in keys:
        last_sent = m.now if key in fired else state.get(key, (0, 0))[1]
        db.execute("INSERT OR REPLACE INTO alert_state VALUES (?,?,?,?)",
                   (*key, 1 if key in current else 0, last_sent))
    db.commit()
    print(f"notify: {len(current)} conditions, sent {len(fire)}")


if __name__ == "__main__":
    sys.exit(main())
