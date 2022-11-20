import getpass
import platform
from os.path import join


def _get_bgg_dir():
    usrname = getpass.getuser()
    bgg_dir = ".bgg"
    if platform.system() == "Linux":
        data_dir = f"/home/{usrname}/{bgg_dir}"
    elif platform.system() == "Darwin":
        data_dir = f"/Users/{usrname}/{bgg_dir}"
    elif platform.system() == "Windows":
        data_dir = f"C:\\Users\\{usrname}\\{bgg_dir}"
    else:
        data_dir = ""

    return data_dir


def get_collection_dir():
    return join(_get_bgg_dir(), "collections")


def get_data_dir():
    return join(_get_bgg_dir(), "data")
