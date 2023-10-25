from typing import List

BGG_COLLECTION_STATUSES = [
    "own",
    "prevowned",
    "fortrade",
    "wanttoplay",
    "wanttobuy",
    "want",
    "wishlist",
]


def _parse_sub_dict(key_dict: dict) -> str:
    if isinstance(key_dict, list):
        key_dict = key_dict[0]
    if key_dict.get("@value"):
        return key_dict["@value"]
    elif key_dict.get("#text"):
        return key_dict["#text"]
    return None


class BGGCollectionItem:
    """BoardGameGeek Collection Item."""

    def __init__(self, bgg_id, name: str, statuses: List[str]):
        self.bgg_id = bgg_id
        self.name = name
        self.statuses = statuses

    def __iter__(self):
        yield from {
            "bgg_id": self.bgg_id,
            "name": self.name,
            "statuses": self.statuses,
        }.items()

    def __str__(self) -> str:
        return str(dict(self))

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        if isinstance(other, BGGCollectionItem):
            return self.bgg_id == other.bgg_id
        return False

    def __hash__(self):
        return hash(("bgg_id", self.bgg_id))

    def fmt_name(self) -> str:
        return f"[i blue]{self.name}[/i blue]"

    @staticmethod
    def from_bgg_dict(bgg_dict: dict):
        """Parse a BGG API dict into an BGGCollectionItem.

        Args:
            bgg_dict (dict): dictionary to parse.

        Returns:
            BGGCollectionItem: BGGCollectionItem
        """
        if bgg_dict.get("@objectid"):
            bgg_id = int(bgg_dict["@objectid"])
        else:
            bgg_id = None
        if bgg_dict.get("name"):
            name = _parse_sub_dict(bgg_dict["name"])
        else:
            name = None
        if bgg_dict.get("status"):
            status_dict = bgg_dict["status"]
            statuses = [
                status
                for status in BGG_COLLECTION_STATUSES
                if status_dict[f"@{status}"] == "1"
            ]
        else:
            statuses = []

        return BGGCollectionItem(bgg_id, name, statuses)
