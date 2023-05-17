import getpass
import json
import platform
from os.path import join

import yaml

CONFIG_DIR_ROOT = ".meeple"


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


def get_collection_dir() -> str:
    return join(_get_config_dir(), "collections")


def get_data_dir() -> str:
    return join(_get_config_dir(), "data")


def read_json_file(file_path: str) -> dict:
    with open(file_path, "r") as f:
        return json.load(f)


def write_json_file(file_path: str, data: dict) -> None:
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def read_yaml_file(file_path: str) -> dict:
    with open(file_path, "r") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def write_yaml_file(file_path: str, data: dict) -> None:
    with open(file_path, "w") as f:
        yaml.dump(data, f)
