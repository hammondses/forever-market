#!/bin/bash
# Export the web UI as static files and deploy to Cloudflare Pages
# (project forever-market, https://forever.miles.games). Called by run.sh.
set -eu
cd "$(dirname "$0")/.."
"${PY:-.venv/bin/python}" scripts/export_static.py >/dev/null
if [ -z "${CLOUDFLARE_API_TOKEN:-}" ]; then  # CI passes these in; locally read the CF env file
  set -a; . "$HOME/.config/cloudflare/env"; set +a
  export CLOUDFLARE_API_TOKEN="$CF_API_TOKEN" CLOUDFLARE_ACCOUNT_ID="$CF_ACCOUNT_ID"
  export PATH="$HOME/.nvm/versions/node/v22.21.1/bin:$PATH"
fi
cd web  # Pages Functions (functions/api/token.js) deploy from here
timeout 300 wrangler pages deploy ../data/site --project-name forever-market --branch main \
  --commit-dirty=true 2>&1 | grep -E "Deployment complete|ERROR" || true
