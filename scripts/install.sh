# bash
# !/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

echo "🚀 Welcome to BLUX v2.0 Installer!"
PKGS="python clang git cmake make openblas wget gnupg"
for pkg in $PKGS; do
    if ! command -v $pkg >/dev/null 2>&1; then
        echo "[-] Installing $pkg..."
        pkg install -y $pkg
    fi
done

echo "[*] Installing llama.cpp and Deepseek model..."
bash scripts/install_llama.sh
bash scripts/download_deepseek.sh

echo "[*] Setting up initial model..."
bash scripts/switch_model.sh

echo "[*] Installing Acode IDE..."
bash scripts/install_acode.sh

echo "[*] Theming your Termux environment..."
bash scripts/theme_termux.sh

echo "[*] Installation complete! Run python3 blux/blux.py to start BLUX."

