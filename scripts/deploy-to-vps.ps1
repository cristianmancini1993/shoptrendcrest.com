# Deploy homeshopspot.com to VPS (requires SSH key — run scripts/ssh-one-time-setup.ps1 once)
$ErrorActionPreference = "Stop"
$Root = Split-Path $PSScriptRoot -Parent
$Tar = Join-Path $env:TEMP "hss.tar"
$SshHost = "homeshopspot-vps"
$Docroot = "/var/www/homeshopspot.com"

Write-Host "Building archive from $Root ..."
Push-Location $Root
tar -cf $Tar --exclude=.git --exclude=scripts/__pycache__ .
Pop-Location

Write-Host "Uploading to ${SshHost}:/tmp/hss.tar ..."
scp $Tar "${SshHost}:/tmp/hss.tar"

Write-Host "Extracting on server ..."
$remote = "set -e; cd $Docroot; tar -xf /tmp/hss.tar; grep 'Meta Pixel' index.html | head -1; echo Deploy OK: $Docroot"
ssh $SshHost $remote

Write-Host "Done."
