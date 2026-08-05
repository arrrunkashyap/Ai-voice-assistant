APP_ALIASES = {
    "chrome": [
        "chrome",
        "google chrome",
        "browser"
    ],

    "edge": [
        "edge",
        "microsoft edge"
    ],

    "vscode": [
        "vscode",
        "vs code",
        "visual studio code",
        "code",
        "code editor"
    ],

    "notepad": [
        "notepad",
        "text editor"
    ],

    "calculator": [
        "calculator",
        "calc"
    ],

    "explorer": [
        "explorer",
        "file explorer",
        "files"
    ],

    "cmd": [
        "cmd",
        "command prompt"
    ],

    "powershell": [
        "powershell",
        "power shell"
    ]
}

def resolve_app(user_text: str):

    user_text = user_text.lower().strip()

    for app, aliases in APP_ALIASES.items():

        for alias in aliases:

            if alias in user_text:
                return app

    return None