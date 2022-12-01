import getpass
import platform
from os.path import join


def _get_config_dir():
    usrname = getpass.getuser()
    config_dir = ".meeple"
    if platform.system() == "Linux":
        data_dir = f"/home/{usrname}/{config_dir}"
    elif platform.system() == "Darwin":
        data_dir = f"/Users/{usrname}/{config_dir}"
    elif platform.system() == "Windows":
        data_dir = f"C:\\Users\\{usrname}\\{config_dir}"
    else:
        data_dir = ""

    return data_dir


def get_collection_dir():
    return join(_get_config_dir(), "collections")


def get_data_dir():
    return join(_get_config_dir(), "data")
