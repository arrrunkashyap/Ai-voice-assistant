from ollama import chat
from ai.base_provider import AIProvider


class OllamaProvider(AIProvider):

    def ask(self, prompt: str) -> str:

        try:

            response = chat(
                model="qwen2.5:3b",
                messages=[
                    {
                        "role": "system",
                        "content": "You are EVI, an intelligent desktop voice assistant. Keep responses short and conversational."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response["message"]["content"]

        except Exception as e:
            return f"Offline AI Error: {e}"