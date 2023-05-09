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
        sys.exit(
            print_error(f"[yellow]{bgg_id}[/yellow] is not a valid BoardGameGeek ID.")
        )

    # check that the given collection is a valid collection
    if not is_collection(collection):
        sys.exit(
            print_error(f"[yellow]{collection}[/yellow] is not a valid collection.")
        )

    item_ids, to_add_ids, to_drop_ids = read_collection(collection)

    # check if the given id already exists in the given collection
    if (item_ids and bgg_id in item_ids) or (to_add_ids and bgg_id in to_add_ids):
        sys.exit(
            print_error(
                f"[i blue]{bgg_item.name}[/i blue] already exists in collection [u magenta]{collection}[/u magenta]."
            )
        )

    if to_drop_ids and bgg_id in to_drop_ids:
        # if the given id is slated to be dropped, simply undo that
        to_drop_ids.remove(bgg_id)
        item_ids.append(bgg_id)
        item_ids.sort()
    else:
        # otherwise, add the id to the collection as normal
        to_add_ids.append(bgg_id)
        to_add_ids.sort()

    # persist changes
    update_collection(collection, item_ids, to_add_ids, to_drop_ids)
    print_info(
        f"Added [i blue]{bgg_item.name}[/i blue]' to [u]{collection}[/u]. To update, run: [green]meeple update[/green]"
    )
