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
@click.argument("from_collection", shell_complete=complete_collections)
@click.argument("to_collection", shell_complete=complete_collections)
@click.argument("id", type=int)
@click.help_option("-h", "--help")
def move(from_collection: str, to_collection: str, id: int) -> None:
    """Move an item from one collection to another.

    - FROM_COLLECTION is the name of the intended source collection.

    - TO_COLLECTION is the name of the intended destination collection.

    - ID is the BoardGameGeek ID of the board game/expansion to be moved.
    """
    # check that the given id is a valid BoardGameGeek ID
    bgg_id = id
    bgg_item = get_bgg_item(bgg_id)
    if not bgg_item:
        sys.exit(
            print_error(f"[yellow]{bgg_id}[/yellow] is not a valid BoardGameGeek ID.")
        )

    # check that the given collection is a valid collection
    if not is_collection(from_collection):
        sys.exit(
            print_error(
                f"[yellow]{from_collection}[/yellow] is not a valid collection."
            )
        )

    from_item_ids, from_to_add_ids, from_to_drop_ids = read_collection(from_collection)

    # check that the given collection is a valid collection
    if not is_collection(to_collection):
        # TODO: offer to create the new collection
        sys.exit(
            print_error(f"[yellow]{to_collection}[/yellow] is not a valid collection.")
        )

    dest_item_ids, dest_to_add_ids, dest_to_drop_ids = read_collection(to_collection)

    # check that the id exists in from collection
    # TODO: check the from collection to_add list and to_drop list
    if bgg_id not in from_item_ids:
        # TODO: ask if they want to add it to the destination collection anyway
        sys.exit(
            print_error(
                f"[i blue]{bgg_item.name}[/i blue] already doesn't exist in [u magenta]{from_collection}[/u magenta]."
            )
        )

    # check that the id doesn't exist in dest collection
    # TODO: check the dest collection to_add list and to_drop list
    if dest_item_ids and bgg_id in dest_item_ids:
        sys.exit(
            print_error(
                f"[i blue]{bgg_item.name}[/i blue] already exists in collection [u magenta]{to_collection}[/u magenta]."
            )
        )

    # drop the id from the from collection
    from_item_ids.remove(bgg_id)
    from_to_drop_ids.append(bgg_id)
    from_to_drop_ids.sort()

    # add the id to the destination collection
    dest_to_add_ids.append(bgg_id)
    dest_to_add_ids.sort()

    # persist changes
    update_collection(from_collection, from_item_ids, from_to_add_ids, from_to_drop_ids)
    update_collection(to_collection, dest_item_ids, dest_to_add_ids, dest_to_drop_ids)
    print_info(
        f"Moved [i blue]{bgg_item.name}[/i blue] from [u magenta]{from_collection}[/u magenta] to [u magenta]{to_collection}[/u magenta]. To update, run: [green]meeple update[/green]"
    )
