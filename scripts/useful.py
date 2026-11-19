"""Build the useful(id, per_player, professions) table from the levelling guides.

data/catalog/guides/*.json is {profession: [{guide, materials: [{name, qty, vendor}]}]}.
per_player is the average quantity one player levelling that profession buys
(averaged across that profession's guides), summed across professions.
Vendor-bought materials are skipped.
"""

from __future__ import annotations

import json
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDES = ROOT / "data" / "catalog" / "guides"


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def build(db: sqlite3.Connection) -> list[str]:
    demand: dict[str, dict[str, float]] = {}
    for f in sorted(GUIDES.glob("*.json")):
        for prof, guides in json.loads(f.read_text()).items():
            per: dict[str, float] = {}
            for g in guides:
                for m in g.get("materials", []):
                    if not m.get("vendor") and m.get("name"):
                        per[m["name"]] = per.get(m["name"], 0) + float(m.get("qty") or 0)
            for name, q in per.items():
                demand.setdefault(name, {})[prof] = q / max(1, len(guides))
    byname: dict[str, str] = {}
    for i, n in db.execute("SELECT id, name FROM items WHERE name IS NOT NULL ORDER BY CAST(id AS INTEGER)"):
        byname.setdefault(norm(n), i)
    db.execute("DROP TABLE IF EXISTS useful")
    db.execute("CREATE TABLE useful(id TEXT PRIMARY KEY, per_player REAL, professions TEXT)")
    missing = []
    for name, profs in demand.items():
        i = byname.get(norm(name))
        if i is None:
            missing.append(name)
            continue
        by = ", ".join(f"{p}:{q:.0f}" for p, q in sorted(profs.items(), key=lambda x: -x[1]))
        db.execute("INSERT OR REPLACE INTO useful VALUES (?, ?, ?)", (i, sum(profs.values()), by))
    db.commit()
    return missing


if __name__ == "__main__":
    con = sqlite3.connect(ROOT / "data" / "market.db")
    miss = build(con)
    print(con.execute("SELECT count(*) FROM useful").fetchone()[0], "useful materials;",
          "unmatched:", ", ".join(miss) or "none")
