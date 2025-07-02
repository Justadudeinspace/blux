#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "Updating BLUX..."
git pull origin main
chmod +x scripts/*.sh
echo "Optionally update models? (y/n)"
read UPDATE_MODELS
if [[ "$UPDATE_MODELS" =~ ^[Yy]$ ]]; then
    bash scripts/download_deepseek.sh
fi
echo "BLUX is up to date."
plugins/registry.json
json
[
  {
    "name": "ExamplePlugin",
    "description": "An example plugin for BLUX.",
    "author": "JADIS",
    "version": "1.0.0",
    "url": "https://raw.githubusercontent.com/Justadudeinspace/blux-plugins/main/ExamplePlugin.py"
  }
]

