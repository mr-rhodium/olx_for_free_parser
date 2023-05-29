import asyncio
import httpx
from settings import HEADERS
import json
from abc import ABC, abstractmethod


class BaseParser(ABC):
    def clear_list(self):
        pass

    def get_stop_words(self):
        pass

    def get_data(self) -> json:
        pass


async def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            "https://www.olx.pl/api/v1/offers/?category_id=1151&city_id=17871&district_id=369&filter_enum_price=free&filter_refiners=spell_checker&limit=1&offset=10",
            headers=HEADERS,
        )
        print(json.loads(resp.text).get("data"))


if __name__ == "__main__":
    asyncio.run(main())
