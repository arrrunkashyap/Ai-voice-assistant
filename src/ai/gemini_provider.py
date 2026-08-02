from src.ai.base_provider import BaseProvider


class GeminiProvider(BaseProvider):

    def ask(self, prompt):

        return "[Gemini] " + prompt