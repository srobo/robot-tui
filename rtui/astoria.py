"""RTUI Astoria Integration."""

from json import JSONDecodeError, loads
from typing import Match, Optional

from astoria.common.config import AstoriaConfig
from astoria.common.consumer import StateConsumer
from astoria.common.messages.astmetad import Metadata, MetadataManagerMessage
from prompt_toolkit import print_formatted_text
from pydantic import ValidationError


class AstoriaIntegration(StateConsumer):
    """Astoria Consumer for RTUI."""

    name = "rtui"

    dependencies = ["astprocd", "astdiskd", "astmetad"]

    def __init__(self, verbose: bool, config_file: Optional[str]) -> None:
        self.config = AstoriaConfig.load(config_file)

        self._setup_logging(verbose, welcome_message=False)
        self._setup_event_loop()
        self._setup_mqtt()

        self._init()

    def _init(self) -> None:
        self._mqtt.subscribe("astmetad", self.handle_astmetad_message)

        self.metadata: Optional[Metadata] = None

    async def main(self) -> None:
        """Main method of the data component."""
        await self.wait_loop()

    async def handle_astmetad_message(
            self,
            match: Match[str],
            payload: str,
    ) -> None:
        """Event handler for metadata changes."""
        if payload:
            try:
                metadata_manager_message = MetadataManagerMessage(**loads(payload))
                self.metadata = metadata_manager_message.metadata
            except (ValidationError, JSONDecodeError):
                print_formatted_text("Bad Message from astmetad")
        else:
            print_formatted_text("Bad Message from astmetad")
