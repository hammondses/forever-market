"""Write the web UI as static files for Cloudflare Pages (forever.miles.games).

Same JSON the live server returns, one file per window and per item on the map.
Run: .venv/bin/python scripts/export_static.py [outdir]   (default data/site)
"""

from __future__ import annotations

import hashlib
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "web"))

from server import PAGE, ah_book, hist_buckets, item_history, item_names, market_map

WINDOWS = ["1", "6", "24", "72", "168", "hist"]

out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data" / "site"
tmp = out.with_name(out.name + ".tmp")
shutil.rmtree(tmp, ignore_errors=True)
(tmp / "data" / "item").mkdir(parents=True)
ids: set[str] = set()
for w in WINDOWS:
    m = market_map(w)
    del m["server"]
    ids.update(r["id"] for r in m["items"])
    (tmp / "data" / f"map-{w}.json").write_text(json.dumps(m))
(tmp / "data" / "ah.json").write_text(json.dumps(ah_book()))
(tmp / "data" / "names.json").write_text(json.dumps(item_names()))
(tmp / "data" / "hist").mkdir()
for n, b in enumerate(hist_buckets()):
    (tmp / "data" / "hist" / f"{n}.json").write_text(json.dumps(b, separators=(",", ":")))
icons = ROOT / "data" / "catalog" / "icons.json"
(tmp / "data" / "icons.json").write_text(icons.read_text() if icons.exists() else "{}")
for i in ids:
    (tmp / "data" / "item" / f"{i}.json").write_text(json.dumps(item_history(i)))
page = PAGE.read_text()
build = hashlib.sha1(page.encode()).hexdigest()[:12]
html = page.replace("<script>", f"<script>window.STATIC = true; window.BUILD = '{build}';</script>\n<script>", 1)
(tmp / "index.html").write_text(html)
# the page polls version.json on focus and swaps in newer prices (or reloads for a new build)
latest = max(json.loads((tmp / "data" / f"map-{w}.json").read_text())["latest"] for w in WINDOWS)
(tmp / "version.json").write_text(json.dumps({"latest": latest, "build": build}))
(tmp / "_headers").write_text("/data/*\n  Cache-Control: public, max-age=300\n"
                              "/version.json\n  Cache-Control: no-store\n")
shutil.rmtree(out, ignore_errors=True)
tmp.rename(out)
print(f"{len(ids)} items -> {out}")
