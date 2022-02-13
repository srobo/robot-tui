"""Available commands."""

from typing import Dict, Type

from .command import BaseCommand
from .quit import QuitCommand

COMMANDS: Dict[str, Type[BaseCommand]] = {
    "exit": QuitCommand,
    "quit": QuitCommand,
}

__all__ = ["COMMANDS"]
