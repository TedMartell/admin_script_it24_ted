function Install-Software {
    Write-Host "=== Install Software ==="
    Write-Host "1. Install via group"
    Write-Host "2. Install individual"

    $choice = Read-Host "Select option"

    # 🔹 Exempeldata (kan senare hämtas från fil)
    $groups = @{
        "group_1" = @("Chrome", "7-Zip")
        "group_2" = @("VS Code", "Git")
    }

    $software = @("Chrome", "VS Code", "7-Zip", "Git")

    if ($choice -eq "1") {
        # Gruppinstallation
        Write-Host "Available groups:"
        $groups.Keys

        $groupChoice = Read-Host "Enter group name"
        $programs = $groups[$groupChoice]

        foreach ($prog in $programs) {
            Write-Host "[SIMULATION] Installing $prog..."
        }

        Log-Install $programs "Group: $groupChoice"
    }

    elseif ($choice -eq "2") {
        # Individuell installation
        Write-Host "Available software:"
        $software

        $progChoice = Read-Host "Enter program"
        Write-Host "[SIMULATION] Installing $progChoice..."

        Log-Install @($progChoice) "Individual"
    }

    else {
        Write-Host "Invalid choice"
    }
}


function Log-Install {
    param (
        [array]$Programs,
        [string]$Method
    )

    $logDir = Join-Path $PSScriptRoot "..\\logs"
    New-Item -ItemType Directory -Force -Path $logDir | Out-Null

    $fileName = "install_$((Get-Date).ToString('yyyy-MM-dd_HH-mm-ss')).txt"
    $logPath = Join-Path $logDir $fileName

    $user = $env:USERNAME
    $dateTime = Get-Date

    $logText = @"
===================
INSTALL LOG

Date: $dateTime
User: $user
Method: $Method

Programs:
$(($Programs -join "`n"))

===================
"@

    $logText | Out-File -FilePath $logPath -Encoding utf8

    Write-Host "Log saved: $logPath"
}
