# Deploy the same static tree to all 7 production domain docroots (two VPS hosts).
# Usage: powershell -ExecutionPolicy Bypass -File .\scripts\deploy-multi-domain-vps.ps1

$ErrorActionPreference = "Stop"
$Root = Split-Path $PSScriptRoot -Parent
$Tar = Join-Path $env:TEMP "hss-multidomain.tar"

$Host216 = "root@179.198.216.71"
$Host118 = "root@179.198.201.118"

$Domains216 = @(
    "gadgetshifthub.com",
    "hubaurashop.com",
    "shopterva.com",
    "shoptrendcrest.com",
    "devicegridbay.com",
    "hometrendlivora.com"
)

Write-Host "Building archive from $Root ..."
Push-Location $Root
tar -cf $Tar --exclude=.git --exclude=scripts/__pycache__ .
Pop-Location

Write-Host "Uploading to ${Host216}:/tmp/hss-multidomain.tar ..."
scp $Tar "${Host216}:/tmp/hss-multidomain.tar"

foreach ($d in $Domains216) {
    $remote = "cd /var/www/$d && tar -xf /tmp/hss-multidomain.tar && grep -q 'Meta Pixel' index.html && echo OK:$d"
    Write-Host "Extracting -> $d ..."
    ssh $Host216 $remote
}

Write-Host "Uploading to ${Host118}:/tmp/hss-multidomain.tar ..."
scp $Tar "${Host118}:/tmp/hss-multidomain.tar"

$remote118 = "cd /var/www/shoproomdock.com && tar -xf /tmp/hss-multidomain.tar && grep -q 'Meta Pixel' index.html && echo OK:shoproomdock.com"
Write-Host "Extracting -> shoproomdock.com ..."
ssh $Host118 $remote118

Write-Host "Done."
