import sys

import click

from meeple.util.api_util import get_bgg_item
from meeple.util.collection_util import (
    is_collection,
    read_collection,
    update_collection,
)
from meeple.util.output_util import print_error, print_info


@click.command()
@click.help_option("-h", "--help")
@click.argument("from_collection")
@click.argument("to_collection")
@click.argument("id")
def move(from_collection: str, to_collection: str, id: str) -> None:
    """Move a board game/extension from one collection to another.

    - FROM_COLLECTION is the name of the intended source collection.

    - TO_COLLECTION is the name of the intended destination collection.

    - ID is the BoardGameGeek ID of the board game/expansion to be moved.
    """
    # check that the given id is an integer
    if not id.isdigit():
        sys.exit(print_error("Provided ID must be an integer value"))
    bgg_id = int(id)

    # check that the given id is a valid BoardGameGeek ID
    bgg_item = get_bgg_item(bgg_id)
    if not bgg_item:
        sys.exit(print_error(f"'{bgg_id}' is not a valid BoardGameGeek ID"))

    # check that the given collection is a valid collection
    if not is_collection(from_collection):
        sys.exit(print_error(f"'{from_collection}' is not a valid collection"))

    # check that the given collection is a valid collection
    if not is_collection(to_collection):
        # TODO: offer to create the new collection
        sys.exit(print_error(f"'{to_collection}' is not a valid collection"))

    # TODO: refactor to avoid the following duplicated code
    # remove the id from the source collection
    from_bgg_ids = read_collection(from_collection)
    if bgg_id not in from_bgg_ids:
        # TODO: ask if they want to add it to the to collection anyway
        sys.exit(
            print_error(f"'{bgg_id}' already doesn't exist in '{from_collection}'")
        )

    from_bgg_ids.remove(bgg_id)

    # add the id to the destination collection
    to_bgg_ids = read_collection(to_collection)
    if to_bgg_ids and bgg_id in to_bgg_ids:
        sys.exit(print_error(f"'{bgg_id}' already exists in '{to_collection}'"))

    to_bgg_ids.append(bgg_id)
    to_bgg_ids.sort()

    # save changes
    update_collection(from_collection, from_bgg_ids)
    update_collection(to_collection, to_bgg_ids)
    print_info(f"Moved '{bgg_item.name}' from '{from_collection}' to '{to_collection}'")
