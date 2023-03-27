import json
import shutil
from datetime import date
from os import makedirs, walk
from os.path import basename, exists, join, splitext

from meeple.util.fs_util import get_data_dir

OUT_PATH = get_data_dir()


def _collection_data_dir(collection_name: str) -> str:
    return join(OUT_PATH, collection_name)


def _latest_data_file(collection_name: str) -> str:
    # find latest data dump file path for collection
    data_dir = _collection_data_dir(collection_name)
    if not exists(data_dir):
        return None
    month_dirs = next(walk(data_dir))[1]
    month_dirs.sort()
    latest_month_dir = join(data_dir, month_dirs[-1])
    latest_data_files = next(walk(latest_month_dir))[2]
    latest_data_files.sort()
    return join(latest_month_dir, latest_data_files[-1])


def last_updated(collection_name: str) -> str:
    latest_data_file = _latest_data_file(collection_name)
    if not latest_data_file:
        return "NA"
    date = splitext(basename(latest_data_file))[0]
    return date


def get_data(collection_name: str) -> dict:
    data_path = _latest_data_file(collection_name)
    if not data_path:
        return None

    with open(data_path, "r") as f:
        data = json.load(f)
    # TODO: serialize json into objects instead of dict
    return data


def write_data(collection_name: str, result: dict) -> None:
    today = date.today()
    data_path = f"{_collection_data_dir(collection_name)}/{today.strftime('%Y-%m')}"
    filename = f"{today}.json"

    # create out dirs if they do not exist
    if not exists(data_path):
        makedirs(data_path)

    with open(join(data_path, filename), "w") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    print(f"\tSuccessfully updated collection '{collection_name}'.")


def delete_data(collection_name: str) -> None:
    shutil.rmtree(_collection_data_dir(collection_name))
