class History:

    def __init__(self):

        self.messages = []

    def add_user(self, text):

        self.messages.append({
            "role": "user",
            "text": text
        })

    def add_assistant(self, text):

        self.messages.append({
            "role": "assistant",
            "text": text
        })

    def get(self):

        return self.messages

    def clear(self):

        self.messages.clear()