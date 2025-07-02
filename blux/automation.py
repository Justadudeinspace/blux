import os

class Automation:
    def __init__(self):
        pass

    def run_git_push(self):
        os.system("git add . && git commit -m 'BLUX Auto Commit' && git push")

    def nfc_trigger(self):
        os.system("termux-toast 'NFC Triggered' && bash scripts/start_blux.sh")

    def bluetooth_trigger(self):
        os.system("termux-vibrate && bash scripts/start_blux.sh")

