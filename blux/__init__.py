# BLUX v2.0 - The Sovereign Android AI Forge
"""
BLUX package initialization
"""

__version__ = "2.0.0"
__author__ = "JADIS"

# Import main components for easier access
from .ai_engine import AIEngine
from .memory import Memory
from .config import Config
from .plugin_loader import load_plugins

__all__ = ['AIEngine', 'Memory', 'Config', 'load_plugins']
