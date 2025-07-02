# !/data/data/com.termux/files/usr/bin/bash
set -e

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

echo "[*] Installation complete! Run python3 blux/main.py to start BLUX."

