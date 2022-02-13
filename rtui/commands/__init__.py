"""Available commands."""

from typing import Dict, Type

from .command import BaseCommand
from .help import HelpCommand
from .quit import QuitCommand

COMMANDS: Dict[str, Type[BaseCommand]] = {
    "exit": QuitCommand,
    "help": HelpCommand,
    "quit": QuitCommand,
}

__all__ = ["COMMANDS"]
