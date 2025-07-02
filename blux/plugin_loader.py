python
import importlib
import os
from blux.config import Config

def load_plugins():
    plugins = []
    plugin_dir = Config.PLUGIN_DIR
    for fname in os.listdir(plugin_dir):
        if fname.endswith(".py") and fname != "__init__.py":
            mod_name = fname[:-3]
            try:
                module = importlib.import_module(f"plugins.{mod_name}")
                for attr in dir(module):
                    obj = getattr(module, attr)
                    if isinstance(obj, type) and hasattr(obj, 'run'):
                        plugins.append(obj())
            except Exception as e:
                print(f"[Plugin Loader] Failed to load {fname}: {e}")
    return plugins

