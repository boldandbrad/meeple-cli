from pathlib import Path

from meeple.util.collection_util import (
    are_active_collections,
    get_collection_names,
    is_active_collection,
    unique_collection_name,
)


def test_is_active_collection(mocker):
    mocker.patch(
        "meeple.util.collection_util.get_collection_names",
        side_effect=[["one", "two"], ["one", "two"]],
    )
    assert is_active_collection("one")
    assert not is_active_collection("three")


def test_are_active_collections(mocker):
    mocker.patch(
        "meeple.util.collection_util.get_collection_names",
        side_effect=[["one", "two"], ["three", "four"]],
    )
    assert are_active_collections(["one", "two"])
    assert not are_active_collections(["one", "two"])


def test_get_collection_names(mocker):
    mocker.patch(
        "meeple.util.collection_util.get_collection_state_files",
        side_effect=[[Path("one.yml"), Path("two.yml")]],
    )
    collection_names = get_collection_names()
    assert collection_names == ["one", "two"]


def test_unique_collection_name(mocker):
    mocker.patch(
        "meeple.util.collection_util.is_active_collection",
        side_effect=[True, True, False],
    )

    assert unique_collection_name("name") == "name-2"
