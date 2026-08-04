from google import genai
from google.genai.errors import ClientError

from src.ai.base_provider import BaseProvider
from src import config


class GeminiProvider(BaseProvider):

    def __init__(self):
        self.client = genai.Client(
            api_key=config.GEMINI_API_KEY
        )

    def ask(self, prompt: str) -> str:
        try:
            stream = self.client.models.generate_content_stream(
                model=config.GEMINI_MODEL,
                contents=prompt,
            )

            final_text = ""

            for chunk in stream:
                if chunk.text:
                    print(chunk.text, end="", flush=True)
                    final_text += chunk.text

            print()
            return final_text

        except ClientError as e:
            if e.code == 429:
                return "I'm receiving too many requests right now."

            if e.code == 404:
                return f"Model '{config.GEMINI_MODEL}' not found."

            return f"Gemini API Error: {e}"

        except Exception as e:
            return f"Unexpected error: {e}"


    def stream(self, prompt: str):
        stream = self.client.models.generate_content_stream(
        model=config.GEMINI_MODEL,
        contents=prompt,
        )

        for chunk in stream:
            if chunk.text:
                yield chunk.text