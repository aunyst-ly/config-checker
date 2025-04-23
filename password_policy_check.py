import subprocess
from utils.logger import log

def run():
    log("[Password Policy Check]")
    try:
        result = subprocess.check_output("net accounts", shell=True, text=True)
        log(result)
    except Exception as e:
        log(f"Error checking password policy: {e}")
