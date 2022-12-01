import sys

import click

from meeple.util.collection_util import (
    is_collection,
    read_collection,
    update_collection,
)


@click.command()
@click.help_option("-h", "--help")
@click.argument("collection")
@click.argument("id")
def drop(collection: str, id: int):
    """Remove a board game/extension from a collection.

    - COLLECTION is the name of the collection to be modified.

    - ID is the BoardGameGeek ID of the board game/expansion to be removed.
    """
    # check that the given ID is an integer
    if not id.isdigit():
        sys.exit("Error: ID must be an integer value.")

    # check that the given collection is a valid collection
    if not is_collection(collection):
        sys.exit(f"Error: '{collection}' is not a valid collection.")

    bgg_ids = read_collection(collection)
    # check that the given id already does not exist in the given collection
    if int(id) not in bgg_ids:
        sys.exit(f"Error: '{id}' already doesn't exist in '{collection}'.")

    # remove the id from the collection and save
    bgg_ids.remove(int(id))
    update_collection(collection, bgg_ids)
    print(f"Successfully dropped '{id}' from '{collection}'.")
