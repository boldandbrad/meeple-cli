from meeple.util.fs_util import CONFIG_DIR_ROOT, get_collection_dir, get_data_dir


def test_linux_collection_dir(mocker):
    mocker.patch("getpass.getuser", side_effect=["user"])
    mocker.patch("platform.system", side_effect=["Linux"])

    collection_dir = get_collection_dir()
    assert collection_dir == f"/home/user/{CONFIG_DIR_ROOT}/collections"


def test_mac_collection_dir(mocker):
    mocker.patch("getpass.getuser", side_effect=["user"])
    mocker.patch("platform.system", side_effect=["Darwin"])

    collection_dir = get_collection_dir()
    assert collection_dir == f"/Users/user/{CONFIG_DIR_ROOT}/collections"


def test_win_collection_dir(mocker):
    mocker.patch("getpass.getuser", side_effect=["user"])
    mocker.patch("platform.system", side_effect=["Windows"])

    collection_dir = get_collection_dir()
    assert collection_dir == f"C:\\Users\\user\\{CONFIG_DIR_ROOT}/collections"


def test_other_collection_dir(mocker):
    mocker.patch("getpass.getuser", side_effect=["user"])
    mocker.patch("platform.system", side_effect=["other"])

    collection_dir = get_collection_dir()
    assert collection_dir == f"{CONFIG_DIR_ROOT}/collections"


def test_linux_data_dir(mocker):
    mocker.patch("getpass.getuser", side_effect=["user"])
    mocker.patch("platform.system", side_effect=["Linux"])

    collection_dir = get_data_dir()
    assert collection_dir == f"/home/user/{CONFIG_DIR_ROOT}/data"


def test_mac_data_dir(mocker):
    mocker.patch("getpass.getuser", side_effect=["user"])
    mocker.patch("platform.system", side_effect=["Darwin"])

    collection_dir = get_data_dir()
    assert collection_dir == f"/Users/user/{CONFIG_DIR_ROOT}/data"


def test_win_data_dir(mocker):
    mocker.patch("getpass.getuser", side_effect=["user"])
    mocker.patch("platform.system", side_effect=["Windows"])

    collection_dir = get_data_dir()
    assert collection_dir == f"C:\\Users\\user\\{CONFIG_DIR_ROOT}/data"


def test_other_data_dir(mocker):
    mocker.patch("getpass.getuser", side_effect=["user"])
    mocker.patch("platform.system", side_effect=["other"])

    collection_dir = get_data_dir()
    assert collection_dir == f"{CONFIG_DIR_ROOT}/data"
