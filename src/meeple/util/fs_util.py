import getpass
import platform
from os.path import join

CONFIG_DIR_NAME = ".meeple"


def _get_config_dir() -> str:
    usrname = getpass.getuser()
    system = platform.system()
    if system == "Linux":
        return f"/home/{usrname}/{CONFIG_DIR_NAME}"
    elif system == "Darwin":
        return f"/Users/{usrname}/{CONFIG_DIR_NAME}"
    elif system == "Windows":
        return f"C:\\Users\\{usrname}\\{CONFIG_DIR_NAME}"
    return f"{CONFIG_DIR_NAME}"


def get_collection_dir() -> str:
    return join(_get_config_dir(), "collections")


def get_data_dir() -> str:
    return join(_get_config_dir(), "data")
