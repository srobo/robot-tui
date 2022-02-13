"""The TUI class."""

from prompt_toolkit import PromptSession, print_formatted_text


class TUI:
    """The Terminal User Interface."""

    def __init__(self) -> None:
        self._session = self._get_session()
        self._running: bool = True

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
        while self._running:
            command = await self._session.prompt_async()
            self.print(f"Command: {command}")

    async def welcome(self) -> None:
        """Print the welcome message."""
        self.print("Student Robotics OS")
