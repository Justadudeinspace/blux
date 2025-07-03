# python
import importlib
import os
from blux.config import Config

def load_plugins():
    """
    Dynamically loads all plugins in the plugins directory.
    """
    plugins = []
    plugin_dir = Config.PLUGIN_DIR
    
    if not os.path.exists(plugin_dir):
        print(f"[Plugin Loader] Plugin directory {plugin_dir} does not exist")
        return plugins
        
    for fname in os.listdir(plugin_dir):
        if fname.endswith(".py") and fname != "__init__.py":
            mod_name = fname[:-3]
            try:
                module = importlib.import_module(f"plugins.{mod_name}")
                for attr in dir(module):
                    obj = getattr(module, attr)
                    if (isinstance(obj, type) and hasattr(obj, 'run') and 
                        obj.__name__ != 'BluxPlugin' and hasattr(obj, 'name')):
                        try:
                            plugin_instance = obj()
                            plugins.append(plugin_instance)
                        except Exception as e:
                            print(f"[Plugin Loader] Failed to instantiate {obj.__name__}: {e}")
            except Exception as e:
                print(f"[Plugin Loader] Failed to load {fname}: {e}")
    return plugins

