"""Keep data/catalog/items.json: Blizzard metadata for every item we've seen.

    {id: [name, quality, itemLevel, requiredLevel, class, subclass, slot, vendorSell,
          classId, subclassId, dps, speed, armor, stats]}

speed is seconds; stats is the tooltip lines joined by ", " (e.g. "+18 Strength, +20 Hit").
Rows shorter than ROW_LEN (older format) are refetched.

Covers the items table (TSM's names) plus anything in the newest Blizzard snapshot.
Only missing ids are fetched (static-forever-us item API, 16 at a time), so after
the first run this costs a handful of requests an hour. Used by the AH tab's filters.
"""

from __future__ import annotations

import glob
import gzip
import json
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from blizzard_collect import OUT, token
from ingest import connect

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "data" / "catalog" / "items.json"
ICONS = ROOT / "data" / "catalog" / "icons.json"  # {id: "forever-us/icons/56/133138"}; + .jpg on render.worldofwarcraft.com
MEDIA = "https://us.api.blizzard.com/data/wow/media/item/{}?namespace={}&locale=en_US"
ROW_LEN = 14
ITEM = "https://us.api.blizzard.com/data/wow/item/{}?namespace={}&locale=en_US"
# Forever's static namespace lacks thousands of items its AH lists (e.g. 10057 Duskwoven
# Tunic, Nov 2026); Classic Era has them with the same stats.
NAMESPACES = ("static-forever-us", "static-classic1x-us")


def fetch(tok: str, item: str) -> list | None:
    for ns in NAMESPACES:
        req = urllib.request.Request(ITEM.format(item, ns), headers={"Authorization": f"Bearer {tok}"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                d = json.load(r)
            break
        except urllib.error.HTTPError as e:
            if e.code != 404:
                return None  # retry next run
        except OSError:
            return None
    else:
        return []  # nobody knows it
    cl, sub, pv = d.get("item_class") or {}, d.get("item_subclass") or {}, d.get("preview_item") or {}
    wp = pv.get("weapon") or {}
    stats = [x["display"]["display_string"] for x in pv.get("stats", []) if x.get("display")]
    stats += [x.get("description", "") for x in pv.get("spells", []) if x.get("description")]
    return [d.get("name"), (d.get("quality") or {}).get("type"), d.get("level"), d.get("required_level"),
            cl.get("name"), sub.get("name"), (d.get("inventory_type") or {}).get("name"), d.get("sell_price"),
            cl.get("id"), sub.get("id"), round(wp["dps"]["value"], 1) if wp.get("dps") else None,
            wp["attack_speed"]["value"] / 1000 if wp.get("attack_speed") else None,
            (pv.get("armor") or {}).get("value"), ", ".join(stats) or None]


def icon(tok: str, item: str) -> str | None:
    """'forever-us/icons/56/133138' from https://render.worldofwarcraft.com/forever-us/icons/56/133138.jpg.

    Forever names icons by file id, Classic Era by name, under different paths. '' if nobody has one.
    """
    for ns in NAMESPACES:
        req = urllib.request.Request(MEDIA.format(item, ns), headers={"Authorization": f"Bearer {tok}"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                assets = json.load(r).get("assets", [])
            url = next((a["value"] for a in assets if a.get("key") == "icon"), "")
            return url.split("render.worldofwarcraft.com/", 1)[-1].removesuffix(".jpg")
        except urllib.error.HTTPError as e:
            if e.code != 404:
                return None
        except OSError:
            return None
    return ""


def icons(ids: list[str]) -> None:
    got = json.loads(ICONS.read_text()) if ICONS.exists() else {}
    missing = [i for i in ids if i not in got]
    if missing:
        tok = token()
        with ThreadPoolExecutor(16) as pool:
            for i, name in zip(missing, pool.map(lambda i: icon(tok, i), missing)):
                if name is not None:
                    got[i] = name
        ICONS.write_text(json.dumps(got, separators=(",", ":")))
    print(f"icons: {len(got)} items, fetched {len(missing)}")


def main() -> None:
    cat = json.loads(CATALOG.read_text()) if CATALOG.exists() else {}
    ids = {i for (i,) in connect().execute("SELECT id FROM items")}
    snaps = sorted(glob.glob(str(OUT / "blizzard-113-*.json.gz")))
    for f in snaps[-2:]:  # newest regular + commodities files
        ids |= {str(a["item"]["id"]) for a in json.load(gzip.open(f)).get("auctions", [])}
    missing = sorted((i for i in ids if i not in cat or 0 < len(cat[i]) < ROW_LEN), key=int)
    if missing:
        tok = token()
        with ThreadPoolExecutor(16) as pool:
            for i, row in zip(missing, pool.map(lambda i: fetch(tok, i), missing)):
                if row is not None:
                    cat[i] = row
        CATALOG.write_text(json.dumps(cat, separators=(",", ":")))
    print(f"item catalog: {len(cat)} items, fetched {len(missing)}")
    icons(sorted((i for i, r in cat.items() if r), key=int))


if __name__ == "__main__":
    main()
