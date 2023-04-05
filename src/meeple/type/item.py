import json


def _grab_first(key_dict: dict) -> str:
    if isinstance(key_dict, list):
        return key_dict[0]["@value"]
    return key_dict["@value"]


def _parse_item_float_val(key_dict: dict) -> float:
    value = key_dict["@value"]
    if value != "":
        return float(value)
    return 0.0


def _parse_item_rank(ranks_dict: dict) -> str:
    if isinstance(ranks_dict, dict):
        rank = _grab_first(ranks_dict["rank"])
        if rank.isdigit():
            return rank
    return "NA"


class Item:
    def __init__(
        self,
        id,
        name,
        item_type,
        year,
        rating,
        weight,
        rank,
        minplayers,
        maxplayers,
        minplaytime,
        maxplaytime,
        minage,
    ):
        self.id = id
        self.name = name
        self.type = item_type
        self.year = year
        self.rating = rating
        self.weight = weight
        self.rank = rank
        self.minplayers = minplayers
        self.maxplayers = maxplayers
        self.minplaytime = minplaytime
        self.maxplaytime = maxplaytime
        self.minage = minage

    def __iter__(self):
        yield from {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "year": self.year,
            "rating": self.rating,
            "weight": self.weight,
            "rank": self.rank,
            "minplayers": self.minplayers,
            "maxplayers": self.maxplayers,
            "minplaytime": self.minplaytime,
            "maxplaytime": self.maxplaytime,
            "minage": self.minage,
        }.items()

    def __str__(self) -> str:
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __hash__(self):
        return hash(("id", self.id))

    @staticmethod
    def from_json(json_dict):
        return Item(
            json_dict["id"],
            json_dict["name"],
            json_dict["type"],
            json_dict["year"],
            json_dict["rating"],
            json_dict["weight"],
            json_dict["rank"],
            json_dict["minplayers"],
            json_dict["maxplayers"],
            json_dict["minplaytime"],
            json_dict["maxplaytime"],
            json_dict["minage"],
        )

    @staticmethod
    def from_bgg_dict(bgg_dict):
        rating = (
            weight
        ) = rank = minplayers = maxplayers = minplaytime = maxplaytime = minage = 0
        item_id = int(bgg_dict["@id"])
        name = _grab_first(bgg_dict["name"])
        if bgg_dict.get("@type"):
            item_type = bgg_dict["@type"]
        else:
            item_type = None
        if bgg_dict.get("yearpublished"):
            year = bgg_dict["yearpublished"]["@value"]
        else:
            year = 0
        if bgg_dict.get("statistics"):
            stats_dict = bgg_dict["statistics"]["ratings"]
            rating = round(_parse_item_float_val(stats_dict["average"]), 2)
            weight = round(_parse_item_float_val(stats_dict["averageweight"]), 2)
            rank = _parse_item_rank(stats_dict["ranks"])
        if bgg_dict.get("minplayers"):
            minplayers = bgg_dict["minplayers"]["@value"]
        if bgg_dict.get("maxplayers"):
            maxplayers = bgg_dict["maxplayers"]["@value"]
        if bgg_dict.get("minplaytime"):
            minplaytime = bgg_dict["minplaytime"]["@value"]
        if bgg_dict.get("maxplaytime"):
            maxplaytime = bgg_dict["maxplaytime"]["@value"]
        if bgg_dict.get("minage"):
            minage = bgg_dict["minage"]["@value"]
        return Item(
            item_id,
            name,
            item_type,
            year,
            rating,
            weight,
            rank,
            minplayers,
            maxplayers,
            minplaytime,
            maxplaytime,
            minage,
        )
