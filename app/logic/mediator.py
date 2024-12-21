from collections import defaultdict
from dataclasses import dataclass, field

from domain.events.base import BaseEvent
from logic.commands.base import BaseCommand, CommandHandler, CT, CR
from logic.events.base import EventHandler, ET, ER


@dataclass(eq=False)
class Mediator:

    events_map: dict[ET, EventHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )
    commands_map: dict[CT, CommandHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )

    def register_event(self, event: ET, event_handler: EventHandler[ET, ER]):
        self.events_map[event.__class__].append(event_handler)

    def register_command(self, command: CT, command_handler: EventHandler[CT, CR]):
        self.commands_map[command.__class__].append(command_handler)