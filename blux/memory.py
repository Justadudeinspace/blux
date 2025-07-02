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
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=2)

    def add_note(self, note):
        self.data.setdefault('notes', []).append(note)
        self.save()

    def get_notes(self):
        return self.data.get('notes', [])

