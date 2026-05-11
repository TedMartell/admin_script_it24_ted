from functions.log_base_info import write_system_log
from functions.install_software import install_software

def main():
    print("Kör install software")
    #write_system_log()
    install_software()

if __name__ == "__main__":
    main()