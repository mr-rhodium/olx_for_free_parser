from functools import lru_cache
from pydantic import BaseSettings


HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
# TODO need refactor
URL: str = "https://www.olx.pl/api/v1/offers/?category_id=1151&city_id=17871&district_id=369&filter_enum_price=free&filter_refiners=spell_checker&limit=40&offset=0"
BOT_THOKEN: str = "961019773:AAF271xwgF8lskKr8x7exxMgzfgNGOioUuY"
TIME_OUT_REQUEST = 100
TIME_OUT_REQUEST_LONG_POLLING = 60


class RedisSettings(BaseSettings):
    REDIS_HOST: str = ""
    REDIS_PORT: int = 0
    REDIS_DB: int = 0
    REDIS_PASSWORD: str = ""
    TTl = 60 * 60 * 24  # 1 day

    @property
    def ttl(self) -> int:
        return int(self.TTl)

    @property
    def url(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"  # noqa: A003


@lru_cache()
def redis_settings() -> RedisSettings:
    return RedisSettings()
