from src.audio.listener import listen
from src.audio.speaker import speak
from src.core.brain import ask_ai
from src.core.commands import execute_command


def main():

    speak("Hello Arun. I am Evi. How can I help you?")

    while True:

        command = listen()

        if command == "":
            continue

        local = execute_command(command)

        if local:

            speak(local)

            if local == "Goodbye!":
                break

            continue

        reply = ask_ai(command)

        speak(reply)


if __name__ == "__main__":
    main()