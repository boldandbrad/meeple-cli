from meeple.type.collection import Collection
from meeple.type.collection_state import CollectionState


def test_collection():
    collection_name = "name"
    collection = Collection(collection_name)

    # test collection
    assert collection.name == collection_name
    assert len(collection.get_board_games()) == 0
    assert len(collection.get_expansions()) == 0
    assert not collection.is_pending_updates()

    # test collection state
    assert len(collection.state.active_ids) == 0
    assert len(collection.state.to_add_ids) == 0
    assert len(collection.state.to_drop_ids) == 0
    assert not collection.state
    assert isinstance(collection.state.to_dict(), dict)

    # test collection data
    assert collection.data.last_updated is None
    assert len(collection.data.items) == 0
    assert not collection.data
    assert isinstance(collection.data.to_dict(), dict)


def test_fmt_name(mocker):
    clean_collection = Collection("name")
    styled_fmt = clean_collection.fmt_name()
    assert styled_fmt == "[u magenta]name[/u magenta]"
    unstyled_fmt = clean_collection.fmt_name(styled=False)
    assert unstyled_fmt == "name"

    collection_state = CollectionState(to_add_ids=[12345])
    dirty_collection = Collection("name", state=collection_state)
    dirty_fmt = dirty_collection.fmt_name(styled=False, state=True)
    assert dirty_fmt == "name ([red]*[/red])"
