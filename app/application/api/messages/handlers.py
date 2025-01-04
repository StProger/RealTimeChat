from fastapi import APIRouter, Depends
from fastapi import HTTPException, status

from punq import Container

from application.api.messages.schemas import CreateChatRequestSchema, CreateChatResponseSchema
from application.api.schemas import ErrorSchema
from domain.exceptions.base import ApplicationException
from logic.commands.messages import CreateChatCommand
from logic.init import init_container
from logic.mediator import Mediator


router = APIRouter(tags=['Chat'])


@router.post(
        '/',
        response_model=CreateChatResponseSchema, 
        status_code=status.HTTP_201_CREATED,
        description='Ручка создаёт новый чат, если чат с таким названием существует, то возвращается 400 ошибка',
        responses={
            status.HTTP_201_CREATED: {'model': CreateChatResponseSchema},
            status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema},
        }
)
async def create_chat_handler(schema: CreateChatRequestSchema, container: Container = Depends(init_container)):
    """ Создать новый чат """

    mediator: Mediator = container.resolve(Mediator)
    try:
        chat, *_ = await mediator.handle_command(CreateChatCommand(title=schema.title))
    except ApplicationException as ex:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=ex.message)
    
    return CreateChatResponseSchema.from_entity(chat=chat)