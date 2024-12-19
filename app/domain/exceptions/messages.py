from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=True)
class TextTooLongException(ApplicationException):
    text: str

    @property
    def message(self):

        return f'Слишком длинный текст сообщения {self.text[:255]}...'

@dataclass(eq=True)
class EmptyTextError(ApplicationException):

    @property
    def message(self):
        return 'Текст не может быть пустым'
