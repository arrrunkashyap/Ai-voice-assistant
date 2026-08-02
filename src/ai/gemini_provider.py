from ai.base_provider import AIProvider


class GeminiProvider(AIProvider):

    def ask(self, prompt):

        return f"[Gemini] {prompt}"