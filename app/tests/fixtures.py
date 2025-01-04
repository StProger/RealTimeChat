from punq import Container, Scope

from infra.repositories.messages.base import BaseChatRepository
from infra.repositories.messages.memory import MemoryChatRepository
from logic.init import _init_container
from logic.mediator import Mediator



def init_dummy_container() -> Container:
    container = _init_container()
    container.register(BaseChatRepository, MemoryChatRepository, scope=Scope.singleton)
    return container


if __name__ == "__main__":

    container: Container = init_dummy_container()

    print(container.resolve(BaseChatRepository))