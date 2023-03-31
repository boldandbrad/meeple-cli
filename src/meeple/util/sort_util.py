from typing import Any

from meeple.type.item import Item


def sortby_rank(item: Item) -> Any:
    try:
        return int(item.rank)
    except ValueError:
        return float("inf")
