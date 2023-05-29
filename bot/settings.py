HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
URL: str = "https://www.olx.pl/api/v1/offers/?category_id=1151&city_id=17871&district_id=369&filter_enum_price=free&filter_refiners=spell_checker&limit=40&offset=0"
BOT_THOKEN: str = "961019773:AAF271xwgF8lskKr8x7exxMgzfgNGOioUuY"


# from enum import Enum

# from app.config import env


# class RunningMode(str, Enum):
#     LONG_POLLING = "LONG_POLLING"
#     WEBHOOK = "WEBHOOK"


# TG_TOKEN = env("TG_TOKEN", cast=str)

# RUNNING_MODE = env("RUNNING_MODE", cast=RunningMode, default=RunningMode.LONG_POLLING)
# WEBHOOK_URL = env("WEBHOOK_URL", cast=str, default="")
