# BLUX Ollama-Acode Integration Installer

This installer provides full integration between [Ollama](https://ollama.com) and Acode GPT Plugin in the Termux environment.

## Included Components

- `blux-ollama-acode.deb`: Installs Ollama models and dependencies.
- `blux-ollama-acode-install`: Post-install runner script.
- `blux-ollama-acode-uninstall`: Clean uninstall tool.
- `install_blux_ollama_acode.sh`: One-shot install bootstrap for Termux.

## Installation Instructions

```bash
bash install_blux_ollama_acode.sh
```

Or manually:

```bash
dpkg -i blux-ollama-acode.deb
blux-ollama-acode-install
```

## Uninstall

```bash
blux-ollama-acode-uninstall
```