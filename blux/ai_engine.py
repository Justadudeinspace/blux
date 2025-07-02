python
import requests
import subprocess
import os
import json
from blux.config import Config

class AIEngine:
    def __init__(self, model_path):
        self.model_path = models/llama.cpp/models/ggml-vocab-deepseek-coder.gguf

    def query_deepseek(self, prompt):
        try:
            result = subprocess.run([
                "./models/llama.cpp/main",
                "-m", self.model_path,
                "-p", prompt
            ], capture_output=True, text=True)
            return result.stdout.strip()
        except Exception as e:
            return f"[DeepSeek Error] {e}"

    def detect_mode(self):
        if self.config.OPENROUTER_API_KEY:
            return "online"
        else:
            return "offline"

    def process(self, prompt):
        self.memory.save_interaction(prompt)

        if self.api_mode == "online":
            return self.query_online(prompt)
        else:
            return self.query_offline(prompt)

    def query_online(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.config.OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mistral/mistral-7b-instruct",
            "messages": [{"role": "user", "content": prompt}]
        }
        try:
            res = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                data=json.dumps(data)
            )
            return res.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"API error: {e}"

    def query_offline(self, prompt):
        try:
            result = subprocess.run(
                ["./models/llama.cpp/main", "-p", prompt],
                capture_output=True,
                text=True
            )
            return result.stdout.strip()
        except Exception as e:
            return f"Offline error: {e}"

python
import subprocess
import os

class AIEngine:
    def __init__(self, model_path):
        self.model_path = model_path

    def query_deepseek(self, prompt):
        try:
            result = subprocess.run([
                "./models/llama.cpp/main",
                "-m", self.model_path,
                "-p", prompt
            ], capture_output=True, text=True)
            return result.stdout.strip()
        except Exception as e:
            return f"[DeepSeek Error] {e}"
