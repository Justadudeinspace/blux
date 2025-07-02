import json
import os

class Memory:
    def __init__(self):
        self.file = "./memory/memory.json"
        if not os.path.exists(self.file):
            with open(self.file, 'w') as f:
                json.dump({"notes": [], "tasks": [], "history": []}, f)
        self.data = self.load()

    def load(self):
        with open(self.file, 'r') as f:
            return json.load(f)

    def save(self):
        with open(self.file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def save_interaction(self, prompt):
        self.data['history'].append(prompt)
        self.save()

    def add_note(self, note):
        self.data['notes'].append(note)
        self.save()

    def get_notes(self):
        return self.data['notes']

    def clear_notes(self):
        self.data['notes'] = []
        self.save()

