from google import genai

from src.ai.base_provider import BaseProvider
from src import config


class GeminiProvider(BaseProvider):

    def __init__(self):
        self.client = genai.Client(
            api_key=config.GEMINI_API_KEY
        )

    def ask(self, prompt: str) -> str:
        try:
            response = self.client.models.generate_content(
                model=config.GEMINI_MODEL,
                contents=prompt,
            )

            return response.text

        except Exception as e:
            return f"Gemini Error: {e}"