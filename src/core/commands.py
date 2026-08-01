import os
import webbrowser
import subprocess
from datetime import datetime


def execute_command(command: str):
    command = command.lower().strip()

    # ---------------- Browser ---------------- #

    if "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    if "open github" in command:
        webbrowser.open("https://github.com")
        return "Opening GitHub."

    if "open chatgpt" in command:
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT."

    # ---------------- Applications ---------------- #

    if "open chrome" in command:
        chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

        if os.path.exists(chrome):
            subprocess.Popen(chrome)
            return "Opening Chrome."

        return "Chrome is not installed."

    if "open notepad" in command:
        subprocess.Popen("notepad")
        return "Opening Notepad."

    if "open calculator" in command:
        subprocess.Popen("calc")
        return "Opening Calculator."

    if "open vscode" in command:
        subprocess.Popen("code")
        return "Opening Visual Studio Code."

    # ---------------- Date & Time ---------------- #

    if "time" in command:
        return datetime.now().strftime(
            "The current time is %I:%M %p"
        )

    if "date" in command:
        return datetime.now().strftime(
            "Today is %d %B %Y"
        )

    # ---------------- Exit ---------------- #

    if command in ["exit", "quit", "goodbye"]:
        return "EXIT"

    return None