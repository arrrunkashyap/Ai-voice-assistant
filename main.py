from dotenv import load_dotenv

load_dotenv()

from src.core.assistant import Assistant

assistant = Assistant()
assistant.start()  