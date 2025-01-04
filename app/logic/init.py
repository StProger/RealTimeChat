from functools import lru_cache
from punq import Container, Scope

from infra.repositories.messages.base import BaseChatRepository

from infra.repositories.messages.memory import MemoryChatRepository
from logic.commands.messages import CreateChatCommand, CreateChatCommandHandler
from logic.mediator import Mediator



@lru_cache(1)
def init_container():
    return _init_container()


def _init_container() -> Container:
    
    container = Container()

    container.register(BaseChatRepository, MemoryChatRepository, scope=Scope.singleton)
    container.register(CreateChatCommandHandler)
    def init_mediator():
        mediator = Mediator()
        mediator.register_command(
            CreateChatCommand,
            [container.resolve(CreateChatCommandHandler)],
        )
        return mediator
    
    container.register(service=Mediator, factory=init_mediator)

    
    return container