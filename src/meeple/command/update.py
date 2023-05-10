import sys
from datetime import date

import click

from meeple.util.api_util import BOARDGAME_TYPE, EXPANSION_TYPE, get_bgg_items
from meeple.util.collection_util import (
    get_collections,
    is_collection,
    is_pending_updates,
    read_collection,
    update_collection,
)
from meeple.util.completion_util import complete_collections
from meeple.util.data_util import last_updated, write_collection_data
from meeple.util.output_util import print_error, print_info, printf
from meeple.util.sort_util import sort_items


@click.command()
@click.argument("collection", required=False, shell_complete=complete_collections)
@click.option("-f", "--force", is_flag=True, help="Force update.")
@click.help_option("-h", "--help")
def update(collection: str, force: bool) -> None:
    """Update local collection data.

    - COLLECTION (optional) is the name of the collection to be updated. If not provided, update all collections.
    """
    print_info("Updating local collection data...")
    # update only a specific collection, if given
    if collection:
        # check that the given collection is a valid collection
        if not is_collection(collection):
            sys.exit(
                print_error(f"[yellow]{collection}[/yellow] is not a valid collection.")
            )
        collections = [collection]
    else:
        collections = get_collections()

    # check that local collections exist
    if not collections:
        sys.exit(
            print_error(
                "No local collections yet exist. To create one, run: [green]meeple new[/green]"
            )
        )

    # update collection data
    for collection in collections:
        # read board game ids from src file
        item_ids, to_add_ids, to_drop_ids = read_collection(collection)
        if not item_ids and not to_add_ids and not to_drop_ids:
            printf(
                f" ╰╴ [yellow]Warning[/yellow]: Could not update collection [u magenta]{collection}[/u magenta] because it is empty. To add to it, run: [green]meeple add[/green]"
            )
            continue

        # skip if collection not pending updates, has been updated today, and force flag not provided
        updated = last_updated(collection)
        if (
            not force
            and not is_pending_updates(collection)
            and updated == str(date.today())
        ):
            printf(
                f" ╰╴ Skipped collection [u magenta]{collection}[/u magenta]. Already up to date."
            )
            continue

        # resolve pending updates, if any
        if to_add_ids:
            item_ids.extend(to_add_ids)
            item_ids.sort()
            to_add_ids = []
        if to_drop_ids:
            # nothing to resolve, just dump the pending update indicator
            to_drop_ids = []
        update_collection(collection, item_ids, to_add_ids, to_drop_ids)

        # get items from BoardGameGeek
        api_result = get_bgg_items(item_ids)
        boardgames = []
        expansions = []
        for item in api_result:
            item_type = item.type
            if item_type == BOARDGAME_TYPE:
                boardgames.append(item)
            if item_type == EXPANSION_TYPE:
                expansions.append(item)

        # sort board games by rank and expansions by rating
        if boardgames:
            boardgames, _ = sort_items(boardgames, "rank")
        if expansions:
            expansions, _ = sort_items(expansions, "rating")

        # save results
        update_result = {
            "boardgames": [boardgame.__dict__ for boardgame in boardgames],
            "expansions": [expansion.__dict__ for expansion in expansions],
        }
        write_collection_data(collection, update_result)
        printf(f" ╰╴ Updated collection [u magenta]{collection}[/u magenta].")

    print_info("Updated local collection data.")
