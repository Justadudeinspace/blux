# bash
#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

echo "Updating BLUX..."
git pull origin main
chmod +x scripts/*.sh
echo "Optionally update models? (y/n)"
read -r UPDATE_MODELS
if [[ "$UPDATE_MODELS" =~ ^[Yy]$ ]]; then
    bash scripts/download_deepseek.sh
fi
echo "BLUX is up to date."

