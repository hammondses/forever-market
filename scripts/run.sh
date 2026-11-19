#!/bin/bash
# Hourly: pull our auction house from Blizzard, TSM's public realm/region CSVs, refresh item names, alert.
# (tsm_collect.py, the signed-in push collector, is retired: see AGENTS.md.)
set -u
cd "$(dirname "$0")/.."
timeout 300 .venv/bin/python scripts/blizzard_collect.py
.venv/bin/python scripts/item_catalog.py || echo "item catalog failed"
timeout 300 .venv/bin/python scripts/public_collect.py
.venv/bin/python scripts/ingest.py
.venv/bin/python scripts/useful.py >/dev/null
.venv/bin/python scripts/notify.py
scripts/publish.sh || echo "publish failed"
