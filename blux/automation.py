# python
import subprocess
import os
from blux.config import Config

class Automation:
    def __init__(self):
        pass

    def run_git_push(self):
        """
        Sync with git repository safely.
        """
        try:
            # Use subprocess instead of os.system for security
            result = subprocess.run(['git', 'add', '.'], 
                                  capture_output=True, text=True, check=True)
            result = subprocess.run(['git', 'commit', '-m', 'BLUX Auto Commit'], 
                                  capture_output=True, text=True)
            result = subprocess.run(['git', 'push'], 
                                  capture_output=True, text=True, check=True)
            return "Git sync completed successfully"
        except subprocess.CalledProcessError as e:
            return f"Git sync failed: {e.stderr}"
        except Exception as e:
            return f"Git sync error: {e}"

    def nfc_trigger(self):
        """
        Handle NFC trigger safely.
        """
        try:
            # Show notification safely
            subprocess.run(['termux-toast', 'NFC Triggered'], 
                         capture_output=True, text=True, timeout=10)
            # Start BLUX safely
            subprocess.run(['bash', 'scripts/start_blux.sh'], 
                         capture_output=True, text=True, timeout=30)
            return "NFC trigger completed"
        except Exception as e:
            return f"NFC trigger error: {e}"

    def bluetooth_trigger(self):
        """
        Handle Bluetooth trigger safely.
        """
        try:
            # Vibrate safely
            subprocess.run(['termux-vibrate'], 
                         capture_output=True, text=True, timeout=10)
            # Start BLUX safely  
            subprocess.run(['bash', 'scripts/start_blux.sh'], 
                         capture_output=True, text=True, timeout=30)
            return "Bluetooth trigger completed"
        except Exception as e:
            return f"Bluetooth trigger error: {e}"

