import pytest

from faker import Faker

from domain.values.messages import Title

from domain.entities.messages import Chat
from infra.repositories.messages.base import BaseChatRepository
from infra.repositories.messages.memory import MemoryChatRepository

from logic.exceptions.messages import ChatWithTitleAlreadyExistsException
from logic.mediator import Mediator
from logic.commands.messages import CreateChatCommand


@pytest.mark.asyncio
async def test_create_chat_command_success(
        chat_repository: MemoryChatRepository,
        mediator: Mediator,
        faker: Faker
):
    chat, *_ = await mediator.handle_command(CreateChatCommand(title=faker.text()))
    chat: Chat
    assert await chat_repository.check_exist_by_title(title=chat.title.as_generic_type())


@pytest.mark.asyncio
async def test_create_chat_command_title_already_exists(
        chat_repository: MemoryChatRepository,
        mediator: Mediator,
        faker: Faker
):
    title = faker.text()
    chat = Chat(title=Title(title))
    await chat_repository.add_chat(chat=chat)
    
    with pytest.raises(ChatWithTitleAlreadyExistsException):
        await mediator.handle_command(CreateChatCommand(title=title))
    assert len(chat_repository._saved_chats) == 1