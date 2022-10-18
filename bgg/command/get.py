import click

from bgg.util.api_util import get_items, BGG_DOMAIN


@click.command(help="Print out the details of a boardgame or expansion.")
@click.help_option("-h", "--help")
@click.argument("id")
def get(id: str):
    api_result = get_items([id])
    if not api_result:
        print("invalid id given")
    item = api_result[0]
    print(item["name"])
