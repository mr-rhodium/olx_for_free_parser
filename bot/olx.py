import httpx
import json
from settings import HEADERS, URL
from settings import redis_settings, RedisSettings
import aioredis
from core.models import TelegramUser, Advert, StopWord
from collections import defaultdict
from aioredis.client import Redis


# TODO need add dependency injection
async def redis_db():
    redis_url: str = await redis_settings.url
    db = await aioredis.from_url(redis_url)
    return db


## TODO need realase
async def exist_user(ads_id: int, db: Redis):
    return await db.exists(ads_id)


## TODO need realase
## TODO function must be tested
async def add_user(user_id: int, ads_id: int, db: Redis):
    status = check_user_in_ads(user_id, ads_id, db)
    if status:
        return status
    else:
        return await db.sadd(ads_id, user_id)


async def check_user_in_ads(ads_id: int, user_id: int, db: Redis):
    scan_ads = await db.scan(cursor=0, match=ads_id)
    if scan_ads:
        if user_id in scan_ads:
            return True
    return False


## TODO need realase
async def chek_ttl(ads_id: int, db: Redis):
    return await db.ttl(ads_id)


## TODO need realase
async def set_ttl(ads_id: int, db: Redis):
    ttl = await chek_ttl(ads_id, db)
    if not ttl:
        db.expire(ads_id, redis_settings.ttl)


async def get_ads():
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            URL,
            headers=HEADERS,
        )
        print(json.loads(resp.text).get("data"))


class MessageAds:
    def __init__(self, telegram_users: list, stop_word: list, ads: list) -> None:
        self.telegram_users = telegram_users
        self.stop_word = stop_word
        self.ads = ads

    ## TODO need test
    def clear_ads(self):
        out = []
        for ad in self.ads:
            if ad.title not in self.stop_words:
                out.append(ad)
        return out

    def users_and_ads(self) -> dict:
        _clear = self.clear_ads()
        data = defaultdict(list)
        for ad in _clear:
            for user in self.telegram_users:
                out = check_user_in_ads(ad.id, user.id, redis_db)
                if not out:
                    add_user(ad.id, user.id, redis_db)
                    data[user].append(ad)
                    set_ttl(ad.id, redis_db)
        return data
        # need check ads in redis db

    def clear(self):
        pass

    @property
    def get(self) -> list:
        out: list = self.users_and_ads()
        # out: list = self.clear_ads()

        # advert = Advert.objects.filter(
        #     telegram_user__id__in=[99321069], advert_id__in=[817599065, 454545]
        # )

        # # TODO need refactor
        # ## just test sended message or not
        # tu = TelegramUser.objects.filter(active=True).all()
        # Advert.objects.select_related("telegram_user").filter(
        #     telegram_user__id__in=tu
        # ).filter(advert_id__in=[817599065])


class BulidData:
    async def extract_ads(self):
        return await get_ads()

    def extract_users():
        return TelegramUser.objects.filter(active=True).all()

    def extract_stop_words():
        return StopWord.objects.all()

    def build(self) -> list:
        _ads = self.extract_ads()
        _users = self.extract_users()
        _stop_words = self.extract_stop_words()

        manager = MessageAds(telegram_users=_users, stop_word=_stop_words, ads=_ads)

        # manager = MessageAds(telegram_user: TelegramUser, stop_word: StopWord, ads)
        # manager.getStopWord, ads)
        return manager.get
