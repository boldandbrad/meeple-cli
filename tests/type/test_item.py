from meeple.type.item import Item
from meeple.type.item_credits import ItemCredits


def _init_item() -> Item:
    item_credits = ItemCredits(["designer"], ["artist"], ["publisher"])
    return Item(
        12345,
        "name",
        "boardgame",
        2000,
        7.50,
        2.50,
        450,
        1,
        5,
        60,
        11,
        item_credits,
        "description",
    )


def test_item():
    item = _init_item()

    # test item
    assert item.id == 12345
    assert item.name == "name"
    assert item.type == "boardgame"
    assert item.year == 2000
    assert item.rating == 7.50
    assert item.weight == 2.50
    assert item.rank == 450
    assert item.minplayers == 1
    assert item.maxplayers == 5
    assert item.playtime == 60
    assert item.minage == 11
    assert item.credits
    assert item.description == "description"

    # test item credits
    assert len(item.credits.designers) == 1 and item.credits.designers[0] == "designer"
    assert len(item.credits.artists) == 1 and item.credits.artists[0] == "artist"
    assert (
        len(item.credits.publishers) == 1 and item.credits.publishers[0] == "publisher"
    )


def test_item_repr():
    item = _init_item()
    assert item.__repr__() == "Item(12345, name, boardgame)"


def test_item_fmt_name():
    item = _init_item()
    assert item.fmt_name() == "[i blue]name[/i blue]"


def test_item_to_dict():
    item = _init_item()
    item_dict = item.to_dict()

    assert item_dict["id"] == item.id
    assert item_dict["name"] == item.name
    assert item_dict["type"] == item.type
    assert item_dict["year"] == item.year
    assert item_dict["rating"] == item.rating
    assert item_dict["weight"] == item.weight
    assert item_dict["rank"] == item.rank
    assert item_dict["minplayers"] == item.minplayers
    assert item_dict["maxplayers"] == item.maxplayers
    assert item_dict["playtime"] == item.playtime
    assert item_dict["minage"] == item.minage
    assert "credits" not in item_dict.keys()
    assert "description" not in item_dict.keys()


def test_item_from_dict():
    item_dict = _init_item().to_dict()
    item = Item.from_dict(item_dict)

    assert item_dict["id"] == item.id
    assert item_dict["name"] == item.name
    assert item_dict["type"] == item.type
    assert item_dict["year"] == item.year
    assert item_dict["rating"] == item.rating
    assert item_dict["weight"] == item.weight
    assert item_dict["rank"] == item.rank
    assert item_dict["minplayers"] == item.minplayers
    assert item_dict["maxplayers"] == item.maxplayers
    assert item_dict["playtime"] == item.playtime
    assert item_dict["minage"] == item.minage
    assert not item.credits
    assert not item.description
