from dataclasses import dataclass

from abc import ABC, abstractmethod

from typing import Generic, TypeVar, Any

from domain.events.base import BaseEvent

ET = TypeVar(name='ET', bound=BaseEvent)
ER = TypeVar(name='ER', bound=Any)

@dataclass
class EventHandler(ABC, Generic[ET, ER]):
    def handle(self, event: ET) -> ER:
        ...
