# python
import json
import os
from blux.config import Config

class Memory:
    """
    Persistent memory for BLUX.
    """
    def __init__(self):
        self.path = Config.MEMORY_FILE
        self.data = {}
        self.load()

    def load(self):
        try:
            if os.path.exists(self.path):
                with open(self.path, 'r') as f:
                    content = f.read().strip()
                    if content:
                        self.data = json.loads(content)
                    else:
                        self.data = {}
            else:
                self.data = {}
        except json.JSONDecodeError as e:
            print(f"[Memory] Warning: Corrupted memory file, creating new one: {e}")
            self.data = {}
        except Exception as e:
            print(f"[Memory] Error loading memory: {e}")
            self.data = {}

    def save(self):
        try:
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            with open(self.path, 'w') as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"[Memory] Error saving memory: {e}")

    def add_note(self, note):
        self.data.setdefault('notes', []).append(note)
        self.save()

    def get_notes(self):
        return self.data.get('notes', [])

