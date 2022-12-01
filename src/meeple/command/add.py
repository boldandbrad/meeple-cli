import sys

import click

from meeple.util.api_util import get_items
from meeple.util.collection_util import (
    is_collection,
    read_collection,
    update_collection,
)


@click.command()
@click.help_option("-h", "--help")
@click.argument("collection")
@click.argument("id")
def add(collection: str, id: int):
    """Add a board game/extension to a collection.

    - COLLECTION is the name of the intended destination collection.

    - ID is the BoardGameGeek ID of the board game/expansion to be added.
    """
    # check that the given id is an integer
    if not id.isdigit():
        sys.exit("Error: ID must be an integer value.")

    # check that the given id is a valid BoardGameGeek ID
    api_result = get_items([id])
    if not api_result:
        sys.exit(f"Error: '{id}' is not a valid BoardGameGeek ID.")

    # check that the given collection is a valid collection
    if not is_collection(collection):
        sys.exit(f"Error: '{collection}' is not a valid collection.")

    bgg_ids = read_collection(collection)
    # check that the given id does not already exist in the given collection
    if bgg_ids and int(id) in bgg_ids:
        sys.exit(f"Error: '{id}' already exists in '{collection}'.")

    # add the id to the collection and save
    bgg_ids.append(int(id))
    bgg_ids.sort()
    update_collection(collection, bgg_ids)
    print(f"Successfully added '{id}' to '{collection}'.")
