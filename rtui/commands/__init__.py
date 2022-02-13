"""Available commands."""

from typing import Dict, Type

from .command import BaseCommand
from .quit import QuitCommand

COMMANDS: Dict[str, Type[BaseCommand]] = {
    "quit": QuitCommand,
}

__all__ = ["COMMANDS"]
