"""Parse data/research/quest-reward-recipes.md (Crafter's Journal Sources.lua + QuestieDB, exported by the owner)
into data/research/quest-recipes.json: {recipeItemId: [{id, name, reqlevel, text, turnins: [{id, name, qty}], prereq, next}]}.
Quantities only live in the objective text, so qty is parsed from it (None when the text doesn't say)."""
import json, re
from pathlib import Path
R = Path(__file__).resolve().parent.parent / "data/research"
NUM = {"a": 1, "an": 1, "one": 1, "some": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
       "nine": 9, "ten": 10, "twelve": 12, "fifteen": 15, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50}

def qty(text, name):
    if not text or not name: return None
    stem = re.escape(name.rstrip("s")[:-1] if name.endswith(("es",)) else name.rstrip("s"))
    m = re.search(r"(\d+|%s)\s+(?:(?:pieces?|vials?|mugs?) of\s+)?%s" % ("|".join(NUM), stem), text, re.I)
    if m: return int(m.group(1)) if m.group(1).isdigit() else NUM[m.group(1).lower()]
    return 1 if re.search(stem, text, re.I) else None

out, cur, q = {}, None, None
for line in (R / "quest-reward-recipes.md").read_text().splitlines():
    if m := re.match(r"- Recipe item ID: (\d+)", line): cur = out.setdefault(m.group(1), [])
    elif m := re.match(r"- \*\*Quest (\d+): (.*?)\*\* \(requires level (\d+)", line):
        q = {"id": int(m.group(1)), "name": m.group(2), "reqlevel": int(m.group(3)), "text": None, "turnins": [], "prereq": [], "next": None}
        cur.append(q)
    elif q is None: continue
    elif m := re.match(r"\s+- Objective text: (.*)", line): q["text"] = m.group(1)
    elif m := re.match(r"\s+- Turn-in item IDs: (.*)", line):
        for t in re.finditer(r"(\d+)(?: \(([^)]*)\))?", m.group(1)):
            q["turnins"].append({"id": int(t.group(1)), "name": t.group(2)})
    elif m := re.match(r"\s+- Prereq quests.*?: \[(.*)\]", line): q["prereq"] = [int(x) for x in re.findall(r"\d+", m.group(1))]
    elif m := re.match(r"\s+- Next in chain: (\d+)", line): q["next"] = int(m.group(1))
for qs in out.values():
    for q in qs:
        for t in q["turnins"]: t["qty"] = qty(q["text"], t["name"])
# turn-in counts the quest data leaves out, from the owner (2026-11-21): Thorium Brotherhood Imperial Plate quests
TH, SR, AQ, RL, CI = (12359, "Thorium Bar"), (7910, "Star Ruby"), (7909, "Aquamarine"), (8170, "Rugged Leather"), (3864, "Citrine")
OVERRIDE = {"12705": [(TH, 40), (SR, 2)], "12715": [(TH, 44), (SR, 2)], "12700": [(TH, 34), (SR, 1), (AQ, 1)],
            "12701": [(TH, 34), (SR, 2)], "12690": [(TH, 20), (SR, 1)], "12688": [(TH, 22), (RL, 6), (AQ, 1)],
            "12687": [(TH, 24), (RL, 6), (CI, 2)]}
for rid, items in OVERRIDE.items():
    for q in out[rid]: q["turnins"] = [{"id": i, "name": n, "qty": k} for (i, n), k in items]
(R / "quest-recipes.json").write_text(json.dumps(out, indent=1))
print(len(out), "recipe items,", sum(map(len, out.values())), "quests")
