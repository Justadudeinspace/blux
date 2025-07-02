python
from blux.ai_engine import AIEngine
from blux.memory import Memory
from blux.plugin_loader import load_plugins

def main():
    print("Welcome to BLUX v2.0!")
    memory = Memory()
    plugins = load_plugins()
    print(f"Loaded plugins: {[p.name for p in plugins]}")

    engine = AIEngine()
    prompt = input("Ask BLUX: ")
    print(engine.query(prompt))

    for plugin in plugins:
        print(f"Plugin [{plugin.name}]: {plugin.run(prompt)}")

if __name__ == "__main__":
    main()

