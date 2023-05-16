from os import walk
from os.path import join, splitext
from pathlib import Path
from typing import List

import yaml

from meeple.util.fs_util import get_collection_dir

COLLECTION_DIR = get_collection_dir()

_ITEM_LIST_KEY = "items"
_OLD_ITEM_LIST_KEY = "bgg-ids"  # TODO: deprecated - eventually remove
_TO_ADD_LIST_KEY = "to_add"
_TO_DROP_LIST_KEY = "to_drop"


def _collection_file(collection_name: str) -> str:
    return join(COLLECTION_DIR, f"{collection_name}.yml")


def _get_ids(data: dict, list_key: str) -> List[int]:
    if list_key in data:
        ids = data[list_key]
        if not ids:
            return []
    # remove non int values from list
    for bgg_id in ids:
        if not isinstance(bgg_id, int):
            ids.remove(bgg_id)
    return ids


def get_collections() -> List[str]:
    # create in_path dir and exit if it does not exist
    if not Path(COLLECTION_DIR).exists():
        Path(COLLECTION_DIR).mkdir(parents=True)

    # retrieve collection source files from in_path
    collection_files = next(walk(COLLECTION_DIR))[2]
    collections = []
    for collection_file in collection_files:
        collection, ext = splitext(collection_file)
        if ext == ".yml":
            collections.append(collection)
    return collections


def is_collection(name: str) -> bool:
    return name in get_collections()


def is_pending_updates(name: str) -> bool:
    _, to_add_ids, to_drop_ids = read_collection(name)
    return len(to_add_ids) > 0 or len(to_drop_ids) > 0


def are_collections(names: [str]) -> bool:
    return set(names) <= set(get_collections())


def read_collection(name: str) -> (List[int], List[int], List[int]):
    with open(_collection_file(name), "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

        # check if data is in old format
        # TODO: deprecated - eventually remove
        if data and _OLD_ITEM_LIST_KEY in data:
            bgg_ids = data[_OLD_ITEM_LIST_KEY]
            if not bgg_ids:
                return [], [], []

            # remove non int values from list
            for bgg_id in bgg_ids:
                if not isinstance(bgg_id, int):
                    bgg_ids.remove(bgg_id)
            return bgg_ids, [], []

        if data:
            return (
                _get_ids(data, _ITEM_LIST_KEY),
                _get_ids(data, _TO_ADD_LIST_KEY),
                _get_ids(data, _TO_DROP_LIST_KEY),
            )
        return [], [], []


def create_collection(name: str) -> None:
    # TODO: create a class for this Collection object
    data = {_ITEM_LIST_KEY: [], _TO_ADD_LIST_KEY: [], _TO_DROP_LIST_KEY: []}
    with open(_collection_file(name), "w") as f:
        yaml.dump(data, f)


def update_collection(
    name: str, item_ids: list, to_add_ids: list, to_drop_ids: list
) -> None:
    data = {
        _ITEM_LIST_KEY: item_ids,
        _TO_ADD_LIST_KEY: to_add_ids,
        _TO_DROP_LIST_KEY: to_drop_ids,
    }
    with open(_collection_file(name), "w") as f:
        yaml.dump(data, f)


def rename_collection(current_name: str, new_name: str) -> None:
    Path(_collection_file(current_name)).rename(join(COLLECTION_DIR, f"{new_name}.yml"))


def delete_collection(name: str) -> None:
    Path(_collection_file(name)).unlink()
