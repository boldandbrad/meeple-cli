from os import walk
from os.path import join, splitext
from pathlib import Path
from typing import List

import yaml

from meeple.util.fs_util import get_collection_dir

IN_PATH = get_collection_dir()
ID_LIST_KEY = "bgg-ids"


def _collection_file(collection_name: str) -> str:
    return join(IN_PATH, f"{collection_name}.yml")


def get_collections() -> List[str]:
    # create in_path dir and exit if it does not exist
    if not Path(IN_PATH).exists():
        Path(IN_PATH).mkdir(parents=True)

    # retrieve collection source files from in_path
    collection_files = next(walk(IN_PATH))[2]
    collections = []
    for collection_file in collection_files:
        collection, ext = splitext(collection_file)
        if ext == ".yml":
            collections.append(collection)
    return collections


def is_collection(name: str) -> bool:
    return name in get_collections()


def are_collections(names: [str]) -> bool:
    return set(names) <= set(get_collections())


def read_collection(name: str) -> List[int]:
    with open(_collection_file(name), "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        if data and ID_LIST_KEY in data:
            bgg_ids = data[ID_LIST_KEY]
            if not bgg_ids:
                return []

            # remove non int values from list
            for bgg_id in bgg_ids:
                if not isinstance(bgg_id, int):
                    bgg_ids.remove(bgg_id)
            return bgg_ids
        return []


def create_collection(name: str) -> None:
    data = {ID_LIST_KEY: []}
    with open(_collection_file(name), "w") as f:
        yaml.dump(data, f)


def update_collection(name: str, ids: list) -> None:
    data = {ID_LIST_KEY: ids}
    with open(_collection_file(name), "w") as f:
        yaml.dump(data, f)


def rename_collection(current_name: str, new_name: str) -> None:
    Path(_collection_file(current_name)).rename(join(IN_PATH, f"{new_name}.yml"))


def delete_collection(name: str) -> None:
    Path(_collection_file(name)).unlink()
