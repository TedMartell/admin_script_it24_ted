import os
import datetime
import getpass


def create_user():
    print("=== Create User ===")

    username = input("Ange användarnamn: ")
    password = input("Ange lösenord: ")

    # ✅ Simulering (ingen riktig skapning)
    print(f"\n[SIMULERING] Skapar användare '{username}'...")

    # 🔹 Logga
    log_create_user(username, password)

    print("Användare skapad (simulerat)")

def log_create_user(username, password):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    log_dir = os.path.join(base_dir, "logs")
    os.makedirs(log_dir, exist_ok=True)

    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    file_time = now.strftime("%Y-%m-%d_%H-%M-%S")

    log_path = os.path.join(log_dir, f"user_create_{file_time}.txt")

    admin_user = getpass.getuser()

    log_text = f"""
===============================
CREATE USER LOG

Datum & Tid: {date_time}
Skapad av: {admin_user}

Ny användare:
  Username: {username}
  Password: {password}

===============================

OBS: Lösenord lagras i klartext (inte krypterat).
Detta är ENDAST för utbildningssyfte.
===============================
"""

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(log_text)

    print("Logg sparad:", log_path)
 