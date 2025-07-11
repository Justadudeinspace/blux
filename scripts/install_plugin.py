# python
import json
import os
import requests

REGISTRY_PATH = "plugins/registry.json"
PLUGIN_DIR = "plugins"

with open(REGISTRY_PATH) as f:
    registry = json.load(f)

print("Available plugins:")
for idx, plugin in enumerate(registry):
    print(f"{idx+1}: {plugin['name']} - {plugin['description']} (v{plugin['version']})")

choice = int(input("Enter plugin number to install: ")) - 1
plugin = registry[choice]
try:
    r = requests.get(plugin['url'])
    r.raise_for_status()
    with open(f"{PLUGIN_DIR}/{plugin['name']}.py", "w") as f:
        f.write(r.text)
    print(f"{plugin['name']} installed!")
except Exception as e:
    print(f"Failed to install plugin: {e}")

