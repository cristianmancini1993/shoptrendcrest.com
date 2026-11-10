#!/usr/bin/env bash
# Deploy from your Mac when GitHub Actions SSH key is on the server.
set -eu
SSH_HOST="${DEPLOY_SSH_HOST:-shoptrendcrest}"
REPO="${DEPLOY_REPO_PATH:-/var/www/shoptrendcrest.com}"
ssh "${SSH_HOST}" "cd '${REPO}' && git fetch origin main && git reset --hard origin/main && bash scripts/server-deploy.sh"
echo "Done. Check: https://shoptrendcrest.com/it/forvex-4363/"
