class History:

    def __init__(self, max_messages=20):
        self.max_messages = max_messages
        self.messages = []

    def add_user(self, text):
        self.messages.append({
            "role": "user",
            "text": text
        })
        self._trim()

    def add_assistant(self, text):
        self.messages.append({
            "role": "assistant",
            "text": text
        })
        self._trim()

    def get(self):
        return self.messages

    def clear(self):
        self.messages.clear()

    def _trim(self):
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]