"""Fetch TSM's public price CSVs (no sign-in) and load them into data/market.db.

    realm  forever/us/realm/pvp-horde/items.csv
           itemId,name,marketValue,minBuyout,recent,historical,updatedAt
    region forever/us/region/items.csv
           itemId,name,marketValue,historical,avgSalePrice,saleRate,soldPerDay,updatedAt

Each realm scan (one updatedAt) fills the market-value and historical tables.
Since 19 Nov 2026 the cheapest-price snapshots come from Blizzard's API instead
(blizzard_collect.py); TSM rows from 18-19 Nov have NULL numAuctions. Region soldPerDay and saleRate are stored x1000 as before.
Files are kept gzipped in data/raw/public/ and recorded in the files table, so
re-running with an unchanged scan does nothing.
"""

from __future__ import annotations

import csv
import gzip
import io
import sqlite3
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

from ingest import connect

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "raw" / "public"
NAMES = ROOT / "data" / "catalog" / "tsm-realm-items.csv"
BASE = "https://public-data.tradeskillmaster.com/forever/us/"
SCOPE, REGION = "realm1098-HORDE", "region29"
REALM_COLS = ["itemId", "name", "marketValue", "minBuyout", "recent", "historical", "updatedAt"]
REGION_COLS = ["itemId", "name", "marketValue", "historical", "avgSalePrice", "saleRate", "soldPerDay", "updatedAt"]


def fetch(path: str) -> bytes:
    req = urllib.request.Request(BASE + path, headers={"User-Agent": "wow-market (personal tracker)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def parse(raw: bytes, cols: list[str]) -> tuple[int, list[dict]]:
    """Rows from the newest scan in the file, and that scan's epoch time."""
    rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8", "replace"))))
    if not rows or list(rows[0]) != cols:
        raise ValueError(f"unexpected columns {list(rows[0]) if rows else None}")
    latest = max(r["updatedAt"] for r in rows)
    ts = int(datetime.fromisoformat(latest.replace("Z", "+00:00")).timestamp())
    return ts, [r for r in rows if r["updatedAt"] == latest and r["itemId"].isdigit()]


def num(s: str) -> int | None:
    return int(s) if s.isdigit() else None


def x1000(s: str) -> int | None:
    try:
        return round(float(s) * 1000)
    except ValueError:
        return None


def seen(db: sqlite3.Connection, name: str) -> bool:
    return db.execute("SELECT 1 FROM files WHERE name=?", (name,)).fetchone() is not None


def save(name: str, raw: bytes) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{name}.csv.gz").write_bytes(gzip.compress(raw))


def load_realm(db: sqlite3.Connection, raw: bytes) -> str:
    ts, rows = parse(raw, REALM_COLS)
    name = f"public-realm-{ts}"
    if seen(db, name):
        return f"realm scan {ts} already loaded"
    save(name, raw)
    # Price snapshots (auctiondb_non_commodity_data) now come from blizzard_collect.py.
    db.executemany("INSERT OR REPLACE INTO auctiondb_non_commodity_scan_stat(scope, ts, item, marketValue) "
                   "VALUES (?,?,?,?)", [(SCOPE, ts, r["itemId"], num(r["marketValue"])) for r in rows])
    db.executemany("INSERT OR REPLACE INTO auctiondb_non_commodity_historical(scope, ts, item, historical) "
                   "VALUES (?,?,?,?)", [(SCOPE, ts, r["itemId"], num(r["historical"])) for r in rows])
    db.execute("INSERT OR REPLACE INTO files VALUES (?,?,?,?)", (name, SCOPE, "PUBLIC_REALM", ts))
    NAMES.write_bytes(raw)  # ingest.py loads item names from here
    return f"realm scan {ts}: {len(rows)} items"


def load_region(db: sqlite3.Connection, raw: bytes) -> str:
    ts, rows = parse(raw, REGION_COLS)
    name = f"public-region-{ts}"
    if seen(db, name):
        return f"region scan {ts} already loaded"
    save(name, raw)
    db.executemany("INSERT OR REPLACE INTO auctiondb_region_sale"
                   "(scope, ts, item, regionSale, regionSoldPerDay, regionSalePercent) VALUES (?,?,?,?,?,?)",
                   [(REGION, ts, r["itemId"], num(r["avgSalePrice"]), x1000(r["soldPerDay"]), x1000(r["saleRate"]))
                    for r in rows])
    db.execute("INSERT OR REPLACE INTO files VALUES (?,?,?,?)", (name, REGION, "PUBLIC_REGION", ts))
    return f"region scan {ts}: {len(rows)} items"


def main() -> None:
    db = connect()
    failed = False
    for path, load in (("realm/pvp-horde/items.csv", load_realm), ("region/items.csv", load_region)):
        try:
            msg = load(db, fetch(path))
        except (OSError, ValueError, sqlite3.Error) as e:  # one feed failing shouldn't stop the other
            msg, failed = f"{path}: {type(e).__name__}: {e}", True
        db.commit()
        print(msg)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
