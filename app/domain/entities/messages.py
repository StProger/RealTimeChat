from dataclasses import dataclass, field

import datetime
import uuid

from domain.entities.base import BaseEntity
from domain.events.messages import NewMessageReceivedEvent
from domain.values.messages import Text, Title


@dataclass(eq=False)
class Message(BaseEntity):
    text: Text


@dataclass(eq=False)
class Chat(BaseEntity):
    title: Title
    messages: set[Message] = field(default_factory=set,
                                   kw_only=True)

    def add_message(self, message: Message):

        self.messages.add(message)
        self.register_event(NewMessageReceivedEvent(
            message_text=message.text.as_generic_type(),
            message_oid=message.oid,
            chat_oid=self.oid
        ))
