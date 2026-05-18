function Create-User {
    Write-Host "=== Create User ==="

    # 🔹 Läs in användare
    $username = Read-Host "Enter username"
    $password = Read-Host "Enter password"

    # 🔹 Simulera skapning (ingen riktig user skapas)
    Write-Host "[SIMULATION] Creating user '$username'..."

    # 🔹 Hämta info om vem som kör
    $adminUser = $env:USERNAME
    $dateTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

    # 🔹 Sätt logpath
    $logDir = Join-Path $PSScriptRoot "..\\logs"
    New-Item -ItemType Directory -Force -Path $logDir | Out-Null

    $fileName = "user_create_$((Get-Date).ToString('yyyy-MM-dd_HH-mm-ss')).txt"
    $logPath = Join-Path $logDir $fileName

    # 🔹 Loggtext
    $logText = @"
===============================
CREATE USER LOG

Date & Time: $dateTime
Created by: $adminUser

New User:
  Username: $username
  Password: $password

NOTE:
Password is stored in plain text.
For educational purposes only.
===============================
"@

    # 🔹 Spara logg
    $logText | Out-File -FilePath $logPath -Encoding utf8

    Write-Host "Log saved: $logPath"
}

# Skapa riktig användare
function Create-RealUser {

    Write-Host "=== Create Windows User ==="

    # 🔹 Läs in username
    $username = Read-Host "Enter username"

    # 🔹 Läs in lösenord som SecureString (säkrare input)
    $password = Read-Host "Enter password" -AsSecureString

    try {
        # 🔹 Skapar användaren
        New-LocalUser -Name $username -Password $password -FullName $username -Description "Created via script"

        # 🔹 Lägg till i Users grupp (standard)
        Add-LocalGroupMember -Group "Users" -Member $username

        Write-Host "User '$username' created successfully!" -ForegroundColor Green
    }
    catch {
        Write-Host "Error creating user: $_" -ForegroundColor Red
    }
}