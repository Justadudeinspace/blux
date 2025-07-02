# python
from plugins import BluxPlugin

class ExamplePlugin(BluxPlugin):
    name = "Example"
    description = "An example plugin."
    def run(self, prompt):
        return f"Plugin response to: {prompt}"

