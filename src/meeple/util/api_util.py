import sys
from typing import List

import requests
import xmltodict

from meeple.type.item import Item

BGG_DOMAIN = "boardgamegeek.com"
API2_BASE_URL = f"https://{BGG_DOMAIN}/xmlapi2"

# BoardGameGeek item types
BOARDGAME_TYPE = "boardgame"
EXPANSION_TYPE = "boardgameexpansion"


def _bgg_api_get_items(url: str) -> List[Item]:
    response = requests.get(url)
    if response.status_code == 200:
        resp_dict = xmltodict.parse(response.content)
        resp_list = resp_dict["items"].get("item", [])
        if not isinstance(resp_list, list):
            resp_list = [resp_list]
        return [Item.from_bgg_dict(bgg_dict) for bgg_dict in resp_list]
    # TODO: provide better error handling and logging for bad requests
    sys.exit(f"Error: HTTP {response.status_code}: {response.content}")


def get_bgg_items(bgg_ids: List[int]) -> List[Item]:
    ids_str = ",".join(map(str, bgg_ids))
    url = f"{API2_BASE_URL}/thing?id={ids_str}&type={BOARDGAME_TYPE},{EXPANSION_TYPE}&stats=1"
    return _bgg_api_get_items(url)


def get_bgg_item(bgg_id: int) -> Item:
    bgg_items = get_bgg_items([bgg_id])
    if bgg_items:
        return bgg_items[0]
    return None


def get_bgg_hot() -> List[Item]:
    url = f"{API2_BASE_URL}/hot?type={BOARDGAME_TYPE}"
    return _bgg_api_get_items(url)


def search_bgg(query: str) -> List[Item]:
    url = f"{API2_BASE_URL}/search?type={BOARDGAME_TYPE}&query={query}"
    return _bgg_api_get_items(url)
