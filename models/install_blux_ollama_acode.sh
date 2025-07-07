#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Fetching latest BLUX Ollama-Acode installer..."
wget https://github.com/Justadudeinspace/blux/raw/main/forge/installers/blux-ollama-acode/blux-ollama-acode.deb -O blux-ollama-acode.deb
dpkg -i blux-ollama-acode.deb
blux-ollama-acode-install
