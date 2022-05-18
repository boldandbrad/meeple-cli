import os

from click.testing import CliRunner

from bgg.bgg import cli


def test_makey():
    if "TRAVIS" not in os.environ:
        runner = CliRunner()
        result = runner.invoke(cli, [])
        assert result.exit_code == 0
