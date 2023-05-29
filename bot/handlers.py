from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from helper import CORE_TELEGRAM_USER


router = Router()


@router.message(Command(commands=["start"]))
async def handler_start_command(message: Message) -> None:
    if message.from_user is None:
        return
    _, is_new = await CORE_TELEGRAM_USER.register_bot_user(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        username=message.from_user.username,
    )
    if is_new:
        # TODO send keybotton
        await message.answer("Yes")
    else:
        # TODO send keybotton
        await message.answer("You are already registred")


# TODO need refactor
@router.message(Command(commands=["on"]))
async def send_on(message: Message) -> None:
    await CORE_TELEGRAM_USER.on(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
    )


@router.message(Command(commands=["off"]))
async def send_on(message: Message) -> None:
    await CORE_TELEGRAM_USER.on(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
    )
