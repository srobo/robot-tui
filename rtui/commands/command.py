"""Base Command classes."""
from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rtui.tui import TUI


class BaseCommand(metaclass=ABCMeta):
    """A base command class."""

    def __init__(self, tui: 'TUI') -> None:
        self._tui = tui

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Name of the command.

        :returns: The name of the command, lowercase as a single word.
        """
        raise NotImplementedError  # pragma: nocover

    @abstractmethod
    async def exec(self) -> None:
        """Execute the command."""
        raise NotImplementedError  # pragma: nocover
