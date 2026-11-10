#!/usr/bin/env bash
# Add deploy SSH public key — run once on the server as root (password login OK).
set -euo pipefail

KEYS=(
  "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFxpbs9xC1O83QnB2B/snFpFWv13DPeTowYvRvqsjRPj cursor-shoptrendcrest-deploy"
  "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJitAs9zA8BkKW+Xa6rQLbnINC1X3e0HseiIYQtPMIu0 server-72.62.34.234"
)

mkdir -p ~/.ssh
chmod 700 ~/.ssh
touch ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

for DEPLOY_PUBKEY in "${KEYS[@]}"; do
  if grep -qF "${DEPLOY_PUBKEY}" ~/.ssh/authorized_keys 2>/dev/null; then
    echo "Already installed: ${DEPLOY_PUBKEY%% *}"
  else
    echo "${DEPLOY_PUBKEY}" >> ~/.ssh/authorized_keys
    echo "Added: ${DEPLOY_PUBKEY%% *}"
  fi
done
