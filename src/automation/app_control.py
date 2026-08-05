import subprocess
import psutil
import os
import shutil

import pygetwindow as gw


# --------------------------
# Application Registry
# --------------------------

APP_MAP = {
    "chrome": {
        "exe": "chrome.exe",
        "command": "chrome"
    },
    "edge": {
        "exe": "msedge.exe",
        "command": "msedge"
    },
    "firefox": {
        "exe": "firefox.exe",
        "command": "firefox"
    },
    "vscode": {
        "exe": "Code.exe",
        "command": "code"
    },
    "notepad": {
        "exe": "notepad.exe",
        "command": "notepad"
    },
    "calculator": {
        "exe": "CalculatorApp.exe",
        "command": "calc"
    },
    "cmd": {
        "exe": "cmd.exe",
        "command": "cmd"
    },
    "powershell": {
        "exe": "powershell.exe",
        "command": "powershell"
    },
    "explorer": {
        "exe": "explorer.exe",
        "command": "explorer"
    }
}

def is_running(app_name: str) -> bool:

    app = APP_MAP.get(app_name.lower())

    if not app:
        return False

    exe = app["exe"].lower()

    for process in psutil.process_iter(["name"]):

        try:
            if process.info["name"] and process.info["name"].lower() == exe:
                return True
        except Exception:
            pass

    return False

def focus_window(app_name: str) -> bool:

    keywords = [
        app_name.lower()
    ]

    for window in gw.getAllTitles():

        if any(k in window.lower() for k in keywords):

            try:
                w = gw.getWindowsWithTitle(window)[0]

                if w.isMinimized:
                    w.restore()

                w.activate()

                return True

            except Exception:
                pass

    return False


def open_app(app_name: str):

    app_name = app_name.lower()

    if app_name not in APP_MAP:
        return False, f"I don't know how to open {app_name}."

    if focus_window(app_name):
        return True, f"{app_name} is already open."

    command = APP_MAP[app_name]["command"]

    try:
        subprocess.Popen(command)

        return True, f"Opening {app_name}."

    except FileNotFoundError:

        executable = shutil.which(command)

        if executable:
            subprocess.Popen(executable)
            return True, f"Opening {app_name}."

        return False, f"{app_name} is not installed."

    except Exception as e:

        return False, str(e)


def close_app(app_name: str):

    app = APP_MAP.get(app_name.lower())

    if not app:
        return False, "Unknown application."

    exe = app["exe"].lower()

    closed = False

    for process in psutil.process_iter(["pid", "name"]):

        try:

            if process.info["name"] and process.info["name"].lower() == exe:

                process.kill()

                closed = True

        except Exception:
            pass

    if closed:
        return True, f"{app_name} closed."

    return False, f"{app_name} isn't running."  