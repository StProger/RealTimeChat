from dataclasses import dataclass

from logic.exceptions.base import LogicException


@dataclass(eq=False)
class ChatWithTitleAlreadyExistsException(LogicException):

    title: str

    @property
    def message(self):
        return f'Чат с таким названием уже существует: "{self.title}"'