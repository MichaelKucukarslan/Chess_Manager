import re
from abc import ABC, abstractmethod
from datetime import datetime

class BaseScreen(ABC):
    """Abstract class for screen interaction"""

    @abstractmethod
    def get_command(self):
        """Child classes must implement this method. It must return a Command."""
        pass

    def input_string(self, prompt="", default=None, empty=False):
        """
        Utility function: get a string from the screen.
        If default is provided and the user provides an empty response, then the default value is used.
        If empty is True, a user cannot provide an empty response.
        """

        prompt = prompt + "? "

        if default:
            prompt += f"[{default}] "

        while True:
            value = input(prompt)

            if not value and default:
                value = default

            if not empty:
                return value
            if empty and value:
                return value