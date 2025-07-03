# python
import importlib
import os
import sys
from blux.config import Config

def load_plugins():
    """
    Dynamically loads all plugins in the plugins directory with security checks.
    """
    plugins = []
    plugin_dir = Config.PLUGIN_DIR
    
    if not os.path.exists(plugin_dir):
        print(f"[Plugin Loader] Plugin directory {plugin_dir} does not exist")
        return plugins
    
    # Ensure plugin directory is in sys.path for imports
    if plugin_dir not in sys.path:
        sys.path.insert(0, os.path.dirname(plugin_dir))
        
    for fname in os.listdir(plugin_dir):
        if fname.endswith(".py") and fname != "__init__.py":
            mod_name = fname[:-3]
            
            # Basic filename validation - only allow alphanumeric and underscore
            if not mod_name.replace('_', '').isalnum():
                print(f"[Plugin Loader] Skipping invalid plugin name: {fname}")
                continue
                
            try:
                module = importlib.import_module(f"plugins.{mod_name}")
                for attr in dir(module):
                    obj = getattr(module, attr)
                    if (isinstance(obj, type) and hasattr(obj, 'run') and 
                        obj.__name__ != 'BluxPlugin' and hasattr(obj, 'name')):
                        try:
                            plugin_instance = obj()
                            # Validate plugin has required attributes
                            if hasattr(plugin_instance, 'name') and hasattr(plugin_instance, 'run'):
                                plugins.append(plugin_instance)
                                print(f"[Plugin Loader] Loaded plugin: {plugin_instance.name}")
                        except Exception as e:
                            print(f"[Plugin Loader] Failed to instantiate {obj.__name__}: {e}")
            except Exception as e:
                print(f"[Plugin Loader] Failed to load {fname}: {e}")
    return plugins

