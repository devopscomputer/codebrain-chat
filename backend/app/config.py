# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MODEL_API_URL: str = os.getenv("MODEL_API_URL", "http://localhost:11434/api/generate")
    DEFAULT_MODEL: str = os.getenv("DEFAULT_MODEL", "mistral")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()