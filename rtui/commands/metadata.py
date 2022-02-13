"""Command to display robot metadata."""
from typing import List

from .command import BaseCommand


class MetadataCommand(BaseCommand):
    """Show all robot metadata."""

    description = "Show all robot metadata"

    async def exec(self, args: List[str]) -> None:
        """Execute the command."""
        for i, v in sorted(self._tui.astoria.metadata.__dict__.items()):
            self._tui.print(f"{i}: {v}")

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
            return [f"{command} does not expect any arguments."]
