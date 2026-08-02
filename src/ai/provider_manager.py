import socket

from src.ai.gemini_provider import GeminiProvider
from src.ai.ollama_provider import OllamaProvider


class ProviderManager:

    def __init__(self):

        self.gemini = GeminiProvider()
        self.ollama = OllamaProvider()

    def is_online(self):

        try:
            socket.create_connection(("8.8.8.8", 53), timeout=2)
            return True
        except OSError:
            return False

    def ask(self, prompt: str):

        if self.is_online():
            return self.gemini.ask(prompt)

        return self.ollama.ask(prompt)