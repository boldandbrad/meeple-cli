import json
from typing import List

from meeple.type.item import Item

DATA_VERSION_KEY = "version"
DATA_DATE_KEY = "date"
DATA_ITEMS_KEY = "items"

OLD_DATA_BG_KEY = "boardgames"  # TODO: deprecated - remove old key
OLD_DATA_EX_KEY = "expansions"  # TODO: deprecated - remove old key


class CollectionData:
    """Collection data record."""

    def __init__(self, last_updated: str = None, items: List[Item] = []):
        self.last_updated = last_updated
        self.items = items

    def __bool__(self) -> bool:
        return self.last_updated or len(self.items) > 0

    def to_dict(self) -> dict:
        return {
            DATA_VERSION_KEY: "v1.0",  # TODO: make this dynamic
            DATA_DATE_KEY: self.last_updated,
            DATA_ITEMS_KEY: [item.__dict__ for item in self.items],
        }

    @staticmethod
    def from_dict(data_dict: dict):
        # TODO: handle reading old data format
        return CollectionData(
            last_updated=data_dict[DATA_DATE_KEY],
            items=[
                json.loads(json.dumps(item_dict), object_hook=Item.from_json)
                for item_dict in data_dict[DATA_ITEMS_KEY]
            ],
        )
