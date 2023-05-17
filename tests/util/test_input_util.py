from meeple.util.input_util import bool_input


def test_bool_input(mocker):
    mocked_ask = mocker.patch(
        "meeple.util.input_util.Confirm.ask", side_effect=[True, False]
    )

    response = bool_input("prompt")
    assert response is True
    mocked_ask.assert_called_with("prompt")

    response = bool_input("prompt")
    assert response is False
    mocked_ask.assert_called_with("prompt")
