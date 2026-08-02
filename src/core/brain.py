from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

conversation = []


def ask_ai(prompt: str):
    conversation.append(
        {
            "role": "user",
            "parts": [{"text": prompt}]
        }
    )

    try:
        response = client.models.generate_content(
            model="models/gemini-3.1-flash-live-preview",
            contents=conversation
        )

        answer = response.text

        conversation.append(
            {
                "role": "model",
                "parts": [{"text": answer}]
            }
        )

        return answer

    except Exception as e:
        print("Gemini Error:", e)
        return "Sorry, I couldn't answer that."