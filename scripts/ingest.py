"""Load data/raw/*.lua.gz AuctionDB strings into data/market.db.

Each file is {downloadTime=N, fields={...}, data={{...},...}} with numbers in
base 32 (0-9A-V). Every tag gets its own table named after it, one row per
(ts, item), columns as the file's fields. regionSoldPerDay and
regionSalePercent are stored as sent (x1000).
"""

from __future__ import annotations

import csv
import gzip
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
DB = ROOT / "data" / "market.db"

NAME = re.compile(r"^(?P<scope>[A-Za-z0-9-]+)__(?P<tag>[A-Z_]+)__(?P<lm>\d+)\.lua\.gz$")
HEAD = re.compile(r'fields=\{([^}]*)\}')
ROW = re.compile(r"\{([^{}]*)\}")


def b32(s: str) -> int:
    return int(s, 32) if s else 0


def connect() -> sqlite3.Connection:
    db = sqlite3.connect(DB)
    db.execute("CREATE TABLE IF NOT EXISTS files(name TEXT PRIMARY KEY, scope TEXT, tag TEXT, ts INTEGER)")
    return db


def ingest_file(db: sqlite3.Connection, path: Path) -> int:
    m = NAME.match(path.name)
    if not m:
        return 0
    text = gzip.decompress(path.read_bytes()).decode("utf-8", "replace")
    ts_m = re.search(r"downloadTime=(\d+)", text)
    head = HEAD.search(text)
    if not ts_m or not head:
        raise ValueError(f"{path.name}: unexpected format")
    ts = int(ts_m.group(1))
    fields = [f.strip().strip('"') for f in head.group(1).split(",")]
    if fields[0] != "itemString" or not all(re.fullmatch(r"[A-Za-z]+", f) for f in fields):
        raise ValueError(f"{path.name}: unexpected fields {fields}")
    table = m["tag"].lower()
    cols = ", ".join(f"{f} INTEGER" for f in fields[1:])
    db.execute(f"CREATE TABLE IF NOT EXISTS {table}(scope TEXT, ts INTEGER, item TEXT, {cols}, "
               "PRIMARY KEY(scope, ts, item))")
    body = text[text.index("data=") :]
    rows = []
    for r in ROW.findall(body):
        parts = r.split(",")
        if len(parts) != len(fields):
            continue
        item = parts[0].strip('"')
        rows.append((m["scope"], ts, item, *(b32(p) for p in parts[1:])))
    marks = ",".join("?" * (len(fields) + 2))
    db.executemany(f"INSERT OR REPLACE INTO {table}(scope, ts, item, {', '.join(fields[1:])}) "
                   f"VALUES ({marks})", rows)
    db.execute("INSERT OR REPLACE INTO files VALUES (?,?,?,?)", (path.name, m["scope"], m["tag"], ts))
    return len(rows)


def load_catalog(db: sqlite3.Connection) -> None:
    """items(id, name, class, vendor): names from the TSM CSV, class and vendor
    price from the BootyBayBroker export in data/catalog/trade_goods_vendor.txt."""
    db.execute("CREATE TABLE IF NOT EXISTS items(id TEXT PRIMARY KEY, name TEXT, class TEXT, vendor INTEGER)")
    cat = ROOT / "data" / "catalog"
    names = cat / "tsm-realm-items.csv"
    if names.exists():
        with names.open(newline="", encoding="utf-8") as f:
            rows = [(r["itemId"], r["name"]) for r in csv.DictReader(f) if r.get("itemId")]
        db.executemany("INSERT INTO items(id, name) VALUES (?, ?) "
                       "ON CONFLICT(id) DO UPDATE SET name=excluded.name", rows)
    vend = cat / "trade_goods_vendor.txt"
    if vend.exists():
        rows = []
        for e in vend.read_text().replace("\n", ";").split(";"):
            parts = e.strip().split(",")
            if len(parts) == 3 and parts[0].isdigit():
                rows.append((parts[0], parts[1], int(parts[2]) if parts[2] else None))
        db.executemany("INSERT INTO items(id, class, vendor) VALUES (?, ?, ?) "
                       "ON CONFLICT(id) DO UPDATE SET class=excluded.class, vendor=excluded.vendor", rows)


def main() -> None:
    db = connect()
    load_catalog(db)
    done = {r[0] for r in db.execute("SELECT name FROM files")}
    for path in sorted(RAW.glob("*.lua.gz")):
        if path.name in done:
            continue
        n = ingest_file(db, path)
        print(f"ingested {path.name}: {n} rows")
    db.commit()


if __name__ == "__main__":
    main()
