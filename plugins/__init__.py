# python
class BluxPlugin:
    name = "BasePlugin"
    description = "Base plugin class"
    def run(self, *args, **kwargs):
        raise NotImplementedError("Plugin must implement run()")

