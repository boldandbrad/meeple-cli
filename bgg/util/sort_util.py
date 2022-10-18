from typing import Any

from bgg.type.item import Item


def sortby_rank(x: Item) -> Any:
    try:
        return int(x["rank"])
    except ValueError:
        return float("inf")
