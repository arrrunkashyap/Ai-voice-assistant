from src.audio.listener import listen
from src.audio.speaker import speak

from src.core.commands import execute_command
from src.core.brain import ask_ai

from src.config import ASSISTANT_NAME


def main():

    speak(f"Hello, I am {ASSISTANT_NAME}. How can I help you?")

    while True:

        command = listen()

        if not command:
            continue

        response = execute_command(command)

        if response == "EXIT":
            speak("Goodbye!")
            break

        if response is None:
            response = ask_ai(command)

        speak(response)


if __name__ == "__main__":
    main()