from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command(commands=["start"]))
async def handler_start_command(message: Message) -> None:
    if message.from_user is None:
        return
    # _, is_new = await pass
