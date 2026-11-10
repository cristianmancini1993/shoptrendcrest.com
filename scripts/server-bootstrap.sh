#!/usr/bin/env bash
# First-time VPS setup for gadgetshifthub.com
# Run as root on a fresh Ubuntu/Debian server:
#   curl -fsSL https://raw.githubusercontent.com/cristianmancini1993/gadgetshifthub.com/main/scripts/server-bootstrap.sh | bash
set -euo pipefail

DOMAIN="gadgetshifthub.com"
REPO_URL="https://github.com/cristianmancini1993/gadgetshifthub.com.git"
REPO_PATH="${DEPLOY_REPO_PATH:-/root/gadgetshifthub.com}"
DOCROOT="${DEPLOY_DOCROOT_PATH:-/var/www/gadgetshifthub.com}"
CERTBOT_EMAIL="${CERTBOT_EMAIL:-info@gadgetshifthub.com}"

echo "==> Installing packages..."
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq nginx certbot python3-certbot-nginx git rsync ufw curl

echo "==> Configuring firewall..."
ufw allow OpenSSH >/dev/null 2>&1 || true
ufw allow 'Nginx Full' >/dev/null 2>&1 || true
ufw --force enable >/dev/null 2>&1 || true

echo "==> Cloning repository..."
if [ -d "${REPO_PATH}/.git" ]; then
  cd "${REPO_PATH}"
  git fetch origin main
  git reset --hard origin/main
else
  git clone "${REPO_URL}" "${REPO_PATH}"
  cd "${REPO_PATH}"
fi
echo "Repo: $(git log -1 --oneline)"

echo "==> Deploying static files to ${DOCROOT}..."
mkdir -p "${DOCROOT}"
export DEPLOY_DOCROOT_PATH="${DOCROOT}"
bash "${REPO_PATH}/scripts/server-deploy.sh"

echo "==> Installing nginx site..."
install -d /etc/nginx/sites-available /etc/nginx/sites-enabled
cp "${REPO_PATH}/scripts/nginx/gadgetshifthub.conf" /etc/nginx/sites-available/gadgetshifthub.com
ln -sf /etc/nginx/sites-available/gadgetshifthub.com /etc/nginx/sites-enabled/gadgetshifthub.com
rm -f /etc/nginx/sites-enabled/default
nginx -t
systemctl enable nginx
systemctl restart nginx

echo "==> Requesting SSL certificate (Let's Encrypt)..."
if certbot --nginx -d "${DOMAIN}" -d "www.${DOMAIN}" \
    --non-interactive --agree-tos -m "${CERTBOT_EMAIL}" --redirect; then
  echo "SSL OK for ${DOMAIN} and www.${DOMAIN}"
else
  echo "WARN: certbot failed — site is live on HTTP only."
  echo "      Point DNS A records to this server IP, then run:"
  echo "      certbot --nginx -d ${DOMAIN} -d www.${DOMAIN}"
fi

echo ""
echo "============================================"
echo " Bootstrap complete!"
echo " Site root: ${DOCROOT}"
echo " Repo:      ${REPO_PATH}"
echo " Update:    cd ${REPO_PATH} && bash scripts/server-deploy.sh"
echo "============================================"
