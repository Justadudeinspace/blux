python
class BluxPlugin:
    name = "BasePlugin"
    description = "Base plugin class"
    def run(self, *args, **kwargs):
        raise NotImplementedError("Plugin must implement run()")
plugins/plugin_example.py
python
from plugins import BluxPlugin

class ExamplePlugin(BluxPlugin):
    name = "Example"
    description = "An example plugin."
    def run(self, prompt):
        return f"Plugin response to: {prompt}"

