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


def _api_get(url: str) -> dict:
    response = requests.get(url)
    if response.status_code == 200:
        resp_dict = xmltodict.parse(response.content)
        items = resp_dict["items"].get("item", [])
        if not isinstance(items, list):
            return [items]
        return items
    # TODO: provide better error handling and logging for bad requests
    sys.exit(f"Error: HTTP {response.status_code}: {response.content}")


def get_items(ids: List[int]) -> List:
    ids_str = ",".join(map(str, ids))
    url = f"{API2_BASE_URL}/thing?id={ids_str}&type={BOARDGAME_TYPE},{EXPANSION_TYPE}&stats=1"
    resp_list = _api_get(url)
    result = []
    for item_dict in resp_list:
        result.append(Item(item_dict))
    return result


def get_hot() -> dict:
    url = f"{API2_BASE_URL}/hot?type={BOARDGAME_TYPE}"
    resp_list = _api_get(url)
    result = []
    for item_dict in resp_list:
        result.append(Item(item_dict))
    return result


# TODO: figure out how to allow user to only search for board games or expansions
# current api returns both as board game type for some reason
def get_search(query: str):
    url = f"{API2_BASE_URL}/search?type={BOARDGAME_TYPE}&query={query}"
    resp_list = _api_get(url)
    result = []
    for item_dict in resp_list:
        result.append(Item(item_dict))
    return result
