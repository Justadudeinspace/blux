<p align="center">
  <img src="assets/blux_logo.png" alt="BLUX Logo">
</p>

<h1 align="center">BLUX v2.0 — Terminal AI Developer Forge</h1>

<p align="center">
  <b>"Your Mind. Your Machine. Your Reality."</b>
</p>

---

# ⚡️ BLUX v2.0 – The Sovereign Android AI Forge ⚡️

> **Create. Innovate. Never Destroy.**
>
> By JADIS

---

## 🔥 What is BLUX v2.0?
BLUX v2.0 is a fully offline, AI-powered, terminal-based development forge for Android.  
No PC. No subscriptions. No limits.  
Harness the power of local LLMs, voice, automation, and scripting—right on your device.

---

## 🚀 Features

- **100% Offline AI** (DeepSeek, Phi-2, TinyLlama, etc.)
- **Model Switcher:** Swap between installed models instantly
- **Model Benchmarking:** Test speed and memory usage on your device
- **Plugin System:** Drop in new AI/automation modules
- **Plugin Marketplace:** Discover and install plugins from a community registry
- **Voice Control:** Full offline speech-to-text and TTS (coming soon)
- **Automation:** Termux, Tasker, and system scripting
- **Author Authenticity:** All releases GPG-signed by JADIS

---

## ⚠️ Responsible Use Statement

BLUX is a tool for creation and innovation.  
**It is NOT intended for malicious use. I do not support hacking, destruction, or harm.**  
I am not responsible for how others use this tool.  
Use BLUX to build, learn, and push boundaries—never to destroy.

---

## 📦 Installation

1. **Install Termux** (Android 10+)
2. **Clone this repo:**
git clone https://github.com/Justadudeinspace/blux
cd blux

3. **Run the installer:**
bash scripts/install.sh

4. **Set your Hugging Face token (for model downloads):**
export HF_TOKEN=your_huggingface_token

5. **Switch models anytime:**
bash scripts/switch_model.sh

---

## 🧪 Benchmark Models

Test all installed models for speed and memory usage:
bash scripts/benchmark_models.sh

---

## 🔌 Plugin Marketplace

Discover and install plugins:
python scripts/install_plugin.py

- Browse available plugins in `plugins/registry.json`
- Install new plugins instantly

---

## 🔑 Author Authenticity

All official BLUX releases are signed with my GPG key.  
To verify:
gpg --import blux_author_pubkey.asc
gpg --verify blux_v2_xda_ready.sig blux_v2_xda_ready.zip

---

## 🛠️ Troubleshooting

- **Model not found:** Run `bash scripts/switch_model.sh` and select a valid model.
- **Model download fails:** Ensure your Hugging Face token is set and valid.
- **Plugin not loading:** Check for syntax errors or missing dependencies in the plugin file.
- **Update BLUX:** Run `bash scripts/update.sh`

---

## 💬 Final Words

BLUX v2.0 is for the visionaries, the outc asts, and the creators who refuse to accept “impossible.”  
Let’s build the future—one line of code at a time.

— **JADIS**
