"""Available commands."""

from typing import Dict, Type

from .command import BaseCommand
from .help import HelpCommand
from .kill import KillUsercodeCommand
from .metadata import MetadataCommand
from .quit import QuitCommand

COMMANDS: Dict[str, Type[BaseCommand]] = {
    "exit": QuitCommand,
    "help": HelpCommand,
    "kill": KillUsercodeCommand,
    "metadata": MetadataCommand,
    "quit": QuitCommand,
}

__all__ = ["COMMANDS"]
