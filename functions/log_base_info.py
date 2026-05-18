import os
import platform
import socket
import datetime
import psutil
import getpass
import uuid


def write_system_log():
    # 🔹 Sätt loggmapp (parallell med functions/)
    base_dir = os.path.dirname(os.path.dirname(__file__))
    log_dir = os.path.join(base_dir, "logs")
    os.makedirs(log_dir, exist_ok=True)

    # 🔹 Datum & tid
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    date_str = now.strftime("%Y-%m-%d")

    # 🔹 Unikt ID (för flera loggar samma dag)
    unique_id = uuid.uuid4().hex[:6]

    # 🔹 Filnamn
    log_path = os.path.join(log_dir, f"base_info_log_{date_str}_{unique_id}.txt")

    # 🔹 Vem som kör skriptet
    script_user = getpass.getuser()

    # 🔹 Systeminfo
    computer_name = socket.gethostname()
    try:
        user_name = os.getlogin()
    except:
        user_name = script_user  # fallback

    os_name = platform.system() + " " + platform.release()
    architecture = platform.machine()

    # 🔹 Hårdvara
    cpu = platform.processor()

    ram = psutil.virtual_memory()
    ram_total = round(ram.total / (1024**3), 2)
    ram_free = round(ram.available / (1024**3), 2)

    disk = psutil.disk_usage('C:\\')
    disk_total = round(disk.total / (1024**3), 2)
    disk_free = round(disk.free / (1024**3), 2)

    # 🔹 Nätverk (robust version)
    ip_address = None
    mac_address = None

    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET and not addr.address.startswith("127."):
                ip_address = addr.address
            elif addr.family == psutil.AF_LINK:
                mac_address = addr.address

    # 🔹 Loggtext
    log_entry = f"""
===============================
Datum & Tid: {date_time}

Körs av: {script_user}

System:
  Computer Name: {computer_name}
  User: {user_name}
  OS: {os_name}
  Architecture: {architecture}

Hårdvara:
  CPU: {cpu}
  RAM total: {ram_total} GB
  RAM free: {ram_free} GB
  Disk C total: {disk_total} GB
  Disk C free: {disk_free} GB

Nätverk:
  IP-adress: {ip_address}
  MAC-adress: {mac_address}
===============================

"""

    # 🔹 Skriv till fil
    with open(log_path, "w", encoding="utf-8") as file:
        file.write(log_entry)

    print("Logg skapad:", log_path)
