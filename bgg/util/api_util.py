from typing import Any

import requests
import xmltodict

API2_BASE_URL = "https://boardgamegeek.com/xmlapi2"

# bgg item types
BOARDGAME_TYPE = "boardgame"
EXPANSION_TYPE = "boardgameexpansion"


class API_Result:
    def __init__(self):
        self.boardgames = []
        self.expansions = []


def get_items(ids: "list[int]") -> API_Result:
    ids_str = ",".join(map(str, ids))
    url = f"{API2_BASE_URL}/thing?id={ids_str}&type={BOARDGAME_TYPE},{EXPANSION_TYPE}&stats=1"
    response = requests.get(url)
    if response.status_code == 200:
        resp_dict = xmltodict.parse(response.content)
        # build and result object
        return _parse_response(resp_dict)
    else:
        # TODO: provide better error handling and logging for bad requests
        sys.exit(f"Error: HTTP {response.status_code}: {response.content}")


def get_hot() -> dict:
    url = f"{API2_BASE_URL}/hot?type={BOARDGAME_TYPE}"
    response = requests.get(url)
    if response.status_code == 200:
        resp_dict = xmltodict.parse(response.content)
        return resp_dict
    else:
        # TODO: provide better error handling and logging for bad requests
        sys.exit(f"Error: HTTP {response.status_code}: {response.content}")


def get_search(query: str):
    url = f"{API2_BASE_URL}/search?type={BOARDGAME_TYPE}&query={query}"
    response = requests.get(url)
    if response.status_code == 200:
        resp_dict = xmltodict.parse(response.content)
        return resp_dict
    else:
        # TODO: provide better error handling and logging for bad requests
        sys.exit(f"Error: HTTP {response.status_code}: {response.content}")


def _parse_item_name(name_dict: dict) -> str:
    if isinstance(name_dict, list):
        return name_dict[0]["@value"]
    else:
        return name_dict["@value"]


def _parse_item_rank(ranks_dict: dict) -> Any:
    if isinstance(ranks_dict, dict):
        rank_dict = ranks_dict["rank"]
        if isinstance(rank_dict, list):
            return rank_dict[0]["@value"]
        else:
            return rank_dict["@value"]
    else:
        return "Not Ranked"


def _parse_item_float_val(key_dict: dict) -> Any:
    value = key_dict["@value"]
    if value != "":
        return float(value)
    else:
        return 0.0


def _parse_item(item_dict: dict, result: API_Result) -> None:
    item = {
        "name": _parse_item_name(item_dict["name"]),
        "year": item_dict["yearpublished"]["@value"],
        "rating": round(
            _parse_item_float_val(item_dict["statistics"]["ratings"]["average"]), 2
        ),
        "rank": _parse_item_rank(item_dict["statistics"]["ratings"]["ranks"]),
        "weight": round(
            _parse_item_float_val(item_dict["statistics"]["ratings"]["averageweight"]),
            2,
        ),
        "players": item_dict["minplayers"]["@value"]
        + "-"
        + item_dict["maxplayers"]["@value"],
        "time": item_dict["minplaytime"]["@value"]
        + "-"
        + item_dict["maxplaytime"]["@value"],
        "id": int(item_dict["@id"]),
    }
    type = item_dict["@type"]

    if type == BOARDGAME_TYPE:
        result.boardgames.append(item)
    elif type == EXPANSION_TYPE:
        result.expansions.append(item)


def _parse_response(resp_dict: dict) -> API_Result:
    items = resp_dict["items"]["item"]

    # parse results for item ranks based on structure
    result = API_Result()
    if isinstance(items, list):
        for item in items:
            _parse_item(item, result)
    else:
        item = items
        _parse_item(item, result)

    return result
