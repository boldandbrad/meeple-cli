import json
import shutil
from datetime import date
from os import rename, walk
from os.path import basename, join, splitext
from pathlib import Path
from typing import List

from meeple.type.item import Item
from meeple.util.fs_util import get_data_dir, read_json_file, write_json_file

DATA_DIR = get_data_dir()

_BOARD_GAME_LIST_KEY = "boardgames"
_EXPANSION_LIST_KEY = "expansions"


def _collection_data_dir(collection_name: str) -> str:
    return join(DATA_DIR, collection_name)


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
        rename(_collection_data_dir(current_name), join(DATA_DIR, new_name))


def last_updated(collection_name: str) -> str:
    latest_data_file = _latest_data_file(collection_name)
    if not latest_data_file:
        return "[dim]NA[/dim]"
    date = splitext(basename(latest_data_file))[0]
    return date


def get_collection_data(collection_name: str) -> (List[Item], List[Item]):
    data_path = _latest_data_file(collection_name)
    board_games, expansions = [], []
    if not data_path:
        return board_games, expansions

    # get latest collection data
    data_dict = read_json_file(data_path)

    for item_dict in data_dict[_BOARD_GAME_LIST_KEY]:
        board_games.append(
            json.loads(json.dumps(item_dict), object_hook=Item.from_json)
        )
    for item_dict in data_dict[_EXPANSION_LIST_KEY]:
        expansions.append(json.loads(json.dumps(item_dict), object_hook=Item.from_json))
    return board_games, expansions


def write_collection_data(
    collection_name: str, board_games: List[Item], expansions: List[Item]
) -> None:
    today = date.today()
    data_path = f"{_collection_data_dir(collection_name)}/{today.strftime('%Y-%m')}"
    filename = f"{today}.json"

    # create out dirs if they do not exist
    if not Path(data_path).exists():
        Path(data_path).mkdir(parents=True)

    # build data dictionary
    data_dict = {
        _BOARD_GAME_LIST_KEY: [board_game.__dict__ for board_game in board_games],
        _EXPANSION_LIST_KEY: [expansion.__dict__ for expansion in expansions],
    }

    # persist data
    write_json_file(join(data_path, filename), data_dict)


def delete_collection_data(collection_name: str) -> None:
    shutil.rmtree(_collection_data_dir(collection_name))
