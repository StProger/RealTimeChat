from dataclasses import dataclass

from domain.entities.messages import Chat
from domain.values.messages import Title
from infra.repositories.messages import BaseChatRepository
from logic.commands.base import BaseCommand, CommandHandler
from logic.exceptions.messages import ChatWithTitleAlreadyExistsException


@dataclass(frozen=True)
class CreateChatCommand(BaseCommand):
    title: str


@dataclass(frozen=True)
class CreateChatCommandHandler(CommandHandler[CreateChatCommand, Chat]):
    chat_repository: BaseChatRepository

    async def handle(self, command: CreateChatCommand) -> Chat:
        if await self.chat_repository.check_exist_by_title(command.title):

            raise ChatWithTitleAlreadyExistsException(command.title)

        title = Title(value=command.title)
        # TODO: считать ивенты
        chat = Chat.create_chat(title=title)
        await self.chat_repository.add_chat(chat)

        return chat
