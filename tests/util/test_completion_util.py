from meeple.util.completion_util import complete_collections


def test_complete_collections(mocker):
    mocker.patch(
        "meeple.util.completion_util.get_collection_names",
        return_value=["one", "two", "three"],
    )
    completions = complete_collections(None, None, "t")
    assert completions == ["two", "three"]
