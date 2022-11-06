import sys
from os import makedirs, walk, remove
from os.path import exists, join, splitext

import yaml

IN_PATH = "./in"


def _collection_file(collection_name: str):
    return join(IN_PATH, f"{collection_name}.yml")


def get_collections() -> list[str]:
    # create in_path dir and exit if it does not exist
    if not exists(IN_PATH):
        makedirs(IN_PATH)
        sys.exit(f"Created src directory {IN_PATH}. Add '.yaml' files to it and rerun")

    # retrieve collection source files from in_path
    collection_files = next(walk(IN_PATH))[2]
    collections = []
    for collection_file in collection_files:
        collection, ext = splitext(collection_file)
        if ext == ".yml":
            collections.append(collection)

    # quit if no valid source files are found
    if not collections:
        sys.exit("Error: no valid source files exist in the 'in' directory")
    return collections


def is_collection(name: str) -> bool:
    return name in get_collections()


def read_collection(name: str) -> "list[int]":
    with open(_collection_file(name), "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        if data and "bgg-ids" in data:
            ids = data["bgg-ids"]
            if not ids:
                return []

            # remove non int values from list
            for id in ids:
                if not isinstance(id, int):
                    ids.remove(id)
            return ids
        else:
            return []


def create_collection(name: str):
    data = {"bgg-ids": []}
    with open(_collection_file(name), "w") as f:
        yaml.dump(data, f)


def update_collection(name: str, ids: list) -> None:
    data = {"bgg-ids": ids}
    with open(_collection_file(name), "w") as f:
        yaml.dump(data, f)


def delete_collection(name: str) -> None:
    remove(_collection_file(name))
