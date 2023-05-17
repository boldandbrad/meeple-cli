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


def _bgg_api_get_items(endpoint: str, params: dict) -> List[Item]:
    """Get items from the provided BGG endpoint.

    Args:
        endpoint (str): BGG endpoint.

    Returns:
        List[Item]: List of items.
    """
    response = requests.get(f"{API2_BASE_URL}/{endpoint}", params=params)
    if response.status_code == 200:
        resp_dict = xmltodict.parse(response.content)
        resp_list = resp_dict["items"].get("item", [])
        if not isinstance(resp_list, list):
            resp_list = [resp_list]
        return [Item.from_bgg_dict(bgg_dict) for bgg_dict in resp_list]
    # TODO: log this error and print out a friendly message to the user
    sys.exit(f"Error: HTTP {response.status_code}: {response.content}")


def get_bgg_items(bgg_ids: List[int]) -> List[Item]:
    """Get a list of items with their details from the BGG API.

    Args:
        bgg_ids (List[int]): Item IDs to fetch.

    Returns:
        List[Item]: List of items.
    """
    params = {
        "id": ",".join(map(str, bgg_ids)),
        "type": f"{BOARDGAME_TYPE},{EXPANSION_TYPE}",
        "stats": 1,
    }
    return _bgg_api_get_items(endpoint="thing", params=params)


def get_bgg_item(bgg_id: int) -> Item:
    """Get a single item with its details from the BGG API.

    Args:
        bgg_id (List[int]): Item ID to fetch.

    Returns:
        List[Item]: Item.
    """
    bgg_items = get_bgg_items([bgg_id])
    if bgg_items:
        return bgg_items[0]
    return None


def get_bgg_hot() -> List[Item]:
    """Get the current BGG Hotness items.

    Returns:
        List[Item]: List of items.
    """
    params = {"type": BOARDGAME_TYPE}
    return _bgg_api_get_items(endpoint="hot", params=params)


def search_bgg(query: str) -> List[Item]:
    """Search BGG for items by name.

    Args:
        query (str): Search query.

    Returns:
        List[Item]: List of items.
    """
    params = {"type": BOARDGAME_TYPE, "query": query}
    return _bgg_api_get_items(endpoint="search", params=params)
