class Router:

    def route(self, command: str):

        command = command.lower()

        if "open chrome" in command:
            return "open_chrome"

        if "open vscode" in command:
            return "open_vscode"

        if "calculator" in command:
            return "calculator"

        if "shutdown" in command:
            return "shutdown"

        return "ai"