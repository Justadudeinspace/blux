# python
import subprocess
import os
from blux.config import Config

class AIEngine:
    """
    Engine for running local LLMs via llama.cpp.
    """

    def __init__(self):
        try:
            self.model_path = self.get_active_model_path()
        except Exception as e:
            print(f"[AI Engine] Warning: {e}")
            self.model_path = None

    def get_active_model_path(self):
        try:
            with open(Config.ACTIVE_MODEL_FILE, "r") as f:
                model_filename = f.read().strip()
            model_path = os.path.join(Config.MODEL_DIR, model_filename)
            if not model_filename or not os.path.isfile(model_path):
                raise FileNotFoundError
            return model_path
        except Exception:
            raise RuntimeError("No active model set. Please run scripts/switch_model.sh.")

    def query(self, prompt):
        """
        Run a prompt through the selected local model.
        """
        if not self.model_path:
            return "[AI Engine] No model configured. Please set up a model first."
        
        try:
            result = subprocess.run(
                ["./models/llama.cpp/main", "-m", self.model_path, "-p", prompt],
                capture_output=True, text=True, timeout=120
            )
            if result.returncode != 0:
                return f"[Model error] {result.stderr}"
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            return "[Timeout] Model took too long to respond."
        except Exception as e:
            return f"[AIEngine Error] {e}"

