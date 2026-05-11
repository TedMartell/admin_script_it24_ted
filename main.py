from functions.log_base_info import write_system_log
from functions.install_software import install_software
from functions.create_user import create_user

def main():
    print("skapa användare")
    #write_system_log()
    #install_software()
    create_user()

if __name__ == "__main__":
    main()