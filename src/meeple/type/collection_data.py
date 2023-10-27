from typing import List

from meeple.type.item import Item
from meeple.util.fmt_util import NA_VALUE

DATA_VERSION_KEY = "version"
DATA_DATE_KEY = "date"
DATA_ITEMS_KEY = "items"


class CollectionData:
    """Collection data record."""

    def __init__(self, last_updated: str = None, items: List[Item] = []):
        self.last_updated = last_updated
        self.items = items

    def __bool__(self) -> bool:
        return self.last_updated or len(self.items) > 0

    def fmt_last_updated(self):
        if self.last_updated:
            return self.last_updated
        return NA_VALUE

    def to_dict(self) -> dict:
        return {
            DATA_VERSION_KEY: "1.0",  # TODO: make this dynamic
            DATA_DATE_KEY: self.last_updated,
            DATA_ITEMS_KEY: [item.to_dict() for item in self.items],
        }

    @staticmethod
    def from_dict(data_dict: dict):
        # TODO: handle reading v0 data formats?
        return CollectionData(
            last_updated=data_dict[DATA_DATE_KEY],
            items=[
                Item.from_dict(item_dict)
                for item_dict in data_dict[DATA_ITEMS_KEY]
                if item_dict
            ],
        )
