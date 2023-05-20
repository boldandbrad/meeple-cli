from datetime import date
from typing import List

import click

from meeple.util.api_util import BOARDGAME_TYPE, EXPANSION_TYPE, get_bgg_items
from meeple.util.collection_util import (
    get_collection_names,
    is_collection,
    is_pending_updates,
    read_collection,
    update_collection,
)
from meeple.util.completion_util import complete_collections
from meeple.util.data_util import last_updated, write_collection_data
from meeple.util.message_util import (
    error_msg,
    info_msg,
    invalid_collection_error,
    no_collections_exist_error,
    under_msg,
)
from meeple.util.sort_util import sort_items


def _update_collection(collection_name: str, item_ids, to_add_ids, to_drop_ids) -> None:
    # resolve pending updates, if any
    if to_add_ids:
        item_ids.extend(to_add_ids)
        item_ids.sort()
        to_add_ids = []
    if to_drop_ids:
        # nothing to resolve, just dump the pending update indicator
        to_drop_ids = []
    update_collection(collection_name, item_ids, to_add_ids, to_drop_ids)

    # get items from BoardGameGeek
    api_result = get_bgg_items(item_ids)
    board_games, expansions = [], []
    for item in api_result:
        item_type = item.type
        if item_type == BOARDGAME_TYPE:
            board_games.append(item)
        if item_type == EXPANSION_TYPE:
            expansions.append(item)

    # sort board games by rank and expansions by rating
    if board_games:
        board_games, _ = sort_items(board_games, "rank")
    if expansions:
        expansions, _ = sort_items(expansions, "rating")

    # persist results
    write_collection_data(collection_name, board_games, expansions)


@click.command()
@click.argument(
    "collections", nargs=-1, required=False, shell_complete=complete_collections
)
@click.option("-f", "--force", is_flag=True, help="Force update.")
@click.help_option("-h", "--help")
def update(collections: List[str], force: bool) -> None:
    """Update collection data.

    - COLLECTIONS (optional) are names of collections to update. [default: all]
    """
    # update the given collection(s). otherwise, attempt to update all
    if not collections:
        collections = get_collection_names()

    # check that local collections exist
    if not collections:
        no_collections_exist_error()

    if len(collections) > 1:
        info_msg("Updating collection data...")

        # update collection data
        for collection in collections:
            # check if collection exists
            if not is_collection(collection):
                under_msg(
                    f"[dim]Skipped collection [u magenta]{collection}[/u magenta]. It does not exist.[/dim]"
                )
                continue
            # get collection item ids
            item_ids, to_add_ids, to_drop_ids = read_collection(collection)

            # print warning and skip if collection is empty
            if not item_ids and not to_add_ids and not to_drop_ids:
                under_msg(
                    f"[yellow]Warning[/yellow]: Could not update collection [u magenta]{collection}[/u magenta] because it is empty. To add to it, run: [green]meeple add[/green]"
                )
                continue

            # skip if collection not pending updates, has been updated today, and force flag not provided
            updated = last_updated(collection)
            if (
                not force
                and not is_pending_updates(collection)
                and updated == str(date.today())
            ):
                under_msg(
                    f"[dim]Skipped collection [u magenta]{collection}[/u magenta]. Already up to date.[/dim]"
                )
                continue

            _update_collection(collection, item_ids, to_add_ids, to_drop_ids)
            under_msg(f"Updated collection [u magenta]{collection}[/u magenta].")

        info_msg("Updated collection data.")

    else:
        collection = collections[0]
        # check if collection exists
        if not is_collection(collection):
            invalid_collection_error(collection)

        # get collection item ids
        item_ids, to_add_ids, to_drop_ids = read_collection(collection)

        # if collection is empty
        if not item_ids and not to_add_ids and not to_drop_ids:
            error_msg(
                f"Could not update collection [u magenta]{collection}[/u magenta] because it is empty. To add to it, run: [green]meeple add[/green]"
            )

        # skip if collection not pending updates, has been updated today, and force flag not provided
        updated = last_updated(collection)
        if (
            not force
            and not is_pending_updates(collection)
            and updated == str(date.today())
        ):
            error_msg(
                f"Could not update collection [u magenta]{collection}[/u magenta]. Already up to date."
            )

        _update_collection(collection, item_ids, to_add_ids, to_drop_ids)
        info_msg(f"Updated collection [u magenta]{collection}[/u magenta].")
