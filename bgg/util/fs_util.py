import json
import sys
from datetime import date
from os import makedirs, walk
from os.path import exists, join, splitext

import yaml


IN_PATH = "./in"
OUT_PATH = "./out"


def get_sources() -> list[str]:
    # create in_path dir and exit if it does not exist
    if not exists(IN_PATH):
        makedirs(IN_PATH)
        sys.exit(f"Created src directory {IN_PATH}. Add '.yaml' files to it and rerun")

    # retrieve data source files from in_path
    sources = next(walk(IN_PATH))[2]
    for src in sources:
        ext = splitext(src)[1]
        if ext != ".yaml" and ext != ".yml":
            print(f"Error: could not process '{src}' because it is not a .yaml file")
            sources.remove(src)

    # quit if no valid source files are found
    if not sources:
        sys.exit("Error: no valid source files exist in the 'in' directory")
    return sources


def read_source(src: str) -> "list[int]":
    with open(join(IN_PATH, src), "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        if data and "bgg-ids" in data:
            ids = data["bgg-ids"]
            if not ids:
                return None

            # remove non int values from list
            for id in ids:
                if not isinstance(id, int):
                    ids.remove(id)
            return ids
        else:
            return None


def write_results(src: str, result: dict) -> None:
    src_name = splitext(src)[0]

    today = date.today()
    path = f"{OUT_PATH}/{src_name}/{today.strftime('%Y-%m')}"
    filename = f"{today}.json"

    # create out dirs if they do not exist
    if not exists(path):
        makedirs(path)

    with open(join(path, filename), "w") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    print(f"{src_name} results successfully written to {path}/{filename}")
