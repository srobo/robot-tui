"""Available commands."""

from typing import Dict, Type

from .command import BaseCommand
from .help import HelpCommand
from .kill import KillUsercodeCommand
from .metadata import ArenaCommand, MetadataCommand, ModeCommand, ZoneCommand
from .quit import QuitCommand
from .restart import RestartUsercodeCommand
from .start import StartTriggerCommand

COMMANDS: Dict[str, Type[BaseCommand]] = {
    "arena": ArenaCommand,
    "exit": QuitCommand,
    "help": HelpCommand,
    "kill": KillUsercodeCommand,
    "metadata": MetadataCommand,
    "mode": ModeCommand,
    "quit": QuitCommand,
    "restart": RestartUsercodeCommand,
    "start": StartTriggerCommand,
    "trigger": StartTriggerCommand,
    "zone": ZoneCommand,
}

__all__ = ["COMMANDS"]
