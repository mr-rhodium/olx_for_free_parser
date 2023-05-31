# import asyncio
# import httpx
# from bot.settings import HEADERS, BOT_THOKEN
# from bot.handlers import router
# import json
# from abc import ABC, abstractmethod
# import os
# import os
# import django
# from aiogram import Dispatcher, Bot

# # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parser.settings")
# # django.setup()


# # class BaseParser(ABC):
# #     def clear_list(self):
# #         pass

# #     def get_stop_words(self):
# #         pass

# #     def get_data(self) -> json:
# #         pass


# # # async def main():
# # #     headers = {
# # #         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
# # #     }
# # #     async with httpx.AsyncClient() as client:
# # #         resp = await client.get(
# # #             "https://www.olx.pl/api/v1/offers/?category_id=1151&city_id=17871&district_id=369&filter_enum_price=free&filter_refiners=spell_checker&limit=1&offset=10",
# # #             headers=HEADERS,
# # #         )
# # #         print(json.loads(resp.text).get("data"))


# # # TODO logging
# # # import logging
# # from aiogram import Dispatcher, Bot
# # from aiogram.types import BotCommand


# # # # TODO Add router
# # # def _register_routers() -> None:
# # #     # dispatcher.include_router()
# # #     pass


# # # TODO send message
# # async def send_message(bot: Bot, user_id: int, message: str):
# #     await bot.send_message(user_id, message)


# # async def set_bot_command(bot) -> None:
# #     await bot.set_my_commands(
# #         [
# #             BotCommand(command="/start", description="Start bot"),
# #             BotCommand(command="/on", description="Parser On"),
# #             BotCommand(command="/off", description="Parse Off"),
# #         ]
# #     )


# async def main() -> None:
#     # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parser.settings")

#     dp = Dispatcher()

#     # dispatcher.startup(set_bot_command(bot))
#     dp.include_router(router)
#     bot = Bot(BOT_THOKEN, parse_mode="HTML")
#     await dp.start_polling(bot)

#     for item in range(1, 10):
#         print(item)
#         asyncio.sleep(item)


# if __name__ == "__main__":
#     import os
#     import django

#     os.environ["DJANGO_SETTINGS_MODULE"] = "parser.settings"
#     django.setup()
#     from django.conf import settings
#     from parser.settings import INSTALLED_APPS

#     settings.configure(DEBUG=True, INSTALLED_APPS=INSTALLED_APPS)
#     asyncio.run(main())

import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from bot.settings import HEADERS, BOT_THOKEN
from bot.handlers import router

bot = Bot(BOT_THOKEN, parse_mode="HTML")

dispatcher = Dispatcher()
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def _register_routers() -> None:
    dispatcher.include_router(router)


async def _set_bot_commands() -> None:
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Start bot"),
            BotCommand(command="/apps", description="Show installed apps"),
        ]
    )


@dispatcher.startup()
async def on_startup() -> None:
    # Register all routers
    _register_routers()

    # Set default commands
    await _set_bot_commands()


def run_polling() -> None:
    dispatcher.run_polling(bot)


if __name__ == "__main__":
    run_polling()
