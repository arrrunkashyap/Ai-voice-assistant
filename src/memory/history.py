class History:

    def __init__(self):
        self.messages = []

    def add(self, role, text):

        self.messages.append(
            {
                "role": role,
                "text": text
            }
        )

    def get(self):

        return self.messages

    def clear(self):

        self.messages.clear()