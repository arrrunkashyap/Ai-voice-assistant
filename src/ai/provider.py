from utils.internet import is_online


class Provider:

    def __init__(self):
        self.provider = None

    def load(self):

        if is_online():
            from ai.gemini_provider import GeminiProvider
            self.provider = GeminiProvider()
        else:
            from ai.ollama_provider import OllamaProvider
            self.provider = OllamaProvider()

    def ask(self, prompt):

        if self.provider is None:
            self.load()

        return self.provider.ask(prompt)