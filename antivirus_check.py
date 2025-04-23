import subprocess
from utils.logger import log

def run():
    log("[Antivirus Check]")
    try:
        result = subprocess.check_output(
            'wmic /namespace:\\\\root\\SecurityCenter2 path AntiVirusProduct get displayName,productState',
            shell=True,
            text=True
        )
        log(result)
    except Exception as e:
        log(f"Error checking antivirus status: {e}")
