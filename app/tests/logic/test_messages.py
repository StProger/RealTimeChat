import pytest

from domain.entities.messages import Chat
from infra.repositories.messages import BaseChatRepository
from logic.mediator import Mediator
from logic.commands.messages import CreateChatCommand


@pytest.mark.asyncio
async def test_create_chat_command_success(
        chat_repository: BaseChatRepository,
        mediator: Mediator
):
    # TODO: Закинуть faker для генерации текстов
    chat: Chat = (await mediator.handle_command(CreateChatCommand(title='gigaTitle')))[0]
    assert await chat_repository.check_exist_by_title(title=chat.title.as_generic_type())
