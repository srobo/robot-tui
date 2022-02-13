"""The quit command - exits the session."""
from .command import BaseCommand


class QuitCommand(BaseCommand):
    """Quit the terminal."""

    name = "quit"

    async def exec(self) -> None:
        """Execute the command."""
        self._tui.print("Goodbye!")
        self._tui.running = False
