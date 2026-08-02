from src.ai.base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    def ask(self, prompt):

        return "[Offline] " + prompt