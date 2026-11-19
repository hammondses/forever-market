"""Fetch our auction house straight from Blizzard's Game Data API into data/market.db.

    GET https://us.api.blizzard.com/data/wow/ruleset/1/auctions/113[/commodities]
        ?namespace=dynamic-forever-us
    (unofficial Forever routes; house 113 = our Horde house, matched against TSM's
    pvp-horde prices on 19 Nov 2026: 2311 exact lowest prices vs <460 for any other)

Each snapshot (newest Last-Modified of the two responses) goes into
auctiondb_non_commodity_data under the same scope as before: minBuyout is the
cheapest per-unit buyout, numAuctions the number of listings (what the old push
feed counted). marketValueRecent is NULL; TSM's public CSV still supplies the
market values, historical prices and region sales. Raw responses are kept
gzipped in data/raw/blizzard/. Client credentials: ~/.config/wow-market/blizzard.env.
"""

from __future__ import annotations

import base64
import gzip
import json
import os
import sys
import urllib.parse
import urllib.request
from email.utils import parsedate_to_datetime
from pathlib import Path

from ingest import connect

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "raw" / "blizzard"
CREDS = Path.home() / ".config" / "wow-market" / "blizzard.env"
HOUSE = "https://us.api.blizzard.com/data/wow/ruleset/1/auctions/113"
NS = "?namespace=dynamic-forever-us"
SCOPE = "realm1098-HORDE"


def token() -> str:
    env = os.environ if "BLIZZARD_CLIENT_SECRET" in os.environ else \
        dict(line.strip().split("=", 1) for line in CREDS.read_text().splitlines() if "=" in line)
    basic = base64.b64encode(f"{env['BLIZZARD_CLIENT_ID']}:{env['BLIZZARD_CLIENT_SECRET']}".encode()).decode()
    req = urllib.request.Request("https://oauth.battle.net/token", data=b"grant_type=client_credentials",
                                 headers={"Authorization": f"Basic {basic}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["access_token"]


def fetch(url: str, tok: str) -> tuple[int, bytes]:
    """(Last-Modified epoch, raw JSON bytes)"""
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {tok}", "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=120) as r:
        raw = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            raw = gzip.decompress(raw)
        return int(parsedate_to_datetime(r.headers["Last-Modified"]).timestamp()), raw


def book(listings: list[dict], price_key: str, out: dict[int, list[int]]) -> None:
    """Fold listings into {item: [cheapest per unit, listings]}."""
    for a in listings:
        p = a.get(price_key)
        if not p:  # bid-only auctions have no buyout
            continue
        if price_key == "buyout":
            p //= a["quantity"]
        cur = out.setdefault(a["item"]["id"], [p, 0])
        cur[0] = min(cur[0], p)
        cur[1] += 1


def main() -> None:
    tok = token()
    ts_r, raw_r = fetch(HOUSE + NS, tok)
    ts_c, raw_c = fetch(HOUSE + "/commodities" + NS, tok)
    ts = max(ts_r, ts_c)
    name = f"blizzard-113-{ts}"
    db = connect()
    if db.execute("SELECT 1 FROM files WHERE name=?", (name,)).fetchone():
        print(f"blizzard snapshot {ts} already loaded")
        sys.exit(3 if "--new-or-3" in sys.argv else 0)
    items: dict[int, list[int]] = {}
    book(json.loads(raw_r).get("auctions", []), "buyout", items)
    book(json.loads(raw_c).get("auctions", []), "unit_price", items)
    if not items:
        sys.exit(f"blizzard snapshot {ts}: no auctions, not loading")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{name}.json.gz").write_bytes(gzip.compress(raw_r))
    (OUT / f"{name}-commodities.json.gz").write_bytes(gzip.compress(raw_c))
    db.executemany("INSERT OR REPLACE INTO auctiondb_non_commodity_data"
                   "(scope, ts, item, minBuyout, numAuctions, marketValueRecent) VALUES (?,?,?,?,?,NULL)",
                   [(SCOPE, ts, str(i), p, n) for i, (p, n) in items.items()])
    db.execute("INSERT OR REPLACE INTO files VALUES (?,?,?,?)", (name, SCOPE, "BLIZZARD", ts))
    db.commit()
    print(f"blizzard snapshot {ts}: {len(items)} items")


if __name__ == "__main__":
    main()
