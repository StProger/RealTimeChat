from dataclasses import dataclass

from domain.exceptions.messages import TitleTooLongException, EmptyTextError
from domain.values.base import BaseValueObject


@dataclass(frozen=True)
class Text(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyTextError()

    def as_generic_type(self):
        return str(self.value)


@dataclass(frozen=True)
class Title(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyTextError()
        if len(self.value) > 255:
            raise TitleTooLongException(self.value)

    def as_generic_type(self):
        return str(self.value)