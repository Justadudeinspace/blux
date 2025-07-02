#!/bin/bash

echo "🚀 Installing BLUX dependencies..."

# Update packages
pkg update -y
pkg upgrade -y

# Install Termux essentials
pkg install -y python git clang ffmpeg cmake termux-api

# Install Python libraries
pip install -r requirements.txt

# Whisper.cpp dependencies
pkg install -y build-essential

# Proot (if using Ollama or local LLMs)
pkg install -y proot-distro

# Create folders
mkdir -p memory models logs

echo "✅ Installation Complete."
