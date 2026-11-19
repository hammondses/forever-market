// Cloudflare Pages Function: GET /api/token -> {token, expires}
// Hands the page a Blizzard client-credentials token so the browser can read the
// auction house straight from Blizzard. The client secret stays here (Pages
// secrets BLIZZARD_CLIENT_ID / BLIZZARD_CLIENT_SECRET); the token is read-only
// game data. Cached per isolate and in the edge cache until an hour before expiry.
let cached = null;

export async function onRequestGet({ env }) {
  const now = Date.now();
  if (!cached || cached.expires - now < 3600e3) {
    const edge = caches.default, key = new Request("https://token.internal/blizzard");
    const hit = await edge.match(key);
    cached = hit ? await hit.json() : null;
    if (!cached || cached.expires - now < 3600e3) {
      const r = await fetch("https://oauth.battle.net/token", {
        method: "POST",
        headers: { Authorization: "Basic " + btoa(`${env.BLIZZARD_CLIENT_ID}:${env.BLIZZARD_CLIENT_SECRET}`),
                   "Content-Type": "application/x-www-form-urlencoded" },
        body: "grant_type=client_credentials",
      });
      if (!r.ok) return new Response("token request failed", { status: 502 });
      const d = await r.json();
      cached = { token: d.access_token, expires: now + d.expires_in * 1000 };
      await edge.put(key, new Response(JSON.stringify(cached), { headers: { "Cache-Control": "max-age=3600" } }));
    }
  }
  return Response.json(cached, { headers: { "Cache-Control": "no-store" } });
}
