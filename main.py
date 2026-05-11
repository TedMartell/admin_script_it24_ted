from functions.log_base_info import write_system_log
from functions.install_software import install_software
from functions.create_user import create_user


def show_menu():
    print("\n=== Admin Tool Menu ===")
    print("1. Create User")
    print("2. Install Software")
    print("3. Log System Information")
    print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            create_user()

        elif choice == "2":
            install_software()

        elif choice == "3":
            write_system_log()

        elif choice == "0":
            print("Exiting program...")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()