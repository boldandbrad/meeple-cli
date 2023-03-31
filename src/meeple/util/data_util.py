import json
import shutil
from datetime import date
from os import rename, walk
from os.path import basename, join, splitext
from pathlib import Path
from typing import List

from meeple.type.item import Item
from meeple.util.fs_util import get_data_dir

OUT_PATH = get_data_dir()


def _collection_data_dir(collection_name: str) -> str:
    return join(OUT_PATH, collection_name)


def _latest_data_file(collection_name: str) -> str:
    # find latest data dump file path for collection
    data_dir = _collection_data_dir(collection_name)
    if not Path(data_dir).exists():
        return None
    month_dirs = next(walk(data_dir))[1]
    month_dirs.sort()
    latest_month_dir = join(data_dir, month_dirs[-1])
    latest_data_files = next(walk(latest_month_dir))[2]
    latest_data_files.sort()
    return join(latest_month_dir, latest_data_files[-1])


def rename_collection_data_dir(current_name: str, new_name: str) -> None:
    if Path(_collection_data_dir(current_name)).exists():
        rename(_collection_data_dir(current_name), join(OUT_PATH, new_name))


def last_updated(collection_name: str) -> str:
    latest_data_file = _latest_data_file(collection_name)
    if not latest_data_file:
        return "NA"
    date = splitext(basename(latest_data_file))[0]
    return date


def get_collection_data(collection_name: str) -> (List[Item], List[Item]):
    data_path = _latest_data_file(collection_name)
    boardgames = []
    expansions = []
    if not data_path:
        return boardgames, expansions

    with open(data_path, "r") as f:
        data = json.load(f)

    for dict_item in data["boardgames"]:
        item = json.loads(json.dumps(dict_item), object_hook=Item.from_json)
        boardgames.append(item)
    for dict_item in data["expansions"]:
        item = json.loads(json.dumps(dict_item), object_hook=Item.from_json)
        expansions.append(item)
    return boardgames, expansions


def write_collection_data(collection_name: str, result: dict) -> None:
    today = date.today()
    data_path = f"{_collection_data_dir(collection_name)}/{today.strftime('%Y-%m')}"
    filename = f"{today}.json"

    # create out dirs if they do not exist
    if not Path(data_path).exists():
        Path(data_path).mkdir(parents=True)

    with open(join(data_path, filename), "w") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    # TODO: find a more elegant way to print this out
    print(f"\tUpdated collection '{collection_name}'.")


def delete_collection_data(collection_name: str) -> None:
    shutil.rmtree(_collection_data_dir(collection_name))
