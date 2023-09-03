import re
from datetime import date
from typing import List

from meeple.type.collection import Collection
from meeple.type.collection_data import CollectionData
from meeple.type.collection_state import CollectionState
from meeple.util.api_util import get_bgg_items
from meeple.util.fs_util import (
    delete_file,
    get_collection_data_file,
    get_collection_state_file,
    get_collection_state_files,
    read_json_file,
    read_yaml_file,
    rename_file,
    write_json_file,
    write_yaml_file,
)
from meeple.util.sort_util import sort_items


def is_active_collection(collection_name: str) -> bool:
    return collection_name in get_collection_names()


def are_active_collections(collection_names: [str]) -> bool:
    return set(collection_names) <= set(get_collection_names())


def get_collection_names() -> List[str]:
    return [f.stem for f in get_collection_state_files()]


def get_collection(collection_name: str) -> Collection:
    # check that the collection exists
    if not is_active_collection(collection_name):
        return None

    # get collection state
    state_dict = read_yaml_file(get_collection_state_file(collection_name))
    state = CollectionState.from_dict(state_dict)

    # get collection data
    data_file = get_collection_data_file(collection_name)
    data_dict = read_json_file(data_file)
    if data_dict:
        data = CollectionData.from_dict(data_dict)
    else:
        data = CollectionData()
        write_json_file(data_file, data.to_dict())

    return Collection(collection_name, state=state, data=data)


def get_collections() -> List[Collection]:
    return [get_collection(n) for n in get_collection_names()]


def create_collection(collection_name: str, to_add_ids: List[int] = []) -> None:
    collection = Collection(collection_name)
    if to_add_ids:
        collection.state.to_add_ids = to_add_ids
    write_yaml_file(
        get_collection_state_file(collection.name), collection.state.to_dict()
    )
    write_json_file(
        get_collection_data_file(collection.name), collection.data.to_dict()
    )


def update_collection(collection: Collection, update_data: bool = False) -> None:
    # update collection state and return, if not updating collection data
    if not update_data:
        write_yaml_file(
            get_collection_state_file(collection.name), collection.state.to_dict()
        )
        return

    # resolve pending state adds
    if collection.state.to_add_ids:
        collection.state.active_ids.extend(collection.state.to_add_ids)
        collection.state.active_ids.sort()
        collection.state.to_add_ids = []
    # resolve pending state drops. (just dump the pending update indicator)
    if collection.state.to_drop_ids:
        collection.state.to_drop_ids = []

    # update collection state
    write_yaml_file(
        get_collection_state_file(collection.name), collection.state.to_dict()
    )

    # update collection data from BoardGameGeek
    collection.data.items = get_bgg_items(collection.state.active_ids)
    sort_items(collection.data.items, "id")
    collection.data.last_updated = str(date.today())
    write_json_file(
        get_collection_data_file(collection.name), collection.data.to_dict()
    )


def rename_collection(collection: Collection, new_name: str) -> None:
    # rename collection state file
    rename_file(
        get_collection_state_file(collection.name), get_collection_state_file(new_name)
    )
    # rename collection data file
    rename_file(
        get_collection_data_file(collection.name), get_collection_data_file(new_name)
    )


def delete_collection(collection: Collection) -> None:
    # delete collection state file
    delete_file(get_collection_state_file(collection.name))
    # delete collection data file
    delete_file(get_collection_data_file(collection.name))


def unique_collection_name(collection_name: str) -> str:
    first_iteration = True
    while is_active_collection(collection_name):
        if first_iteration:
            collection_name += "-1"
            first_iteration = False
            continue
        collection_name = re.sub(
            r"[0-9]+$",
            lambda x: f"{str(int(x.group())+1).zfill(len(x.group()))}",
            collection_name,
        )
    return collection_name
