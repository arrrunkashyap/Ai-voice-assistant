import os
from dotenv import load_dotenv

load_dotenv()

AI_PROVIDER = "gemini"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-3-flash-preview"

OLLAMA_MODEL = "llama3.2"
OLLAMA_URL = "http://localhost:11434"

ASSISTANT_NAME = "Evi"
USER_NAME = "Arun"