import click

from bgg.command.get import get
from bgg.command.hot import hot
from bgg.command.open import bgg_open
from bgg.command.search import search
from bgg.command.update import update


@click.group(help="Local BoardGameGeek collection manager.")
@click.help_option("-h", "--help")
@click.version_option(
    None,  # use version auto discovery via setuptools
    "-v",
    "--version",
    package_name="bgg-cli",
    message="%(prog)s-cli, v%(version)s",
)
def cli():
    """Main 'bgg' command."""
    pass


cli.add_command(get, "get")
cli.add_command(hot, "hot")
cli.add_command(bgg_open, "open")
cli.add_command(search, "search")
cli.add_command(update, "update")

if __name__ == "__main__":
    cli()
