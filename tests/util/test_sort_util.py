from meeple.type.collection import Collection
from meeple.type.item import Item
from meeple.util.sort_util import sort_collections, sort_items

test_items = [
    Item(
        1234,
        "abc",
        "boardgame",
        2000,
        7.50,
        2.50,
        50,
        "2",
        "4",
        "30",
        "10",
        "description",
    ),
    Item(
        2345,
        "bcd",
        "boardgameexpansion",
        2005,
        6.50,
        2.00,
        100,
        "1",
        "5",
        "45",
        "12",
        "description",
    ),
    Item(
        3456,
        "cde",
        "boardgame",
        2010,
        5.50,
        1.50,
        0,
        "1",
        "6",
        "60",
        "14",
        "description",
    ),
]

test_items_short = [
    Item(
        3456,
        "cde",
        "boardgame",
        1995,
        5.50,
        1.50,
        500,
        "1",
        "6",
        "60",
        "14",
        "description",
    ),
]

test_collections = [
    Collection(
        "abc",
        test_items,
    ),
    Collection(
        "bcd",
        test_items_short,
    ),
]


def test_sort_collections():
    sorted_collections, _ = sort_collections(test_collections, "name")
    assert sorted_collections[0] == test_collections[0]

    sorted_collections, _ = sort_collections(test_collections, "boardgames")
    assert sorted_collections[0] == test_collections[0]

    sorted_collections, _ = sort_collections(test_collections, "expansions")
    assert sorted_collections[0] == test_collections[0]

    sorted_collections, _ = sort_collections(test_collections, "updated")
    assert sorted_collections[0] == test_collections[0]


def test_sort_items():
    sorted_items, _ = sort_items(test_items, "rank")
    assert sorted_items[0] == test_items[0]

    sorted_items, _ = sort_items(test_items, "weight")
    assert sorted_items[0] == test_items[0]

    sorted_items, _ = sort_items(test_items, "year")
    assert sorted_items[0] == test_items[0]

    sorted_items, _ = sort_items(test_items, "name")
    assert sorted_items[0] == test_items[0]

    sorted_items, _ = sort_items(test_items, "id")
    assert sorted_items[0] == test_items[0]

    sorted_items, _ = sort_items(test_items, "time")
    assert sorted_items[0] == test_items[0]

    sorted_items, _ = sort_items(test_items, "rating")
    assert sorted_items[0] == test_items[0]
