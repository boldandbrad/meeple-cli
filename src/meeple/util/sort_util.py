from meeple.type.collection import Collection
from meeple.type.item import Item

ITEM_SORT_KEYS = ["rank", "rating", "weight", "year", "name", "id", "time"]


def _handle_str_rank(item: Item):
    try:
        return int(item.rank)
    except ValueError:
        return float("inf")


def sort_collections(collection_list: [Collection], sort_key: str) -> [Collection]:
    match sort_key:
        case "name":
            return sorted(collection_list, key=lambda collection: collection.name)
        case "boardgames":
            return sorted(
                collection_list,
                key=lambda collection: len(collection.boardgames),
                reverse=True,
            )
        case "expansions":
            return sorted(
                collection_list,
                key=lambda collection: len(collection.expansions),
                reverse=True,
            )
    return sorted(
        collection_list,
        key=lambda collection: collection.last_updated,
        reverse=True,
    )


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
            return sorted(item_list, key=_handle_str_rank)
        case "weight":
            return sorted(item_list, key=lambda item: item.weight, reverse=True)
        case "year":
            return sorted(item_list, key=lambda item: item.year)
        case "name":
            return sorted(item_list, key=lambda item: item.name)
        case "id":
            return sorted(item_list, key=lambda item: int(item.id))
        case "time":
            return sorted(item_list, key=lambda item: int(item.playtime))
    return sorted(item_list, key=lambda item: item.rating, reverse=True)
