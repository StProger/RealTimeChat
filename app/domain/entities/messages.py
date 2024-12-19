from dataclasses import dataclass, field

import uuid

import datetime

from domain.values.messages import Text, Title


@dataclass
class Message:

    oid: str = field(default_factory=lambda: str(uuid.uuid4()),
                     kw_only=True)
    text: Text
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now,
                                          kw_only=True)


@dataclass
class Chat:
    oid: str = field(default_factory=lambda: str(uuid.uuid4()),
                     kw_only=True)
    title: Title
    messages: list[Message] = field(default_factory=list,
                                    kw_only=True)