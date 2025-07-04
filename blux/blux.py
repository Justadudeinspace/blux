# python
import os
from .ai_engine import AIEngine
from .memory import Memory
from .plugin_loader import load_plugins
from .config import Config

def main():
    # Secure file path handling to prevent path traversal
    logo_path = os.path.join(Config.BASE_DIR, "..", "assets", "blue_logo.txt")
    logo_path = os.path.abspath(logo_path)
    
    # Validate path is within expected directory
    assets_dir = os.path.abspath(os.path.join(Config.BASE_DIR, "..", "assets"))
    if not logo_path.startswith(assets_dir):
        print("🔮 BLUX v2.0!")  # Fallback if logo file is not accessible
    else:
        try:
            with open(logo_path, 'r', encoding='utf-8') as f:
                print(f.read())
        except (FileNotFoundError, PermissionError, UnicodeDecodeError):
            print("🔮 BLUX v2.0!")  # Fallback if logo file is not accessible
    
    print("Welcome to BLUX v2.0!")
    memory = Memory()
    plugins = load_plugins()
    print(f"Loaded plugins: {[p.name for p in plugins]}")

    engine = AIEngine()
    try:
        prompt = input("Ask BLUX: ")
        print(engine.query(prompt))
        for plugin in plugins:
            print(f"Plugin [{plugin.name}]: {plugin.run(prompt)}")
    except KeyboardInterrupt:
        print("\nExiting BLUX. Goodbye!")

if __name__ == "__main__":
    main()



