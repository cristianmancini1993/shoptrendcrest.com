#!/usr/bin/env bash
# Run on the OLD server (72.62.34.234) after SSH key access to NEW server is configured.
# Copies live site + nginx/ssl setup to 179.198.201.118
set -euo pipefail

NEW_HOST="${NEW_HOST:-179.198.201.118}"
NEW_USER="${NEW_USER:-root}"
DOMAIN="gadgetshifthub.com"
SRC="/var/www/gadgetshifthub.com"
REPO_URL="https://github.com/cristianmancini1993/gadgetshifthub.com.git"
REPO_PATH="/root/gadgetshifthub.com"
DOCROOT="/var/www/gadgetshifthub.com"

echo "==> Testing SSH to ${NEW_USER}@${NEW_HOST}..."
ssh -o BatchMode=yes -o ConnectTimeout=15 "${NEW_USER}@${NEW_HOST}" "echo OK"

echo "==> Bootstrapping new server..."
ssh "${NEW_USER}@${NEW_HOST}" bash -s <<'REMOTE'
set -euo pipefail
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq nginx certbot python3-certbot-nginx git rsync ufw curl
ufw allow OpenSSH >/dev/null 2>&1 || true
ufw allow 'Nginx Full' >/dev/null 2>&1 || true
ufw --force enable >/dev/null 2>&1 || true
mkdir -p /var/www/gadgetshifthub.com
REMOTE

echo "==> Syncing site files..."
rsync -az --delete \
  --exclude '.git/' \
  "${SRC}/" "${NEW_USER}@${NEW_HOST}:${DOCROOT}/"

echo "==> Installing nginx config..."
ssh "${NEW_USER}@${NEW_HOST}" bash -s <<REMOTE
set -euo pipefail
if [ ! -d "${REPO_PATH}/.git" ]; then
  git clone "${REPO_URL}" "${REPO_PATH}"
fi
cp "${REPO_PATH}/scripts/nginx/gadgetshifthub.conf" /etc/nginx/sites-available/gadgetshifthub.com
ln -sf /etc/nginx/sites-available/gadgetshifthub.com /etc/nginx/sites-enabled/gadgetshifthub.com
rm -f /etc/nginx/sites-enabled/default
nginx -t
systemctl enable nginx
systemctl restart nginx
REMOTE

echo "==> Requesting SSL certificate on new server..."
ssh "${NEW_USER}@${NEW_HOST}" \
  "certbot --nginx -d ${DOMAIN} -d www.${DOMAIN} --non-interactive --agree-tos -m info@${DOMAIN} --redirect || true"

echo ""
echo "============================================"
echo " Migration complete!"
echo " Update DNS A record: ${DOMAIN} -> ${NEW_HOST}"
echo " Test: curl -I https://${DOMAIN}/hu/nuvia-v17/"
echo "============================================"
