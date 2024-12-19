import uuid
from abc import ABC
from dataclasses import dataclass, field

import datetime


@dataclass
class BaseEntity:
    oid: str = field(default_factory=lambda: str(uuid.uuid4()),
                     kw_only=True)
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now,
                                          kw_only=True)

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, __value: 'BaseEntity') -> bool:
        return self.oid == __value.oid