from sys import maxsize as MAXINT

import arrow

from meeple.type.collection import Collection
from meeple.type.item import Item
from meeple.util.fmt_util import SORT_ASC_SYMBOL, SORT_DESC_SYMBOL

COLLECTION_SORT_KEYS = ["name", "boardgames", "expansions", "updated"]
ITEM_SORT_KEYS = ["rank", "rating", "weight", "year", "name", "id", "time"]


def _sort_date(date_str: str):
    if not date_str:
        return arrow.get("0001-01-01")
    return arrow.get(date_str)


def sort_collections(collection_list: [Collection], sort_key: str) -> [Collection]:
    match sort_key:
        case "name":
            return (
                sorted(collection_list, key=lambda collection: collection.name),
                SORT_ASC_SYMBOL,
            )
        case "boardgames":
            return (
                sorted(
                    collection_list,
                    key=lambda collection: len(collection.get_board_games()),
                    reverse=True,
                ),
                SORT_DESC_SYMBOL,
            )
        case "expansions":
            return (
                sorted(
                    collection_list,
                    key=lambda collection: len(collection.get_expansions()),
                    reverse=True,
                ),
                SORT_DESC_SYMBOL,
            )
    return (
        sorted(
            collection_list,
            key=lambda collection: _sort_date(collection.data.last_updated),
            reverse=True,
        ),
        SORT_DESC_SYMBOL,
    )


def _sort_rank(item: Item) -> int:
    if item.rank == 0:
        return MAXINT
    return item.rank


def sort_items(item_list: [Item], sort_key: str) -> [Item]:
    """Sort the given item list by the given key. Defaults to sort by rating.

    Args:
        item_list (Item]): list of Items.
        sort_key (str): key to sort by.

    Returns:
        [Item]: sorted list of Item.
    """
    match sort_key:
        case "rank":
            return sorted(item_list, key=_sort_rank), SORT_ASC_SYMBOL
        case "weight":
            return (
                sorted(item_list, key=lambda item: item.weight, reverse=True),
                SORT_DESC_SYMBOL,
            )
        case "year":
            return sorted(item_list, key=lambda item: item.year), SORT_ASC_SYMBOL
        case "name":
            return sorted(item_list, key=lambda item: item.name), SORT_ASC_SYMBOL
        case "id":
            return sorted(item_list, key=lambda item: int(item.id)), SORT_ASC_SYMBOL
        case "time":
            return (
                sorted(item_list, key=lambda item: int(item.playtime)),
                SORT_ASC_SYMBOL,
            )
    return (
        sorted(item_list, key=lambda item: item.rating, reverse=True),
        SORT_DESC_SYMBOL,
    )


def sort_campaigns(campaign_list: [dict], sort_key: str) -> [dict]:
    return (
        sorted(campaign_list, key=lambda campaign: _sort_date(campaign["endDate"])),
        SORT_ASC_SYMBOL,
    )
