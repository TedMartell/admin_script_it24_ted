function Write-SystemLog {

    # 🔹 Datum & tid
    $dateTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

    # 🔹 Vem kör skriptet
    $scriptUser = $env:USERNAME

    # 🔹 Systeminfo
    $computerName = $env:COMPUTERNAME
    $os = (Get-CimInstance Win32_OperatingSystem).Caption
    $architecture = (Get-CimInstance Win32_OperatingSystem).OSArchitecture

    # 🔹 Hårdvara
    $cpu = (Get-CimInstance Win32_Processor).Name
    $ram = Get-CimInstance Win32_OperatingSystem

    $ramTotal = [math]::Round($ram.TotalVisibleMemorySize / 1MB, 2)
    $ramFree = [math]::Round($ram.FreePhysicalMemory / 1MB, 2)

    # 🔹 Disk
    $disk = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
    $diskTotal = [math]::Round($disk.Size / 1GB, 2)
    $diskFree = [math]::Round($disk.FreeSpace / 1GB, 2)

    # 🔹 Nätverk
    $net = Get-NetIPConfiguration | Where-Object {$_.IPv4Address -ne $null} | Select-Object -First 1
    $ip = $net.IPv4Address.IPAddress

    $mac = (Get-NetAdapter | Where-Object {$_.Status -eq "Up"} | Select-Object -First 1).MacAddress

    # 🔹 Logpath
    $logDir = Join-Path $PSScriptRoot "..\\logs"
    New-Item -ItemType Directory -Force -Path $logDir | Out-Null

    $fileName = "system_$((Get-Date).ToString('yyyy-MM-dd_HH-mm-ss')).txt"
    $logPath = Join-Path $logDir $fileName

    # 🔹 Loggtext
    $logText = @"
===============================
SYSTEM LOG

Date & Time: $dateTime
User: $scriptUser

System:
  Computer Name: $computerName
  OS: $os
  Architecture: $architecture

Hardware:
  CPU: $cpu
  RAM total: $ramTotal MB
  RAM free: $ramFree MB
  Disk total: $diskTotal GB
  Disk free: $diskFree GB

Network:
  IP: $ip
  MAC: $mac
===============================
"@

    $logText | Out-File -FilePath $logPath -Encoding utf8

    Write-Host "Log saved: $logPath"
}