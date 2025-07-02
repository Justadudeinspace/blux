# 🧠 BLUX System Architecture

## 🔥 Components:
- AI Engine → Online (OpenRouter) / Offline (LLM)
- Voice Engine → Wake Word + Whisper.cpp
- Terminal UI → Rich CLI with memory integration
- Web UI → Flask dashboard at localhost:5000
- Memory → JSON or SQLite
- Automations → NFC/BT hooks, Git sync

## 🔗 Data Flow:
User → Voice/Terminal/Web → AI Engine → Memory/Output

## 🎯 Offline Models:
- llama.cpp → Local LLM
- whisper.cpp → Local STT
- openwakeword → Local wake word detection

## 🔥 Automation Hooks:
- NFC tags
- Bluetooth proximity
- Git automation

## ⚙️ Folder Structure:
- /blux → Python core
- /scripts → Install/Start/Update
- /docs → Manuals
- /assets → Logos, splash
- /memory → Persistent data
- /models → LLM + whisper

