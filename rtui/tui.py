"""The TUI class."""

from prompt_toolkit import PromptSession, print_formatted_text

from .commands import COMMANDS


class TUI:
    """The Terminal User Interface."""

    def __init__(self) -> None:
        self._session = self._get_session()
        self.running: bool = True

    def _get_session(self) -> PromptSession[str]:
        """Get a prompt session."""
        return PromptSession(
            message="> ",
            placeholder="Enter a command, or help to list available commands!",
        )

    def print(self, text: str) -> None:
        """
        Print something to the terminal.

        This is a convenience alias for print_formatted_text.
        """
        print_formatted_text(text)

    async def run_tui(self) -> None:
        """Run the main loop for the TUI."""
        await self.welcome()
        while self.running:
            command = await self._session.prompt_async()
            if command:
                try:
                    com_class = COMMANDS[command]
                    com = com_class(self)
                    await com.exec()
                except KeyError:
                    self.print(f"Unknown command: {command}")

    async def welcome(self) -> None:
        """Print the welcome message."""
        self.print("Student Robotics OS")
