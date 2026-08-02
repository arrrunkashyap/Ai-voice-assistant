from ai.base_provider import AIProvider


class OllamaProvider(AIProvider):

    def ask(self, prompt):

        return f"[Offline] {prompt}"