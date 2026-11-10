# Deploy gadgetshifthub.com to 179.198.201.118 (run from Windows after SSH key is added)
$ErrorActionPreference = "Stop"
$HostAlias = "gadgetshifthub-vps"
$RepoRoot = Split-Path $PSScriptRoot -Parent
$Tarball = Join-Path $env:TEMP "gadgetshifthub.tgz"

Write-Host "==> Testing SSH to $HostAlias..."
ssh -o BatchMode=yes $HostAlias "echo OK"

Write-Host "==> Creating tarball..."
Push-Location $RepoRoot
tar --exclude=".git" -czf $Tarball .
Pop-Location

Write-Host "==> Uploading site..."
scp $Tarball "${HostAlias}:/tmp/gadgetshifthub.tgz"

Write-Host "==> Bootstrapping server..."
ssh $HostAlias @'
set -euo pipefail
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq nginx certbot python3-certbot-nginx git rsync ufw curl
ufw allow OpenSSH >/dev/null 2>&1 || true
ufw allow "Nginx Full" >/dev/null 2>&1 || true
ufw --force enable >/dev/null 2>&1 || true
mkdir -p /var/www/gadgetshifthub.com
tar -xzf /tmp/gadgetshifthub.tgz -C /var/www/gadgetshifthub.com
rm -f /tmp/gadgetshifthub.tgz
cat > /etc/nginx/sites-available/gadgetshifthub.com <<'NGINX'
server {
    listen 80;
    listen [::]:80;
    server_name gadgetshifthub.com www.gadgetshifthub.com;
    root /var/www/gadgetshifthub.com;
    index index.html;
    location / { try_files $uri $uri/ $uri/index.html =404; }
}
NGINX
ln -sf /etc/nginx/sites-available/gadgetshifthub.com /etc/nginx/sites-enabled/gadgetshifthub.com
rm -f /etc/nginx/sites-enabled/default
nginx -t
systemctl enable nginx
systemctl restart nginx
certbot --nginx -d gadgetshifthub.com -d www.gadgetshifthub.com --non-interactive --agree-tos -m info@gadgetshifthub.com --redirect || true
echo "Deploy OK"
'@

Write-Host "Done. Point DNS A record gadgetshifthub.com -> 179.198.201.118"
