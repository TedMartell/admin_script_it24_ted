import os
import datetime
import getpass

#skapar användare
def create_user():
    print("=== Create User ===")

    username = input("Select Username: ")
    password = input("Select Password: ")

    # only simulation
    print(f"\n[simulating] Creating User '{username}'...")

    #Log
    log_create_user(username, password)

    print("User created")

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

Date & Time: {date_time}
Created By: {admin_user}

New User:
  Username: {username}
  Password: {password}

===============================

ATTENTION PASSWORD IS NOT PROTECTED IN ANY WAY!!!
===============================
"""
#sätter infon i loggfilen
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(log_text)

    print("Log saved:", log_path)
 