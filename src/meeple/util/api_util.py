import json
import time
from typing import List

import requests
import xmltodict

from meeple.type import BGGCollectionItem, BGGUser
from meeple.type.item import Item
from meeple.util.message_util import error_msg
from meeple.util.output_util import CustomProgress

BGG_DOMAIN = "boardgamegeek.com"

JSON_API_BASE_URL = "https://api.geekdo.com/api"
XML2_API_BASE_URL = f"https://{BGG_DOMAIN}/xmlapi2"

# BoardGameGeek item types
BOARDGAME_TYPE = "boardgame"
EXPANSION_TYPE = "boardgameexpansion"


def _bgg_json_api_get(endpoint: str, params: dict = {}) -> dict:
    """Get items from provided GeekDo JSON API endpoint.

    Args:
        endpoint (str): GEEKDO API endpoint.
        params (dict): Request parameters.

    Returns:
        response_dict: Dictionary representation of response.
    """
    response = requests.get(f"{JSON_API_BASE_URL}/{endpoint}", params=params)
    match response.status_code:
        case 200:
            return json.loads(response.content)
        case _:
            error_msg(
                f"Unknown GeekDo API Error | HTTP {response.status_code} | {response.content}"
            )


def _bgg_xml2_api_get(endpoint: str, params: dict = {}) -> List[Item]:
    """Get items from the provided BGG endpoint.

    Args:
        endpoint (str): BGG endpoint.
        params (dict): Request parameters.

    Returns:
        response_dict: Dictionary representation of response.
    """
    while True:
        response = requests.get(f"{XML2_API_BASE_URL}/{endpoint}", params=params)
        match response.status_code:
            case 200:
                # successful return
                return xmltodict.parse(response.content)
            case 202:
                # wait and ping again for response
                time.sleep(12)
            case 429:
                # rate limit reached
                error_msg(
                    "BoardGameGeek API rate limit exceeded. Please try again later."
                )
            case _:
                # unknown api error
                # TODO: log this error and print out a friendlier message to the user
                error_msg(
                    f"Unknown BGG API Error | HTTP {response.status_code} | {response.content}"
                )


def _serialize_resp_dict(resp_dict: dict, obj_class) -> List:
    resp_list = resp_dict["items"].get("item", [])
    if not isinstance(resp_list, list):
        resp_list = [resp_list]
    return [obj_class.from_bgg_dict(bgg_dict) for bgg_dict in resp_list]


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
    resp_dict = _bgg_xml2_api_get(endpoint="thing", params=params)
    return _serialize_resp_dict(resp_dict, Item)


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
    resp_dict = _bgg_xml2_api_get(endpoint="hot", params=params)
    return _serialize_resp_dict(resp_dict, Item)


def search_bgg(query: str) -> List[Item]:
    """Search BGG for items by name.

    Args:
        query (str): Search query.

    Returns:
        List[Item]: List of items.
    """
    params = {"type": BOARDGAME_TYPE, "query": query}
    resp_dict = _bgg_xml2_api_get(endpoint="search", params=params)
    return _serialize_resp_dict(resp_dict, Item)


def get_bgg_user(username: str) -> BGGUser:
    """Get BGG User details by username.

    Args:
        username (str): username.

    Returns:
        BGGUser: BGGUser.
    """
    params = {"name": username}
    resp_dict = _bgg_xml2_api_get(endpoint="user", params=params)
    return BGGUser.from_bgg_dict(resp_dict["user"])


def get_bgg_user_collection(username: str) -> List[BGGCollectionItem]:
    """Get BGG User Collection by username.

    Args:
        username (str): username.

    Returns:
        List[BGGCollectionItem]: List[BGGCollectionItem].
    """
    params = {"username": username, "brief": 1}
    with CustomProgress() as progress:
        progress.add_task("Fetching collection", start=False, total=None)
        resp_dict = _bgg_xml2_api_get(endpoint="collection", params=params)
    return _serialize_resp_dict(resp_dict, BGGCollectionItem)


def get_campaigns() -> dict:
    return _bgg_json_api_get(endpoint="ending_preorders")
