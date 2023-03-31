import getpass
import platform
from os.path import join

CONFIG_DIR_NAME = ".meeple"


def _get_config_dir() -> str:
    usrname = getpass.getuser()
    if platform.system() == "Linux":
        data_dir = f"/home/{usrname}/{CONFIG_DIR_NAME}"
    elif platform.system() == "Darwin":
        data_dir = f"/Users/{usrname}/{CONFIG_DIR_NAME}"
    elif platform.system() == "Windows":
        data_dir = f"C:\\Users\\{usrname}\\{CONFIG_DIR_NAME}"
    else:
        data_dir = ""

    return data_dir


def get_collection_dir() -> str:
    return join(_get_config_dir(), "collections")


def get_data_dir() -> str:
    return join(_get_config_dir(), "data")
