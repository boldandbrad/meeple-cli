import click

from bgg.util.api_util import get_hot


@click.command(help="Retrieve the current bgg hotness list.")
@click.help_option("-h", "--help")
def hot():
    api_result = get_hot()
    for item in api_result:
        print(f"{item.id}\t{item.name}")
