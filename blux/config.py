import os

class Config:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
    MODEL_PATH = "./models/llama.cpp/"
    WHISPER_PATH = "./models/whisper.cpp/"
    WAKEWORD_PATH = "./models/openwakeword/"


