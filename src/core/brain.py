from google import genai
from src.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_ai(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return "Sorry, I couldn't connect to Gemini right now."