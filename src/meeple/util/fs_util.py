import getpass
import json
import platform
import shutil
from os import walk
from os.path import join
from pathlib import Path
from typing import List

import yaml

CONFIG_DIR_ROOT = ".meeple/test"


def _get_config_dir() -> str:
    usrname = getpass.getuser()
    system = platform.system()
    if system == "Linux":
        return f"/home/{usrname}/{CONFIG_DIR_ROOT}"
    elif system == "Darwin":
        return f"/Users/{usrname}/{CONFIG_DIR_ROOT}"
    elif system == "Windows":
        return f"C:\\Users\\{usrname}\\{CONFIG_DIR_ROOT}"
    return f"{CONFIG_DIR_ROOT}"


def get_collection_dir(create: bool = True) -> str:
    collection_dir = join(_get_config_dir(), "collections")
    # create collection_dir if it does not exist
    if create and not Path(collection_dir).exists():
        Path(collection_dir).mkdir(parents=True)
    return collection_dir


def get_data_dir(create: bool = True) -> str:
    data_dir = join(_get_config_dir(), "data")
    # create data_dir if it does not exist
    if create and not Path(data_dir).exists():
        Path(data_dir).mkdir(parents=True)
    return data_dir


def get_state_file(collection_name: str) -> str:
    return join(get_collection_dir(), f"{collection_name}.yml")


def get_state_files() -> List[str]:
    return next(walk(get_collection_dir()))[2]


def get_data_file(collection_name: str) -> str:
    return join(get_data_dir(), f"{collection_name}.json")


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


def write_yaml_file(file_path: str, data: dict) -> None:
    with open(file_path, "w") as f:
        yaml.dump(data, f)


def delete_file(file_path: str) -> None:
    if Path(file_path).is_file():
        Path(file_path).unlink()


def delete_dir(dir_path: str) -> None:
    if Path(dir_path).exists():
        shutil.rmtree(dir_path)
