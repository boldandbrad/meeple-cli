def _parse_val_to_bool(integer: int) -> bool:
    return integer == "1"


def _parse_sub_dict(key_dict: dict) -> str:
    if isinstance(key_dict, list):
        key_dict = key_dict[0]
    if key_dict.get("@value"):
        return key_dict["@value"]
    elif key_dict.get("#text"):
        return key_dict["#text"]
    return None


class _BGGCollectionItemStatus:
    """BoardGameGeek Collection Item Status."""

    def __init__(
        self,
        own: bool,
        prevowned: bool,
        fortrade: bool,
        want: bool,
        wanttoplay: bool,
        wanttobuy: bool,
        wishlist: bool,
    ):
        self.own = own
        self.prevowned = prevowned
        self.fortrade = fortrade
        self.want = want
        self.wanttoplay = wanttoplay
        self.wanttobuy = wanttobuy
        self.wishlist = wishlist

    def __iter__(self):
        yield from {
            "own": self.own,
            "prevowned": self.prevowned,
            "fortrade": self.fortrade,
            "want": self.want,
            "wanttoplay": self.wanttoplay,
            "wanttobuy": self.wanttobuy,
            "wishlist": self.wishlist,
        }.items()

    def __str__(self) -> str:
        return str(dict(self))

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        if isinstance(other, _BGGCollectionItemStatus):
            return (
                self.own == other.own
                and self.prevowned == other.prevowned
                and self.fortrade == other.fortrade
                and self.want == other.want
                and self.wanttoplay == other.wanttoplay
                and self.wanttobuy == other.wanttobuy
                and self.wishlist == other.wishlist
            )
        return False

    def __hash__(self):
        return hash(("own", self.own))

    @staticmethod
    def from_bgg_dict(bgg_dict: dict):
        """Parse a BGG API dict into an _BGGCollectionItemStatus.

        Args:
            bgg_dict (dict): dictionary to parse.

        Returns:
            _BGGCollectionItemStatus: _BGGCollectionItemStatus
        """
        own = _parse_val_to_bool(bgg_dict["@own"])
        prevowned = _parse_val_to_bool(bgg_dict["@prevowned"])
        fortrade = _parse_val_to_bool(bgg_dict["@fortrade"])
        want = _parse_val_to_bool(bgg_dict["@want"])
        wanttoplay = _parse_val_to_bool(bgg_dict["@wanttoplay"])
        wanttobuy = _parse_val_to_bool(bgg_dict["@wanttobuy"])
        wishlist = _parse_val_to_bool(bgg_dict["@wishlist"])
        return _BGGCollectionItemStatus(
            own, prevowned, fortrade, want, wanttoplay, wanttobuy, wishlist
        )


class BGGCollectionItem:
    """BoardGameGeek Collection Item."""

    def __init__(self, bgg_id, name: str, status: _BGGCollectionItemStatus):
        self.bgg_id = bgg_id
        self.name = name
        self.status = status

    def __iter__(self):
        yield from {
            "bgg_id": self.bgg_id,
            "name": self.name,
            "status": self.status,
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
        status = _BGGCollectionItemStatus.from_bgg_dict(bgg_dict["status"])
        return BGGCollectionItem(bgg_id, name, status)
