import json


class BGGUser:
    """BoardGameGeek User."""

    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

    def __iter__(self):
        yield from {"user_id": self.user_id, "user_name": self.user_name}.items()

    def __str__(self) -> str:
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        return self.user_id == other.user_id

    def __hash__(self):
        return hash(("id", self.user_id))

    @staticmethod
    def from_json(json_dict: dict):
        """Parse a json dict into a BGGUser.

        Args:
            json_dict (dict): dictionary to parse.

        Returns:
            BGGUser: BGGUser
        """
        return BGGUser(json_dict["user_id"], json_dict["user_name"])

    @staticmethod
    def from_bgg_dict(bgg_dict: dict):
        """Parse a BGG API dict into a BGGUser.

        Args:
            bgg_dict (dict): dictionary to parse.

        Returns:
            BGGUser: BGGUser
        """
        user_id = bgg_dict["@id"]
        user_name = bgg_dict["@name"]
        return BGGUser(user_id, user_name)
