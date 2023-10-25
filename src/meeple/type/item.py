import html

from meeple.type.item_credits import ItemCredits


def _parse_sub_dict(key_dict: dict) -> str:
    if isinstance(key_dict, list):
        key_dict = key_dict[0]
    if key_dict.get("@value"):
        return key_dict["@value"]
    elif key_dict.get("#text"):
        return key_dict["#text"]
    return None


def _parse_item_float_val(key_dict: dict) -> float:
    value = key_dict["@value"]
    if value != "":
        return float(value)
    return 0.0


def _parse_item_rank(ranks_dict: dict) -> str:
    if isinstance(ranks_dict, dict):
        rank = _parse_sub_dict(ranks_dict["rank"])
        if rank.isdigit():
            return int(rank)
    return 0


class Item:
    """Board Game or Expansion."""

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
        playtime,
        minage,
        credits: ItemCredits = {},
        description: str = "",
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
        self.playtime = playtime
        self.minage = minage
        self.credits = credits
        self.description = description

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __hash__(self):
        return hash(("id", self.id))

    def __repr__(self):
        return f"Item({self.id}, {self.name}, {self.type})"

    def fmt_name(self) -> str:
        return f"[i blue]{self.name}[/i blue]"

    @staticmethod
    def from_bgg_dict(bgg_dict: dict):
        """Parse a BGG API dict into an Item.

        Args:
            bgg_dict (dict): dictionary to parse.

        Returns:
            Item: Item
        """
        rating = weight = rank = minplayers = maxplayers = playtime = minage = 0
        if bgg_dict.get("@id"):
            item_id = int(bgg_dict["@id"])
        elif bgg_dict.get("@objectid"):
            item_id = int(bgg_dict["@objectid"])
        else:
            item_id = None
        if bgg_dict.get("name"):
            name = _parse_sub_dict(bgg_dict["name"])
        else:
            name = None
        if bgg_dict.get("@type"):
            item_type = bgg_dict["@type"]
        else:
            item_type = None
        if bgg_dict.get("yearpublished"):
            year = bgg_dict["yearpublished"]["@value"]
        else:
            year = 0
        if bgg_dict.get("link"):
            credits = ItemCredits.from_bgg_dict(bgg_dict.get("link"))
        else:
            credits = {}
        if bgg_dict.get("description"):
            description = html.unescape(bgg_dict["description"]).rstrip()
        else:
            description = ""
        if bgg_dict.get("statistics"):
            stats_dict = bgg_dict["statistics"]["ratings"]
            rating = round(_parse_item_float_val(stats_dict["average"]), 2)
            weight = round(_parse_item_float_val(stats_dict["averageweight"]), 2)
            rank = _parse_item_rank(stats_dict["ranks"])
        if bgg_dict.get("minplayers"):
            minplayers = bgg_dict["minplayers"]["@value"]
        if bgg_dict.get("maxplayers"):
            maxplayers = bgg_dict["maxplayers"]["@value"]
        if bgg_dict.get("playingtime"):
            playtime = bgg_dict["playingtime"]["@value"]
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
            playtime,
            minage,
            credits,
            description,
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "year": self.year,
            "rating": self.rating,
            "weight": self.weight,
            "rank": self.rank,
            "minplayers": self.minplayers,
            "maxplayers": self.maxplayers,
            "playtime": self.playtime,
            "minage": self.minage,
        }

    @staticmethod
    def from_dict(data_dict: dict):
        """Parse a data dictionary into an Item.

        Args:
            data_dict (dict): dictionary to parse.

        Returns:
            Item: Item
        """
        return Item(
            id=data_dict["id"],
            name=data_dict["name"],
            item_type=data_dict["type"],
            year=data_dict["year"],
            rating=data_dict["rating"],
            weight=data_dict["weight"],
            rank=data_dict["rank"],
            minplayers=data_dict["minplayers"],
            maxplayers=data_dict["maxplayers"],
            playtime=data_dict["playtime"],
            minage=data_dict["minage"],
        )
