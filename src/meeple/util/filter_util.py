from meeple.type.item import Item


def _weight_range(weight_key: int) -> (float, float):
    match weight_key:
        case 1:
            return 1.00, 1.99
        case 2:
            return 2.00, 2.99
        case 3:
            return 3.00, 3.99
        case 4:
            return 4.00, 5.00
    return None, None


def filterby_players(item_list: [Item], players: int) -> [Item]:
    return filter(
        lambda item: int(item.minplayers) <= players
        and int(item.maxplayers) >= players,
        item_list,
    )


def filterby_playtime(item_list: [Item], max_time: int) -> [Item]:
    return filter(
        lambda item: int(item.playtime) <= max_time,
        item_list,
    )


def filterby_weight(item_list: [Item], weight_key: str) -> [Item]:
    min_weight, max_weight = _weight_range(int(weight_key))
    return filter(
        lambda item: item.weight >= min_weight and item.weight <= max_weight, item_list
    )
