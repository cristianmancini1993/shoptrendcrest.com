#!/usr/bin/env bash
# Run on the server after CI uploads site files or after git pull.
set -eu

REPO="${DEPLOY_REPO_PATH:-/var/www/shoptrendcrest.com}"
DOCROOT="${DEPLOY_DOCROOT_PATH:-}"

cd "${REPO}"
if [ -d .git ]; then
  git fetch origin main
  git reset --hard origin/main
  echo "Pulled: $(git log -1 --oneline)"
else
  echo "Skip git pull (no .git in ${REPO})"
fi

if [ -z "${DOCROOT}" ]; then
  LIVE_PAGE="$(find /var/www /home -type f -path '*/pt/miorvella/landing.html' 2>/dev/null | head -1 || true)"
  if [ -n "${LIVE_PAGE}" ]; then
    DOCROOT="$(dirname "$(dirname "$(dirname "${LIVE_PAGE}")")")"
  fi
fi

if [ -z "${DOCROOT}" ]; then
  for candidate in \
    /home/*/domains/shoptrendcrest.com/public_html \
    /home/*/shoptrendcrest.com/public_html \
    /var/www/shoptrendcrest.com \
    /home/*/public_html; do
    for d in ${candidate}; do
      if [ -d "${d}" ] && [ -f "${d}/index.html" ]; then
        DOCROOT="${d}"
        break 2
      fi
    done
  done
fi

if [ -n "${DOCROOT}" ] && [ "${DOCROOT}" != "${REPO}" ]; then
  rsync -a \
    --exclude '.git/' \
    --exclude 'scripts/__pycache__/' \
    "${REPO}/" "${DOCROOT}/"
  echo "Synced to ${DOCROOT}"
  LIVE_ROOT="${DOCROOT}"
else
  LIVE_ROOT="${REPO}"
fi

test -f "${LIVE_ROOT}/index.html"
test -f "${LIVE_ROOT}/pt/miorvella-3039/landing.html"
test -f "${LIVE_ROOT}/it/warmio-3990/index.html"
test -f "${LIVE_ROOT}/de/warmio-2285/thank-you/index.html"
echo "Deploy OK — live at ${LIVE_ROOT}/index.html"
