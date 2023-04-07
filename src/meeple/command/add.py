import sys

import click

from meeple.util.api_util import get_bgg_item
from meeple.util.collection_util import (
    is_collection,
    read_collection,
    update_collection,
)
from meeple.util.completion_util import complete_collections
from meeple.util.output_util import print_error, print_info


@click.command()
@click.argument("collection", shell_complete=complete_collections)
@click.argument("id", type=int)
@click.help_option("-h", "--help")
def add(collection: str, id: int) -> None:
    """Add an item to a collection.

    - COLLECTION is the name of the intended destination collection.

    - ID is the BoardGameGeek ID of the board game/expansion to be added.
    """
    # check that the given id is a valid BoardGameGeek ID
    bgg_id = id
    bgg_item = get_bgg_item(bgg_id)
    if not bgg_item:
        sys.exit(print_error(f"'{bgg_id}' is not a valid BoardGameGeek ID"))

    # check that the given collection is a valid collection
    if not is_collection(collection):
        sys.exit(print_error(f"'{collection}' is not a valid collection"))

    bgg_ids = read_collection(collection)
    # check that the given id does not already exist in the given collection
    if bgg_ids and bgg_id in bgg_ids:
        sys.exit(print_error(f"'{bgg_id}' already exists in '{collection}'"))

    # add the id to the collection and save
    bgg_ids.append(bgg_id)
    bgg_ids.sort()
    update_collection(collection, bgg_ids)
    print_info(f"Added '{bgg_item.name}' to '{collection}'")
