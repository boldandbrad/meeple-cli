from typing import Any


def _grab_first(key_dict: dict) -> str:
    if isinstance(key_dict, list):
        return key_dict[0]["@value"]
    return key_dict["@value"]


def _parse_item_float_val(key_dict: dict) -> Any:
    value = key_dict["@value"]
    if value != "":
        return float(value)
    return 0.0


def _parse_item_rank(ranks_dict: dict) -> Any:
    if isinstance(ranks_dict, dict):
        rank = _grab_first(ranks_dict["rank"])
        if rank.isdigit():
            return rank
    return "NA"


class Item:
    def __init__(self, item_dict: dict):
        self.id = int(item_dict["@id"])
        self.name = _grab_first(item_dict["name"])
        if item_dict.get("@type"):
            self.type = item_dict["@type"]
        if item_dict.get("yearpublished"):
            self.year = item_dict["yearpublished"]["@value"]
        if item_dict.get("statistics"):
            stats_dict = item_dict["statistics"]["ratings"]
            self.rating = round(_parse_item_float_val(stats_dict["average"]), 2)
            self.weight = round(_parse_item_float_val(stats_dict["averageweight"]), 2)
            self.rank = _parse_item_rank(stats_dict["ranks"])
        if item_dict.get("minplayers"):
            self.minplayers = item_dict["minplayers"]["@value"]
        if item_dict.get("maxplayers"):
            self.maxplayers = item_dict["maxplayers"]["@value"]
        if item_dict.get("minplaytime"):
            self.minplaytime = item_dict["minplaytime"]["@value"]
        if item_dict.get("maxplaytime"):
            self.maxplaytime = item_dict["maxplaytime"]["@value"]
