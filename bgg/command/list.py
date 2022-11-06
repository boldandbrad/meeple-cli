import click

from bgg.util.collection_util import is_collection, read_collection
from bgg.util.api_util import get_items


@click.command(help="List all games/extensions in a collection.")
@click.help_option("-h", "--help")
@click.argument("collection")
# TODO: add options to list only games or only expansions
def list_collection(collection: str):
    if not is_collection(collection):
        print(f"{collection} is not a valid collection")
        return

    bgg_ids = read_collection(collection)
    if not bgg_ids:
        print(f"{collection} is empty.")
        return

    items = get_items(bgg_ids)
    for item in items:
        print(f"{item.id}\t{item.name}")
