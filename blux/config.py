python
import os

class Config:
    """
    Central configuration for BLUX.
    """
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_DIR = os.path.join(BASE_DIR, '..', 'models', 'llama.cpp', 'models')
    ACTIVE_MODEL_FILE = os.path.join(MODEL_DIR, 'active_model.txt')
    PLUGIN_DIR = os.path.join(BASE_DIR, '..', 'plugins')
    MEMORY_FILE = os.path.join(BASE_DIR, '..', 'memory', 'memory.json')
    GPG_PUBKEY = os.path.join(BASE_DIR, '..', 'blux_author_pubkey.asc')
    HF_TOKEN = os.getenv("HF_TOKEN", "")

