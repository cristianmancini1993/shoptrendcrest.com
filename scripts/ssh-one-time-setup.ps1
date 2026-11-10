# Run ONCE in PowerShell. You will be asked for the root password (last time).
$pub = Get-Content "$env:USERPROFILE\.ssh\id_ed25519.pub" -Raw
$pub = $pub.Trim()
$cmd = @"
mkdir -p ~/.ssh && chmod 700 ~/.ssh
grep -qF '$pub' ~/.ssh/authorized_keys 2>/dev/null || echo '$pub' >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
echo SSH key installed on `$(hostname)
"@
ssh root@179.198.201.118 $cmd
Write-Host ""
Write-Host "Test (should print OK without password):"
ssh -o BatchMode=yes homeshopspot-vps "echo OK"
