import httpx
import json
from settings import HEADERS, URL


async def get():
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            URL,
            headers=HEADERS,
        )
        print(json.loads(resp.text).get("data"))


class Filter:
    def __init__(self, db) -> None:
        self.db = db

    def get_stop_words():
        pass

    def clear(self):
        pass

    @property
    def get(self):
        pass


class BulidData:
    def extract_data(self):
        pass

    def build():
        pass
