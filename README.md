<p align="center">
  <img src="assets/blux_logo.png" alt="BLUX Logo">
</p>

<h1 align="center">BLUX v2.0 — Terminal AI Developer Forge</h1>

<p align="center">
  <b>"Your Mind. Your Machine. Your Reality."</b>
</p>



---

## 🚀 Description


```
BLUX is a fully autonomous, AI-powered development environment that transforms any Android device into a sovereign coding powerhouse.

- 🧠 Local + API AI Models  
- 🔗 Full Git & GitHub CLI Integration  
- 🎙️ Voice-Controlled AI Terminal  
- 📦 Android-Only — No PC Needed  
```


---


# 🔥 BLUX v2.0 — The Terminal AI Developer Forge 

---

## 🚀 Overview  


```
**BLUX v2.0** is a sovereign, self-sustaining, AI-powered mobile development IDE that runs entirely on Android.  

→ No PC. No subscriptions. No corporate leash.  
→ You wield the power of AI, coding, version control, system automation, and voice interaction — from your phone.

**BLUX fuses:**  
- ✅ Acode IDE (Visual Code Editor)  
- ✅ Termux (Linux shell)  
- ✅ Local LLMs (Llama.cpp, MLC-LLM)  
- ✅ Free AI APIs (OpenRouter, Pawan.kr)  
- ✅ Git + GitHub CLI  
- ✅ Voice AI Interface (Whisper.cpp + Espeak-NG)  
- ✅ Tasker & Android Automation  
```


---

## 🏗️ System Architecture  


```
| Layer               | Stack                                                   |
|---------------------|---------------------------------------------------------|
| 🧠 AI Engine         | Local LLM (MLC-LLM, Llama.cpp) + OpenRouter + Pawan.kr  |
| 💻 IDE Interface     | Acode + Termux Shell                                    |
| 🗄️ Backend Shell      | Termux + Proot + Termux API                            |
| 🎙️ Voice I/O         | Whisper.cpp (STT) + Espeak-NG (TTS) + OpenWakeWord      |
| ☁️ Version Control   | Git + GitHub CLI                                        |
| 🔗 System Automation | Tasker + Termux + Shell Scripts                         |
| 🧠 Persistent Memory | Local JSON + SQLite DB                                  |
```


---

## 📦 Features  


```
- ⚙️ **AI Coding Assistant (Offline/Online)**  
- 🔥 **Terminal-Native AI Chat UI (`rich`, `asciimatics`)**  
- 🎙️ **Voice Command + Wake Word ("Hey BLUX")**  
- ☁️ **Full Git & GitHub Repo Control**  
- 🔗 **File Management + System Control via Termux API**  
- 🚀 **Runs Open Source LLMs Fully Offline**  
- 🧠 **Persistent Memory for Context, Tasks, Notes**  
- 🪐 **Zero PC Dependency — Full Developer Forge on Android**  
```


---

## 📱 Requirements  


```
| App                | Purpose                                  |
|--------------------|------------------------------------------|
| Termux             | Linux shell                             |
| Acode IDE          | Code editor                             |
| Tasker (optional)  | Automation                               |
| Whisper.cpp        | Speech-to-text (offline)                |
| Espeak-NG          | Text-to-speech (offline)                |
| Llama.cpp / MLC-LLM| Local AI inference                      |
| OpenWakeWord       | Wake-word detection (offline)           |
```


---

## 🛠️ Installation  

### 1️⃣ **Termux Setup**  


```
pkg update && pkg upgrade -y
pkg install python git clang cmake ffmpeg espeak-ng termux-api proot proot-distro

2️⃣ Python Environment

pip install rich asciimatics flask fastapi termux SpeechRecognition pyaudio
```

---

# 3️⃣ Install Llama.cpp for Local AI


```
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make
mkdir models
cd models
wget [MODEL_URL]
cd ..

Run Test:

./main -m models/model.gguf -p "Hello BLUX"
```

---

