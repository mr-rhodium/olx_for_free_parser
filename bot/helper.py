from typing import Final
from core.models import TelegramUser, Advert


class CoreTelegramUser:
    @staticmethod
    async def register_bot_user(
        user_id: int,
        chat_id: int,
        username: str or None,
    ) -> tuple[TelegramUser, bool]:
        return await TelegramUser.objects.aget_or_create(
            id=user_id,
            chat_id=chat_id,
            username=username,
        )


class CoreAdvert:
    @staticmethod
    async def insert_advert_id(chat_id: int, advert_id: int):
        user = await TelegramUser.objects.aget(chat_id=chat_id)
        return await Advert.objects.aget_or_create(
            telegram_user=user, chat_id=advert_id
        )


CORE_TELEGRAM_USER: Final[CoreTelegramUser] = CoreTelegramUser()
CORE_ADVERT: Final[CoreAdvert] = CoreAdvert()
