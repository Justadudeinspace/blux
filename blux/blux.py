# python
from .ai_engine import AIEngine
from .memory import Memory
from .plugin_loader import load_plugins

def main():
    print(open("assets/blue_logo.txt").read())
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



