from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def ask(self, prompt: str) -> str:
        """Return AI response."""
        pass