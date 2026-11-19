"""TSM account tokens for the headless collector.

Sign-in uses the TSM desktop-app OpenID client, as tsm-app-linux does
(vendor/tsm-app-linux/tsm/api/oidc.py). Differences: the loopback listener uses a
fixed port so it can be reached through an SSH tunnel, and the refresh token is
kept in .secrets/tsm_refresh (mode 600) instead of a desktop keyring.
"""

from __future__ import annotations

import asyncio
import base64
import hashlib
import os
import secrets
import sys
from pathlib import Path
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "vendor" / "tsm-app-linux"))

import aiohttp  # noqa: E402
from aiohttp import web  # noqa: E402

from tsm.api import oidc  # noqa: E402

REFRESH_FILE = ROOT / ".secrets" / "tsm_refresh"
LOGIN_PORT = 53682


def save_refresh(token: str) -> None:
    REFRESH_FILE.parent.mkdir(mode=0o700, exist_ok=True)
    tmp = REFRESH_FILE.with_suffix(".tmp")
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        f.write(token)
    os.replace(tmp, REFRESH_FILE)


def load_refresh() -> str:
    if not REFRESH_FILE.exists():
        raise SystemExit("Not signed in to TSM: run scripts/tsm_login.py first (see CLAUDE.md)")
    return REFRESH_FILE.read_text().strip()


class TokenStore:
    """Access tokens refreshed on demand; the rotated refresh token is saved each time."""

    def __init__(self, session: aiohttp.ClientSession) -> None:
        self._session = session
        self.tokens: oidc.Tokens | None = None

    async def access_token(self) -> str:
        if self.tokens is None or self.tokens.needs_refresh():
            prev = self.tokens.refresh_token if self.tokens else load_refresh()
            self.tokens = await oidc.refresh(self._session, prev)
            if self.tokens.refresh_token != prev:
                save_refresh(self.tokens.refresh_token)
        return self.tokens.access_token


async def login(timeout: float = 600) -> None:
    verifier = oidc._b64url(secrets.token_bytes(48))
    challenge = oidc._b64url(hashlib.sha256(verifier.encode()).digest())
    state = oidc._b64url(secrets.token_bytes(16))
    redirect_uri = f"http://localhost:{LOGIN_PORT}{oidc.CALLBACK_PATH}"
    loop = asyncio.get_running_loop()
    result: asyncio.Future[dict[str, str]] = loop.create_future()

    async def callback(request: web.Request) -> web.Response:
        q = dict(request.query)
        if q.get("state") != state:
            return web.Response(status=400, text="State mismatch")
        if not result.done():
            result.set_result(q)
        text = "Signed in. You can close this tab." if "code" in q else "Sign-in failed."
        return web.Response(text=text)

    app = web.Application()
    app.router.add_get(oidc.CALLBACK_PATH, callback)
    runner = web.AppRunner(app, access_log=None)
    await runner.setup()
    await web.TCPSite(runner, "localhost", LOGIN_PORT).start()
    url = f"{oidc.AUTH_BASE}/auth?" + urlencode(
        {
            "client_id": oidc.CLIENT_ID,
            "response_type": "code",
            "response_mode": "query",
            "scope": oidc.SCOPE,
            "redirect_uri": redirect_uri,
            "state": state,
            "code_challenge": challenge,
            "code_challenge_method": "S256",
        }
    )
    print("Open this in the browser that has the SSH tunnel to this box:\n")
    print(url, flush=True)
    try:
        query = await asyncio.wait_for(result, timeout)
        await asyncio.sleep(0.2)
    finally:
        await runner.cleanup()
    if "code" not in query:
        raise SystemExit(f"Login failed: {query.get('error_description') or query.get('error')}")
    async with aiohttp.ClientSession() as session:
        data = await oidc._post_token(
            session,
            {
                "grant_type": "authorization_code",
                "client_id": oidc.CLIENT_ID,
                "code": query["code"],
                "redirect_uri": redirect_uri,
                "code_verifier": verifier,
            },
        )
    tokens = oidc.Tokens.from_response(data)
    save_refresh(tokens.refresh_token)
    print(f"\nSigned in as {tokens.username or tokens.user_id}. Refresh token saved.")


if __name__ == "__main__":
    asyncio.run(login())
