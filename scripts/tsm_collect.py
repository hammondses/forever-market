"""Hourly TSM collector: grab the AuctionDB strings TSM pushes for followed realms.

Connects to the same push socket as the TSM desktop app, waits for the
realm_auctiondb / region_auctiondb events, downloads each data string it has not
stored yet and saves it gzipped under data/raw/. ingest.py turns them into rows.

    tsm_collect.py               collect (cron)
    tsm_collect.py --realms      list followed realms and Forever realm ids
    tsm_collect.py --follow ID HORDE|ALLIANCE|ALL
"""

from __future__ import annotations

import argparse
import asyncio
import gzip
import json
import re
import sys
import time
from pathlib import Path

import tsmauth  # sets sys.path for the vendored client

from tsm.api.client import TSMApiClient  # noqa: E402
from tsm.api.socket import TSMSocket as SocketClient  # noqa: E402

ROOT = tsmauth.ROOT
RAW = ROOT / "data" / "raw"
WANTED = ("realm_auctiondb", "region_auctiondb")
QUIET_SECONDS = 20  # stop after this long without a new event
MAX_SECONDS = 120


def _safe(s: object) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", str(s))


async def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--realms", action="store_true")
    ap.add_argument("--follow", nargs=2, metavar=("REALM_ID", "AH_TYPE"))
    args = ap.parse_args()

    client = TSMApiClient(user_agent="wow-market")
    session = await client.session()
    store = tsmauth.TokenStore(session)
    client.set_token_provider(store.access_token)
    await store.access_token()
    assert store.tokens is not None
    user_id = store.tokens.user_id
    try:
        if args.follow:
            await client.add_user_realm(user_id, int(args.follow[0]), args.follow[1].upper())
            print("followed")
            return
        if args.realms:
            await list_realms(client, user_id)
            return
        await collect(client, store)
    finally:
        await client.close()


async def list_realms(client: TSMApiClient, user_id: str) -> None:
    regions = {r["regionId"]: r for r in await client.regions()}
    followed = await client.user_realms(user_id)
    print("Followed:", json.dumps(followed, default=str))
    for realm in await client.realms():
        region = realm.get("region") or regions.get(realm.get("regionId"), {})
        if "forever" not in str(region.get("gameVersion", "")).lower():
            continue
        houses = [(a.get("auctionHouseId"), a.get("type")) for a in realm.get("auctionHouses") or []]
        print(realm.get("realmId"), region.get("regionPrefix"), realm.get("localizedName"), houses)


async def collect(client: TSMApiClient, store: tsmauth.TokenStore) -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    events: list[tuple[str, dict]] = []
    last = time.monotonic()

    async def on_event(name: str, payload: object) -> None:
        nonlocal last
        if name in WANTED and isinstance(payload, dict):
            events.append((name, payload))
            last = time.monotonic()

    sock = SocketClient(client.session, store.access_token, on_event)
    sock.start()
    start = time.monotonic()
    try:
        while time.monotonic() - start < MAX_SECONDS:
            await asyncio.sleep(1)
            if events and time.monotonic() - last > QUIET_SECONDS:
                break
    finally:
        await sock.stop()

    saved = 0
    for name, p in events:
        tag, lm, url = p.get("stringType"), p.get("lastModified"), p.get("url")
        if not tag or not lm or not isinstance(url, str):
            continue
        scope = f"realm{p.get('realmId')}-{p.get('auctionHouseType')}" if name.startswith("realm") \
            else f"region{p.get('regionId')}"
        out = RAW / f"{_safe(scope)}__{_safe(tag)}__{int(lm)}.lua.gz"
        if out.exists():
            continue
        raw = await client.download(url)
        if raw is None:
            continue
        tmp = out.with_suffix(".tmp")
        tmp.write_bytes(gzip.compress(raw))
        tmp.replace(out)
        saved += 1
    kinds = sorted({f"{n}:{p.get('stringType')}" for n, p in events})
    print(f"{time.strftime('%F %T')} events={len(events)} new_files={saved} {kinds}")


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
