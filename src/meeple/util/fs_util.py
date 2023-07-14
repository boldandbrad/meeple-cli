import getpass
import json
import platform
import shutil
from os import walk
from os.path import join
from pathlib import Path
from typing import List

import yaml

# STATIC LOCATIONS


def _get_meeple_dir() -> str:
    meeple_root_dir = ".meeple/test"
    usrname = getpass.getuser()
    system = platform.system()
    if system == "Linux":
        return f"/home/{usrname}/{meeple_root_dir}"
    elif system == "Darwin":
        return f"/Users/{usrname}/{meeple_root_dir}"
    elif system == "Windows":
        return f"C:\\Users\\{usrname}\\{meeple_root_dir}"
    return f"{meeple_root_dir}"


MEEPLE_STATE_FILE = join(_get_meeple_dir(), "state.yml")

COLLECTIONS_DIR = join(_get_meeple_dir(), "collections")
COLLECTIONS_STATE_DIR = join(COLLECTIONS_DIR, "state")
COLLECTIONS_DATA_DIR = join(COLLECTIONS_DIR, "data")

V0_COLLECTIONS_STATE_DIR = COLLECTIONS_DIR
V0_COLLECTIONS_DATA_DIR = join(_get_meeple_dir(), "data")

ARCHIVES_DIR = join(_get_meeple_dir(), "archives")
V0_ARCHIVE_DIR = join(ARCHIVES_DIR, "v0")


def _migrate_v0_data() -> None:
    # migrate v0.x data
    # if ymls exist directly in .meeple/collections/, move them to ./meeple/collections/state/
    for file_path in next(walk(V0_COLLECTIONS_STATE_DIR))[2]:
        if file_path.endswith(".yml"):
            Path(join(V0_COLLECTIONS_STATE_DIR), file_path).rename(
                join(COLLECTIONS_STATE_DIR, file_path)
            )

    # if dirs exist in .meeple/data/, move them to .meeple/archives/v0/ and delete .meeple/data/
    if Path(V0_COLLECTIONS_DATA_DIR).exists():
        data_dirs = next(walk(V0_COLLECTIONS_DATA_DIR))[1]
        if data_dirs:
            Path(join(ARCHIVES_DIR, "v0")).mkdir(parents=True, exist_ok=True)
            for dir_path in next(walk(V0_COLLECTIONS_DATA_DIR))[1]:
                Path(join(V0_COLLECTIONS_DATA_DIR, dir_path)).rename(
                    join(ARCHIVES_DIR, "v0", dir_path)
                )
        delete_dir(V0_COLLECTIONS_DATA_DIR)
    write_yaml_file(MEEPLE_STATE_FILE, {"migrated_v0": True}, append=True)


def check_fs() -> None:
    # check that meeple root dir exists
    Path(_get_meeple_dir()).mkdir(parents=True, exist_ok=True)

    # check that collection dirs exist
    Path(COLLECTIONS_STATE_DIR).mkdir(parents=True, exist_ok=True)
    Path(COLLECTIONS_DATA_DIR).mkdir(parents=True, exist_ok=True)

    # migrate v0.x data
    meeple_state = read_yaml_file(MEEPLE_STATE_FILE)
    if "migrated_v0" not in meeple_state:
        _migrate_v0_data()


# COLLECTION FILE PATHS


def get_collection_state_file(collection_name: str) -> str:
    return join(COLLECTIONS_STATE_DIR, f"{collection_name}.yml")


def get_collection_state_files() -> List[str]:
    return next(walk(COLLECTIONS_STATE_DIR))[2]


def get_collection_data_file(collection_name: str) -> str:
    return join(COLLECTIONS_DATA_DIR, f"{collection_name}.json")


# GENERAL FILE UTILITIES


def rename_file(old_path: str, new_path: str) -> None:
    old_path = Path(old_path)
    if old_path.is_file():
        old_path.rename(new_path)


def read_json_file(file_path: str) -> dict:
    if Path(file_path).is_file():
        with open(file_path, "r") as f:
            return json.load(f)
    return {}


def write_json_file(file_path: str, data: dict) -> None:
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def read_yaml_file(file_path: str) -> dict:
    if Path(file_path).is_file():
        with open(file_path, "r") as f:
            return yaml.load(f, Loader=yaml.FullLoader)
    return {}


def write_yaml_file(file_path: str, data: dict, append: bool = False) -> None:
    mode = "a" if append else "w"
    with open(file_path, mode) as f:
        yaml.dump(data, f)


def delete_file(file_path: str) -> None:
    Path(file_path).unlink(missing_ok=True)


def delete_dir(dir_path: str) -> None:
    if Path(dir_path).exists():
        shutil.rmtree(dir_path)
