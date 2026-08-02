from src.audio.listener import listen
from src.audio.speaker import speak

from src.core.commands import execute_command
from src.core.brain import ask_ai

from src.config import ASSISTANT_NAME


class Assistant:

    def __init__(self):
        pass

    def process(self, command: str):

        response = execute_command(command)

        if response == "EXIT":
            return "EXIT"

        if response is None:
            response = ask_ai(command)

        return response

    def start(self):

        speak(f"Hello, I am {ASSISTANT_NAME}. How can I help you?")

        while True:

            command = listen()

            if not command:
                continue

            response = self.process(command)

            if response == "EXIT":
                speak("Goodbye!")
                break

            if response:
                speak(response)