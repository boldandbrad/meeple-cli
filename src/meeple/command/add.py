import sys

import click

from meeple.util.api_util import get_bgg_item
from meeple.util.collection_util import get_collection, update_collection
from meeple.util.completion_util import complete_collections
from meeple.util.fmt_util import fmt_cmd
from meeple.util.message_util import (
    info_msg,
    invalid_collection_error,
    invalid_id_error,
    under_msg,
)


@click.command()
@click.argument("collection_name", shell_complete=complete_collections)
@click.argument("bgg_ids", nargs=-1, type=int, required=True)
@click.option("--update", is_flag=True, help="Update collection data.")
@click.help_option("-h", "--help")
def add(collection_name: str, bgg_ids: [int], update: bool) -> None:
    """Add items to a collection.

    - COLLECTION_NAME is the name of the collection to be modified.

    - BGG_IDS are BoardGameGeek ID(s) of the item(s) to be added.
    """
    multi_add = len(bgg_ids) > 1

    # check that the given collection is a valid collection
    collection = get_collection(collection_name)
    if not collection:
        invalid_collection_error(collection_name)

    if multi_add:
        info_msg(f"Adding items to collection {collection.fmt_name()}...")

    num_added = 0
    for bgg_id in bgg_ids:
        # check that the given id is a valid BoardGameGeek ID
        bgg_item = get_bgg_item(bgg_id)
        if not bgg_item:
            invalid_id_error(bgg_id)

        # if the given id is slated to be dropped, simply undo that
        if bgg_id in collection.state.to_drop_ids:
            collection.state.to_drop_ids.remove(bgg_id)
            collection.state.active_ids.append(bgg_id)
            collection.state.active_ids.sort()
            num_added += 1
        # if the given id does not exist in the collection, and has not already been added, add the id
        elif (
            bgg_id not in collection.state.active_ids
            and bgg_id not in collection.state.to_add_ids
        ):
            collection.state.to_add_ids.append(bgg_id)
            collection.state.to_add_ids.sort()
            num_added += 1
        else:
            if multi_add:
                under_msg(
                    f"[dim]Skipped {bgg_item.fmt_name()}. It already exists in collection {collection.fmt_name()}.[/dim]"
                )
                continue
            else:
                info_msg(
                    f"[dim]{bgg_item.fmt_name()} already exists in collection {collection.fmt_name()}.[/dim]"
                )
                sys.exit()

        # add item message
        success_msg = (
            f"Added {bgg_item.fmt_name()} to collection {collection.fmt_name()}"
        )
        if multi_add:
            under_msg(f"{success_msg}.")
        elif update:
            info_msg(f"{success_msg} and updated collection.")
        else:
            info_msg(f"{success_msg}. To update, run: {fmt_cmd('meeple update')}")

    # persist changes
    update_collection(collection, update_data=update)

    # multi add success message
    if multi_add:
        multi_success_msg = (
            f"Added {num_added} item(s) to collection {collection.fmt_name()}"
        )
        if update:
            info_msg(f"{multi_success_msg} and updated collection.")
        else:
            info_msg(f"{multi_success_msg}. To update, run: {fmt_cmd('meeple update')}")
