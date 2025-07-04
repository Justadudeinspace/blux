# python
import subprocess
import os
import re
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

    def sanitize_prompt(self, prompt):
        """Sanitize user input for safe subprocess execution"""
        if not isinstance(prompt, str):
            raise ValueError("Prompt must be a string")
        
        # Length limit
        if len(prompt) > 2048:
            raise ValueError("Prompt too long (max 2048 characters)")
        
        # Remove potential command injection patterns first
        dangerous_patterns = [
            r'[;&|`$(){}[\]<>]',  # Shell metacharacters
            r'\\[nrtbfav]',       # Escape sequences
            r'\.\.',              # Directory traversal
            r'/[a-zA-Z]',         # Absolute paths starting with /
            r'rm\s+',             # rm commands
            r'sudo\s+',           # sudo commands
            r'exec\s*\(',         # exec function calls
        ]
        
        for pattern in dangerous_patterns:
            if re.search(pattern, prompt):
                raise ValueError("Prompt contains potentially dangerous content")
        
        # Allow only safe characters after dangerous pattern check
        # Allow alphanumeric, spaces, basic punctuation
        safe_chars = re.compile(r'^[a-zA-Z0-9\s\.\,\?\!\-\'\"\:]+$')
        if not safe_chars.match(prompt):
            raise ValueError("Prompt contains invalid characters")
        
        return prompt.strip()

    def query(self, prompt):
        """
        Run a prompt through the selected local model.
        """
        if not self.model_path:
            return "[AI Engine] No model configured. Please set up a model first."
        
        try:
            # Sanitize input
            safe_prompt = self.sanitize_prompt(prompt)
            
            # Validate model path exists and is safe
            if not os.path.isfile(self.model_path):
                return "[AI Engine] Model file not found."
            
            # Use absolute path for executable
            executable = os.path.abspath(os.path.join(Config.BASE_DIR, "..", "models", "llama.cpp", "main"))
            if not os.path.isfile(executable):
                return "[AI Engine] LLaMA executable not found."
            
            # Use absolute paths and validated arguments
            result = subprocess.run(
                [executable, "-m", self.model_path, "-p", safe_prompt],
                capture_output=True, 
                text=True, 
                timeout=120,
                cwd=os.path.dirname(executable)  # Set working directory
            )
            
            if result.returncode != 0:
                return f"[Model error] Process failed with code {result.returncode}"
            return result.stdout.strip()
            
        except ValueError as e:
            return f"[Input Error] {e}"
        except subprocess.TimeoutExpired:
            return "[Timeout] Model took too long to respond."
        except Exception as e:
            return f"[AIEngine Error] Unexpected error occurred"

