"""The quit command - exits the session."""
from typing import List

from .command import BaseCommand


class QuitCommand(BaseCommand):
    """Quit the terminal."""

    description = "Leave the terminal session."

    async def exec(self, args: List[str]) -> None:
        """Execute the command."""
        self._tui.print("Goodbye!")
        self._tui.running = False

    @classmethod
    def validate_args(cls, command: str, args: List[str]) -> List[str]:
        """
        Validate a list of potential arguments to the command.

        :param command: The command that has been called
        :param args: a list of arguments to validate.
        :returns: A list of errors to display.
        """
        if len(args) == 0:
            return []
        else:
            return [f"Expected no arguments to {command}."]
