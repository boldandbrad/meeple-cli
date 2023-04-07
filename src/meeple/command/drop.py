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
def drop(collection: str, id: int) -> None:
    """Remove an item from a collection.

    - COLLECTION is the name of the collection to be modified.

    - ID is the BoardGameGeek ID of the board game/expansion to be removed.
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
    # check that the given id already does not exist in the given collection
    if bgg_id not in bgg_ids:
        sys.exit(print_error(f"'{bgg_id}' already doesn't exist in '{collection}'"))

    # remove the id from the collection and save
    bgg_ids.remove(bgg_id)
    update_collection(collection, bgg_ids)
    print_info(f"Dropped '{bgg_item.name}' from '{collection}'")
