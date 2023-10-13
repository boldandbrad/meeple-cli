import getpass
import json
import platform
import shutil
from pathlib import Path
from typing import List

import yaml

# STATIC LOCATIONS


def _get_meeple_dir() -> Path:
    meeple_root_dir = ".meeple"
    usrname = getpass.getuser()
    system = platform.system()
    if system == "Linux":
        return Path(f"/home/{usrname}/{meeple_root_dir}")
    elif system == "Darwin":
        return Path(f"/Users/{usrname}/{meeple_root_dir}")
    elif system == "Windows":
        return Path(f"C:\\Users\\{usrname}\\{meeple_root_dir}")
    return Path(f"{meeple_root_dir}")


MEEPLE_DIR = _get_meeple_dir()

MEEPLE_STATE_FILE = MEEPLE_DIR.joinpath("state.yml")

COLLECTIONS_DIR = MEEPLE_DIR.joinpath("collections")
COLLECTIONS_STATE_DIR = COLLECTIONS_DIR.joinpath("state")
COLLECTIONS_DATA_DIR = COLLECTIONS_DIR.joinpath("data")

V0_COLLECTIONS_STATE_DIR = COLLECTIONS_DIR
V0_COLLECTIONS_DATA_DIR = MEEPLE_DIR.joinpath("data")

ARCHIVES_DIR = MEEPLE_DIR.joinpath("archives")
V0_ARCHIVE_DIR = ARCHIVES_DIR.joinpath("v0")


def _migrate_v0_data() -> None:
    # if ymls exist directly in .meeple/collections/, move them to ./meeple/collections/state/
    for file_path in list(V0_COLLECTIONS_STATE_DIR.glob("*.yml")):
        file_path.rename(COLLECTIONS_STATE_DIR.joinpath(file_path.name))

    # if dirs exist in .meeple/data/, move them to .meeple/archives/v0/ and delete .meeple/data/
    if V0_COLLECTIONS_DATA_DIR.exists():
        V0_ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
        for dir_path in [d for d in V0_COLLECTIONS_DATA_DIR.iterdir() if d.is_dir()]:
            dir_path.rename(V0_ARCHIVE_DIR.joinpath(dir_path.name))
        delete_dir(V0_COLLECTIONS_DATA_DIR)

    # add migration indicator to state file
    write_yaml_file(MEEPLE_STATE_FILE, {"data_version": "1.0"}, append=True)


def check_fs() -> bool:
    # check that meeple root dir and state file exist
    MEEPLE_DIR.mkdir(parents=True, exist_ok=True)
    MEEPLE_STATE_FILE.touch(exist_ok=True)

    # check that collection dirs exist
    COLLECTIONS_STATE_DIR.mkdir(parents=True, exist_ok=True)
    COLLECTIONS_DATA_DIR.mkdir(parents=True, exist_ok=True)

    # migrate v0.x data
    meeple_state = read_yaml_file(MEEPLE_STATE_FILE)
    if "data_version" not in meeple_state:
        _migrate_v0_data()
        return True
    return False


# COLLECTION FILE PATHS


def get_collection_state_file(collection_name: str) -> Path:
    return COLLECTIONS_STATE_DIR.joinpath(f"{collection_name}.yml")


def get_collection_state_files() -> List[Path]:
    return list(COLLECTIONS_STATE_DIR.glob("*.yml"))


def get_collection_data_file(collection_name: str) -> Path:
    return COLLECTIONS_DATA_DIR.joinpath(f"{collection_name}.json")


# GENERAL FILE UTILITIES


def rename_file(old_path: Path, new_path: Path) -> None:
    if old_path.is_file():
        old_path.rename(new_path)


def read_json_file(file_path: Path) -> dict:
    if file_path.is_file():
        with file_path.open("r") as f:
            return json.load(f)
    return {}


def write_json_file(file_path: Path, data: dict) -> None:
    with file_path.open("w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def read_yaml_file(file_path: Path) -> dict:
    if file_path.is_file():
        with file_path.open("r") as f:
            contents = yaml.load(f, Loader=yaml.FullLoader)
            if contents:
                return contents
    return {}


def write_yaml_file(file_path: Path, data: dict, append: bool = False) -> None:
    mode = "a" if append else "w"
    with file_path.open(mode) as f:
        yaml.dump(data, f)


def delete_file(file_path: Path) -> None:
    file_path.unlink(missing_ok=True)


def delete_dir(dir_path: Path) -> None:
    if dir_path.exists():
        shutil.rmtree(dir_path)
