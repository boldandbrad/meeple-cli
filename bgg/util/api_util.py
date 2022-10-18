from typing import Any

import requests
import xmltodict

BGG_DOMAIN = "boardgamegeek.com"
API2_BASE_URL = f"https://{BGG_DOMAIN}/xmlapi2"

# bgg item types
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


def get_items(ids: "list[int]") -> list:
    ids_str = ",".join(map(str, ids))
    url = f"{API2_BASE_URL}/thing?id={ids_str}&type={BOARDGAME_TYPE},{EXPANSION_TYPE}&stats=1"
    resp_list = _api_get(url)
    result = []
    for item_dict in resp_list:
        item = {
            "name": _grab_first(item_dict["name"]),
            "year": item_dict["yearpublished"]["@value"],
            "rating": round(
                _parse_item_float_val(item_dict["statistics"]["ratings"]["average"]), 2
            ),
            "rank": _parse_item_rank(item_dict["statistics"]["ratings"]["ranks"]),
            "weight": round(
                _parse_item_float_val(
                    item_dict["statistics"]["ratings"]["averageweight"]
                ),
                2,
            ),
            "players": item_dict["minplayers"]["@value"]
            + "-"
            + item_dict["maxplayers"]["@value"],
            "time": item_dict["minplaytime"]["@value"]
            + "-"
            + item_dict["maxplaytime"]["@value"],
            "id": int(item_dict["@id"]),
            "type": item_dict["@type"],
        }
        result.append(item)
    return result


def get_hot() -> dict:
    url = f"{API2_BASE_URL}/hot?type={BOARDGAME_TYPE}"
    resp_list = _api_get(url)
    result = []
    for item in resp_list:
        _parse_basic_item(item, result)
    return result


def get_search(query: str):
    url = f"{API2_BASE_URL}/search?type={BOARDGAME_TYPE}&query={query}"
    resp_list = _api_get(url)
    result = []
    for item in resp_list:
        _parse_basic_item(item, result)
    return result


def _grab_first(key_dict: dict) -> str:
    if isinstance(key_dict, list):
        return key_dict[0]["@value"]
    return key_dict["@value"]


def _parse_item_rank(ranks_dict: dict) -> Any:
    if isinstance(ranks_dict, dict):
        return _grab_first(ranks_dict["rank"])
    return "Not Ranked"


def _parse_item_float_val(key_dict: dict) -> Any:
    value = key_dict["@value"]
    if value != "":
        return float(value)
    return 0.0


def _parse_basic_item(item_dict: dict, result: list) -> None:
    item = {
        "name": _grab_first(item_dict["name"]),
        "year": item_dict["yearpublished"]["@value"]
        if item_dict.get("yearpublished")
        else "",
        "id": int(item_dict["@id"]),
    }
    result.append(item)
