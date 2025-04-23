import subprocess
from utils.logger import log

def run():
    log("[Firewall Check]")
    try:
        result = subprocess.check_output("netsh advfirewall show allprofiles", shell=True, text=True)
        log(result)
    except Exception as e:
        log(f"Error checking firewall: {e}")
