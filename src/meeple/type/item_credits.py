from typing import List


class ItemCredits:
    """Item credits record."""

    def __init__(
        self,
        designers: List[int] = [],
        artists: List[int] = [],
        publishers: List[int] = [],
    ):
        self.designers = designers
        self.artists = artists
        self.publishers = publishers

    @staticmethod
    def from_bgg_dict(link_dicts: dict):
        return ItemCredits(
            designers=[
                link["@value"]
                for link in link_dicts
                if link["@type"] == "boardgamedesigner"
            ],
            artists=[
                link["@value"]
                for link in link_dicts
                if link["@type"] == "boardgameartist"
            ],
            publishers=[
                link["@value"]
                for link in link_dicts
                if link["@type"] == "boardgamepublisher"
            ],
        )

    def to_dict(self) -> dict:
        return {
            "designers": self.designers,
            "artists": self.artists,
            "publishers": self.publishers,
        }

    @staticmethod
    def from_dict(credits_dict: dict):
        return ItemCredits(
            designers=credits_dict["designers"],
            artists=credits_dict["artists"],
            publishers=credits_dict["publishers"],
        )
