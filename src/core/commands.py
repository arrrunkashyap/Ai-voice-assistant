import os
import subprocess
import webbrowser
from datetime import datetime

# ---------- Command Lists ---------- #

CHROME_COMMANDS = [
    "open chrome",
    "launch chrome",
    "start chrome",
    "open browser"
]

VSCODE_COMMANDS = [
    "open vscode",
    "open visual studio code",
    "launch vscode",
    "start vscode"
]

NOTEPAD_COMMANDS = [
    "open notepad",
    "start notepad"
]

CALCULATOR_COMMANDS = [
    "open calculator",
    "start calculator",
    "open calc"
]

PAINT_COMMANDS = [
    "open paint",
    "start paint"
]

EXPLORER_COMMANDS = [
    "open file explorer",
    "open explorer"
]

TASK_MANAGER_COMMANDS = [
    "open task manager",
    "task manager"
]

CMD_COMMANDS = [
    "open cmd",
    "open command prompt"
]

POWERSHELL_COMMANDS = [
    "open powershell"
]

GOOGLE_COMMANDS = [
    "open google"
]

YOUTUBE_COMMANDS = [
    "open youtube"
]

GITHUB_COMMANDS = [
    "open github"
]

CHATGPT_COMMANDS = [
    "open chatgpt"
]

DOWNLOADS_COMMANDS = [
    "open downloads"
]

DOCUMENTS_COMMANDS = [
    "open documents"
]

DESKTOP_COMMANDS = [
    "open desktop"
]

PICTURES_COMMANDS = [
    "open pictures"
]

TIME_COMMANDS = [
    "time",
    "what time",
    "current time"
]

DATE_COMMANDS = [
    "date",
    "today's date",
    "current date"
]

EXIT_COMMANDS = [
    "exit",
    "keep quiet",
    "bye",
    "stop"
]
#----------system commands---#
SYSTEM_COMMANDS = [
    "lock computer",
    "lock pc",
    "lock windows",

    "shutdown computer",
    "shutdown pc",
    "shut down",

    "restart computer",
    "restart pc",

    "sleep computer",
    "sleep pc",

    "log out",
    "logout",
    "sign out"
]

SEARCH_GOOGLE = [
    "search",
    "google"
]

SEARCH_YOUTUBE = [
    "search youtube",
    "youtube search"
]


# ---------- Execute Commands ---------- #

def execute_command(command):

    command = command.lower().strip()

    # ---------------- Chrome ---------------- #

    if any(cmd in command for cmd in CHROME_COMMANDS):

        chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

        if os.path.exists(chrome):
            subprocess.Popen(chrome)
            return "Opening Chrome."

        return "Chrome is not installed."

    # ---------------- VS Code ---------------- #

    if any(cmd in command for cmd in VSCODE_COMMANDS):

        subprocess.Popen("code")
        return "Opening Visual Studio Code."

    # ---------------- Notepad ---------------- #

    if any(cmd in command for cmd in NOTEPAD_COMMANDS):

        subprocess.Popen("notepad")
        return "Opening Notepad."

    # ---------------- Calculator ---------------- #

    if any(cmd in command for cmd in CALCULATOR_COMMANDS):

        subprocess.Popen("calc")
        return "Opening Calculator."

    # ---------------- Paint ---------------- #

    if any(cmd in command for cmd in PAINT_COMMANDS):

        subprocess.Popen("mspaint")
        return "Opening Paint."

    # ---------------- Explorer ---------------- #

    if any(cmd in command for cmd in EXPLORER_COMMANDS):

        subprocess.Popen("explorer")
        return "Opening File Explorer."

    # ---------------- Task Manager ---------------- #

    if any(cmd in command for cmd in TASK_MANAGER_COMMANDS):

        subprocess.Popen("taskmgr")
        return "Opening Task Manager."

    # ---------------- CMD ---------------- #

    if any(cmd in command for cmd in CMD_COMMANDS):

        subprocess.Popen("cmd")
        return "Opening Command Prompt."

    # ---------------- PowerShell ---------------- #

    if any(cmd in command for cmd in POWERSHELL_COMMANDS):

        subprocess.Popen("powershell")
        return "Opening PowerShell."

    # ---------------- Downloads ---------------- #

    if any(cmd in command for cmd in DOWNLOADS_COMMANDS):

        os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))
        return "Opening Downloads."

    # ---------------- Documents ---------------- #

    if any(cmd in command for cmd in DOCUMENTS_COMMANDS):

        os.startfile(os.path.join(os.path.expanduser("~"), "Documents"))
        return "Opening Documents."

    # ---------------- Desktop ---------------- #

    if any(cmd in command for cmd in DESKTOP_COMMANDS):

        os.startfile(os.path.join(os.path.expanduser("~"), "Desktop"))
        return "Opening Desktop."

    # ---------------- Pictures ---------------- #

    if any(cmd in command for cmd in PICTURES_COMMANDS):

        os.startfile(os.path.join(os.path.expanduser("~"), "Pictures"))
        return "Opening Pictures."

    # ---------------- Websites ---------------- #

    if any(cmd in command for cmd in GOOGLE_COMMANDS):

        webbrowser.open("https://www.google.com")
        return "Opening Google."

    if any(cmd in command for cmd in YOUTUBE_COMMANDS):

        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    if any(cmd in command for cmd in GITHUB_COMMANDS):

        webbrowser.open("https://github.com")
        return "Opening GitHub."

    if any(cmd in command for cmd in CHATGPT_COMMANDS):

        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT."

    # ---------------- Search Google ---------------- #

    if command.startswith("search google "):

        query = command.replace("search", "").strip()

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

        return f"Searching Google for {query}"

    #----------youtube search----#
    if command.startswith("search youtube"):

        query = command.replace("search youtube", "").strip()

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={query}"
        )

        return f"Searching YouTube for {query}."
    # ---------------- Time ---------------- #

    if any(cmd in command for cmd in TIME_COMMANDS):

        return datetime.now().strftime(
            "Current time is %I:%M %p"
        )

    # ---------------- Date ---------------- #

    if any(cmd in command for cmd in DATE_COMMANDS):

        return datetime.now().strftime(
            "Today is %d %B %Y"
        )

    #-----system commands--#
    if any(cmd in command for cmd in [
        "lock computer",
        "lock pc",
        "lock windows"
    ]):

        os.system("rundll32.exe user32.dll,LockWorkStation")

        return "Locking your computer."

    if any(cmd in command for cmd in [
        "restart computer",
        "restart pc"

    ]):

        os.system("shutdown /r /t 5")
        return "Restarting your computer." 


    if any(cmd in command for cmd in [
        "sleep computer",
        "sleep pc"

    ]):
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        return "Putting the computer to sleep."

    if "cancel shutdown" in command:

        os.system("shutdown /a")
        return "Shutdown cancelled."
    # ---------------- Exit ---------------- #

    if command in EXIT_COMMANDS:

        return "EXIT"

    return None