import json
import os
import datetime
import getpass

def install_software():
    print("=== Install Software ===")
    print("1. Installera via grupp")
    print("2. Installera individuellt")

    choice = input("Val: ")

    if choice == "1":
        install_group()
    elif choice == "2":
        install_individual()
    else:
        print("Ogiltigt val")


def install_group():
    with open("data/groups.json", "r", encoding="utf-8") as f:
        groups = json.load(f)

    print("\nTillgängliga grupper:")
    for i, group in enumerate(groups.keys(), 1):
        print(f"{i}. {group}")

    val = int(input("Välj grupp: "))
    group_name = list(groups.keys())[val - 1]
    programs = groups[group_name]

    print(f"\nInstallerar grupp: {group_name}")

    for program in programs:
        print(f"Installerar {program}...")

    log_install(programs, f"Grupp: {group_name}")

def install_individual():
    with open("data/software.json", "r", encoding="utf-8") as f:
        software = json.load(f)["program"]

    print("\nTillgängliga program:")
    for i, prog in enumerate(software, 1):
        print(f"{i}. {prog}")

    val = int(input("Välj program: "))
    program_name = software[val - 1]

    print(f"Installerar {program_name}...")
    
    log_install([program_name], "Individuell installation")

def log_install(programs, method):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    log_dir = os.path.join(base_dir, "logs")
    os.makedirs(log_dir, exist_ok=True)

    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d_%H-%M-%S")

    log_path = os.path.join(log_dir, f"install_{date_str}.txt")

    user = getpass.getuser()

    log_text = f"""
===================
Installationslogg
Datum: {now}
Användare: {user}
Metod: {method}

Program:
"""

    for p in programs:
        log_text += f"- {p}\n"

    log_text += "===================\n"

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(log_text)

    print("Logg sparad:", log_path)