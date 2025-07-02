python
from blux.terminal_ui import TerminalUI
from blux.ai_engine import AIEngine
from blux.voice_engine import VoiceEngine
from blux.memory import Memory
from blux.automations import Automation
from blux.web_ui import launch_web
import os

def main():
    print("🚀 Launching BLUX...")

    memory = Memory()
    ai_engine = AIEngine(memory)
    terminal = TerminalUI(ai_engine, memory)
    automation = Automation()
    voice = VoiceEngine(ai_engine, memory)

    # For local Deepseek
    engine = AIEngine("models/llama.cpp/models/ggml-vocab-deepseek-coder.gguf")
    response = engine.query_deepseek("Your prompt here")
    print(response)

    # Optional Web UI
    if os.getenv("BLUX_WEB") == "1":
        launch_web(ai_engine, memory)

    # Optional Wake Word Mode
    if os.getenv("BLUX_VOICE") == "1":
        voice.listen()

    # Terminal Mode Default
    terminal.run()

if __name__ == "__main__":
    main()
