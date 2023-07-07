from meeple.type.item import Item
from meeple.util.filter_util import filterby_players, filterby_playtime, filterby_weight

test_items = [
    Item(
        1234,
        "abc",
        "boardgame",
        2000,
        "7.50",
        4.50,
        "50",
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
        "6.50",
        3.50,
        "100",
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
        "5.50",
        2.50,
        "Not Ranked",
        "1",
        "6",
        "60",
        "14",
        "description",
    ),
    Item(
        4567,
        "def",
        "boardgame",
        2015,
        "5.50",
        1.50,
        "Not Ranked",
        "1",
        "7",
        "60",
        "14",
        "description",
    ),
]


def test_filterby_players():
    filtered_items = filterby_players(test_items, 7)
    assert len(filtered_items) == 1
    assert filtered_items[0] == test_items[3]


def test_filterby_playtime():
    filtered_items = filterby_playtime(test_items, 30)
    assert len(filtered_items) == 1
    assert filtered_items[0] == test_items[0]


def test_filterby_weight():
    filtered_items = filterby_weight(test_items, 1)
    assert len(filtered_items) == 1
    assert filtered_items[0] == test_items[3]

    filtered_items = filterby_weight(test_items, 2)
    assert len(filtered_items) == 1
    assert filtered_items[0] == test_items[2]

    filtered_items = filterby_weight(test_items, 3)
    assert len(filtered_items) == 1
    assert filtered_items[0] == test_items[1]

    filtered_items = filterby_weight(test_items, 4)
    assert len(filtered_items) == 1
    assert filtered_items[0] == test_items[0]
