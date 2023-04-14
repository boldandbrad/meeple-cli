from meeple.util.input_util import bool_input


def test_yes_bool_input(mocker):
    responses = ["y", "Y", "yes", "YES", "yES"]
    mocker.patch("builtins.input", side_effect=responses)

    for i in range(len(responses)):
        bool_output = bool_input("prompt")
        assert bool_output is True


def test_no_bool_input(mocker):
    responses = ["n", "N", "no", "NO", "No", "x", "1"]
    mocker.patch("builtins.input", side_effect=responses)

    for i in range(len(responses)):
        bool_output = bool_input("prompt")
        assert bool_output is False
