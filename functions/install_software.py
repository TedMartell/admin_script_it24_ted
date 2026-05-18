import json
import os
import datetime
import getpass

def install_software():
    print("=== Install Software ===")
    print("1. Installby group")
    print("2. Install ind. software")
    #Välj alternativ
    choice = input("choice: ")

    if choice == "1":
        install_group()
    elif choice == "2":
        install_individual()
    else:
        print("No Kinder Bueno! ")

#Denna funktion installerar per grupp från JSON filen groups
def install_group():
    with open("data/groups.json", "r", encoding="utf-8") as f:
        groups = json.load(f)

    print("\nAvailable Groups:")
    for i, group in enumerate(groups.keys(), 1):
        print(f"{i}. {group}")

    val = int(input("Choose Group: "))
    group_name = list(groups.keys())[val - 1]
    programs = groups[group_name]

    print(f"\nInstalling Group: {group_name}")

    for program in programs:
        print(f"Installing {program}...")

    log_install(programs, f"Group: {group_name}")


#Installerar individuella program från JSON filen software
def install_individual():
    with open("data/software.json", "r", encoding="utf-8") as f:
        software = json.load(f)["program"]

    print("\nTillgängliga program:")
    for i, prog in enumerate(software, 1):
        print(f"{i}. {prog}")

    val = int(input("Välj program: "))
    program_name = software[val - 1]

    print(f"Installerar {program_name}...")
    
    log_install([program_name], "Individual installation")


#Detta är log-funktionen
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
Install-log
Date: {now}
User: {user}
Method: {method}

Software:
"""

    for p in programs:
        log_text += f"- {p}\n"

    log_text += "===================\n"

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(log_text)

    print("Log Created:", log_path)