# 4️⃣ Install Whisper.cpp for Speech Recognition


```
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp
make
mkdir models
cd models
wget https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-base.en.bin
cd ..

Run:

./main -m models/ggml-base.en.bin -f audio.wav
```

---

# 5️⃣ Git & GitHub CLI


```
pkg install git gh
gh auth login
```

---

# 6️⃣ Acode IDE Setup

#3 Install from Google Play/F-Droid.


```
Set workspace to:
/data/data/com.termux/files/home/
```


# 📥 BLUX v2.0 Termux Full Installation


```
git clone https://github.com/Justadudeinspace/blux.git
cd blux
bash scripts/install.sh
bash scripts/start_blux.sh
```


---

# 🔥 AI API Integration (Free)


```
API   	        URL	                Models

OpenRouter	https://openrouter.ai	Llama 3, Mixtral, Claude
Pawan.kr	https://pawan.kr	Llama 3, Mistral, Code Llama
```


# 3. Example API Usage:


```
import requests

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
payload = {
  "model": "meta-llama/llama-3-8b-instruct",
  "messages": [{"role": "user", "content": "Generate a Python script to backup files."}]
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

---

# 🔗 Termux-API Control Examples


```
termux-battery-status
termux-sms-send -n "1234567890" "Message from BLUX"
termux-vibrate
termux-toast "BLUX is running"
```

---

# 🌌 Memory System Example


```
{
  "user": "JADIS",
  "wake_word": "BLUX",
  "memory": [
    {"task": "Push to GitHub"},
    {"note": "Check MLC-LLM benchmarks"}
  ]
}
```

---

# 🚀 Automation Ideas


```
- 🔌 Charger plugged → Launch BLUX + Acode

- 📶 Wi-Fi connected → Run Git pull for all repos

- ⏰ Daily backup to cloud/local
```


---

# 🧠 Future Features


```
- 🔥 Avatar GUI (HTML or ASCII)

- 🔥 SSH control to remote devices

- 🔥 Bluetooth + NFC task triggers

- 🔥 Real-time code linting + AI debugging
```


---

# 📜 License

```
- MIT License — Free to modify, share, and evolve.
```

---

# 🧠 Author

#3 🛰️ JADIS (Justadudeinspace)


```
- GitHub: https://github.com/Justadudeinspace

- Developer. Creator. Philosopher.
```


---

# ⚡ Final Words

```
> “You are no longer a user of the system.
You are the system.”
```



---


```
🏗️ BLUX v2.0 Repository Structure

blux/
├── assets/               # Logos, icons, images, banners
│   ├── blux_logo.png
│   ├── blux_logo.svg
│   └── splashscreen.gif
├── blux/                 # Main Python source code (BLUX core engine)
│   ├── __init__.py
│   ├── blux.py           # Main program entry point
│   ├── ai_engine.py      # AI interaction functions (local + API)
│   ├── voice_engine.py   # Speech recognition + TTS
│   ├── memory.py         # Memory management (JSON / SQLite)
│   ├── terminal_ui.py    # Terminal animations, prompts, chat UI
│   ├── automations.py    # Android automation hooks
│   └── config.py         # Configurations, API keys, constants
├── docs/                 # Documentation files
│   ├── README.md         # Main documentation
│   ├── INSTALL.md        # Installation instructions
│   ├── USAGE.md          # User guide + command references
│   └── ARCHITECTURE.md   # Detailed system architecture
├── models/               # Local AI models (Llama.cpp, Whisper, etc.)
│   └── (model files here)
├── scripts/              # Bash install and automation scripts
│   ├── install.sh        # Automatic environment setup
│   ├── start_blux.sh     # Starts BLUX
│   └── update.sh         # Pull latest from Git
├── memory/               # Persistent memory storage
│   └── memory.json
├── requirements.txt      # Python package dependencies
├── LICENSE               # MIT License
├── .gitignore            # Files to ignore in Git
└── README.md             # Repo homepage readme (beautifully formatted)
```

---
