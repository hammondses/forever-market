#!/usr/bin/env python3
"""Turn the Crafter's Journal addon export (data/research/crafters-journal.md) into data/research/recipes.json.

One entry per crafting spell: profession, product, reagents, how the recipe is learned (trainer fee, or a
recipe item and its vendor price), Merchant's Favor cost, and whether the product binds on pickup.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "research" / "crafters-journal.md"
OUT = ROOT / "data" / "research" / "recipes.json"

pairs = lambda s: [[int(a), int(b)] for a, b in re.findall(r"\{\s*(\d+),\s*(\d+)\s*\}", s)]


def field(body: str, key: str):
    m = re.search(rf"\b{key} = (\"(?:[^\"\\\\]|\\\\.)*\"|true|-?\d+)", body)
    if not m:
        return None
    v = m.group(1)
    return True if v == "true" else json.loads(v) if v.startswith('"') else int(v)


recipes, vendor, names, prof = [], {}, {}, None
for line in SRC.read_text().splitlines():
    if m := re.match(r"^## (\w+)", line):
        prof = m.group(1).lower().replace("firstaid", "first aid")
    elif m := re.match(r"^\s*\[(\d+)\] = \{ (name = .*) \},?$", line):
        body = m.group(2)
        r = re.search(r"\br = \{(.*?)\}\s*\},", body + ",")
        out = re.search(r"\bout = \{ (\d+), (\d+) \}", body)
        rep = re.search(r"\brep = \{ (\d+), (\d+) \}", body)
        recipes.append({
            "spell": int(m.group(1)), "profession": prof, "name": field(body, "name"),
            "train": field(body, "train"), "fee": field(body, "fee"), "scroll": field(body, "scroll"),
            "scrollPrice": field(body, "scrollPrice"), "favor": field(body, "favor"), "favorRep": field(body, "favorRep"),
            "faction": field(body, "faction"), "bop": bool(field(body, "bop")), "basic": bool(field(body, "basic")),
            "rep": [int(rep.group(1)), int(rep.group(2))] if rep else None,
            "reagents": pairs(r.group(1) + "}") if r else [],
            "out": [int(out.group(1)), int(out.group(2))] if out else None,
        })
    elif m := re.match(r'^ES\.Data\.ItemNames\[(\d+)\] = (".*")', line):
        names[m.group(1)] = json.loads(m.group(2))
    elif m := re.match(r"^ES\.Data\.VendorPrices\[(\d+)\] = (\d+)", line):
        vendor[m.group(1)] = int(m.group(2))

OUT.write_text(json.dumps({"source": "Crafter's Journal addon Data/*.lua (Forever client DB2)", "recipes": recipes,
                           "vendorPrices": vendor, "names": names}, separators=(",", ":")))
print(len(recipes), "recipes,", len(vendor), "vendor prices,", len(names), "names")
