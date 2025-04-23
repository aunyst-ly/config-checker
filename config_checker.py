
from config_checks import firewall_check, password_policy_check, antivirus_check
from utils.logger import log

def main():
    log("Starting configuration checks...\n")

    firewall_check.run()
    password_policy_check.run()
    antivirus_check.run()

    log("\nConfiguration checks completed.")

if __name__ == "__main__":
    main()
