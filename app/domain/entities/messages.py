from dataclasses import dataclass, field

import datetime
import uuid

from domain.entities.base import BaseEntity
from domain.values.messages import Text, Title


@dataclass
class Message:
    text: Text
    oid: str = field(default_factory=lambda: str(uuid.uuid4()),
                     kw_only=True)
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now,
                                          kw_only=True)

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, __value: 'BaseEntity') -> bool:
        return self.oid == __value.oid


@dataclass
class Chat:
    title: Title
    messages: set[Message] = field(default_factory=set,
                                   kw_only=True)
    oid: str = field(default_factory=lambda: str(uuid.uuid4()),
                     kw_only=True)
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now,
                                          kw_only=True)

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, __value: 'BaseEntity') -> bool:
        return self.oid == __value.oid

    def add_message(self, message: Message):

        self.messages.add(message)