from src.audio.listener import listen
from src.audio.speaker import speak

from src.core.commands import execute_command

from src.ai.provider_manager import ProviderManager

from src.memory.history import History
from src.memory.session import Session

from src.config import ASSISTANT_NAME


class Assistant:

    def __init__(self):

        self.ai = ProviderManager()
        self.history = History()
        self.session = Session()

    def greet(self):

        speak(f"Hello, I am {ASSISTANT_NAME}. How can I help you?")

    def process(self, command):

        try:

            # Store user message
            self.history.add_user(command)

            # Check local commands first
            response = execute_command(command)

            if response == "EXIT":
                return "EXIT"

            # If not a local command, ask AI
            if response is None:

                response = ""

                print("EVI: ", end="", flush=True)

                for chunk in self.ai.stream(
                    command,
                    self.history.get()
                ):
                    print(chunk, end="", flush=True)
                    response += chunk

                print()

            # Save every assistant response
            self.history.add_assistant(response)

            return response

        except Exception as e:

            print(e)

            return "Sorry, something went wrong."

    def start(self):

        self.greet()

        while True:

            command = listen()

            if not command or len(command.strip()) < 2:
                continue

            response = self.process(command)

            if response == "EXIT":
                speak("Goodbye!")
                break

            if response:
                speak(response)