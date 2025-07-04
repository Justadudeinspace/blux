# python
import importlib
import os
import sys
import re
from blux.config import Config

def validate_plugin_file(plugin_path):
    """Basic validation of plugin file before loading"""
    # Check file size (max 1MB)
    if os.path.getsize(plugin_path) > 1024 * 1024:
        raise ValueError("Plugin file too large")
    
    # Basic static analysis for dangerous patterns
    with open(plugin_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for dangerous patterns
    dangerous_patterns = [
        r'__import__\s*\(',
        r'eval\s*\(',
        r'exec\s*\(',
        r'compile\s*\(',
        r'os\.system',
        r'os\.popen',
    ]
    
    for pattern in dangerous_patterns:
        if re.search(pattern, content):
            raise ValueError(f"Plugin contains dangerous pattern: {pattern}")
    
    return True

def verify_plugin_path(plugin_path):
    """Verify plugin is in trusted directory"""
    trusted_dir = os.path.abspath(Config.PLUGIN_DIR)
    plugin_abs = os.path.abspath(plugin_path)
    
    if not plugin_abs.startswith(trusted_dir):
        raise ValueError("Plugin not in trusted directory")
    
    return True

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
            plugin_path = os.path.join(plugin_dir, fname)
            mod_name = fname[:-3]
            
            # Enhanced filename validation
            if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', mod_name):
                print(f"[Plugin Loader] Skipping invalid plugin name: {fname}")
                continue
                
            try:
                # Security validations
                verify_plugin_path(plugin_path)
                validate_plugin_file(plugin_path)
                
                module = importlib.import_module(f"plugins.{mod_name}")
                for attr in dir(module):
                    obj = getattr(module, attr)
                    if (isinstance(obj, type) and hasattr(obj, 'run') and 
                        obj.__name__ != 'BluxPlugin' and hasattr(obj, 'name')):
                        try:
                            plugin_instance = obj()
                            # Validate plugin has required attributes
                            if (hasattr(plugin_instance, 'name') and 
                                hasattr(plugin_instance, 'run') and
                                isinstance(plugin_instance.name, str)):
                                plugins.append(plugin_instance)
                                print(f"[Plugin Loader] Loaded plugin: {plugin_instance.name}")
                        except Exception as e:
                            print(f"[Plugin Loader] Failed to instantiate {obj.__name__}: {e}")
            except Exception as e:
                print(f"[Plugin Loader] Security check failed for {fname}: {e}")
    return plugins

