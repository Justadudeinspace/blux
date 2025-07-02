import subprocess
from openwakeword.model import Model
from blux.config import Config

class VoiceEngine:
    def __init__(self, ai_engine, memory):
        self.ai_engine = ai_engine
        self.memory = memory
        self.model = Model(wakeword="blux")

    def listen(self):
        print("🎙️ Listening for wake word: 'BLUX'...")

        while True:
            prediction = self.model.predict()

            if prediction:
                print("✅ Wake word detected.")
                self.command_loop()

    def command_loop(self):
        print("🎤 Speak your command...")
        try:
            output = subprocess.check_output(
                [Config.WHISPER_PATH + "main", "-m", "base.en"],
                text=True
            )
            command = output.strip()
            print(f"🗣️ {command}")
            response = self.ai_engine.process(command)
            print(f"💡 {response}")
        except Exception as e:
            print(f"Voice error: {e}")

