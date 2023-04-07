import sys

import click

from meeple.util.api_util import BOARDGAME_TYPE, EXPANSION_TYPE, get_bgg_items
from meeple.util.collection_util import get_collections, is_collection, read_collection
from meeple.util.completion_util import complete_collections
from meeple.util.data_util import write_collection_data
from meeple.util.output_util import print_error, print_info, print_warning
from meeple.util.sort_util import sort_items


@click.command()
@click.argument("collection", required=False, shell_complete=complete_collections)
@click.help_option("-h", "--help")
def update(collection: str) -> None:
    """Update local collection data.

    - COLLECTION (optional) is the name of the collection to be updated. If not provided, update all collections.
    """
    print_info("Updating local data...")
    # update only a specific collection, if given
    if collection:
        # check that the given collection is a valid collection
        if not is_collection(collection):
            sys.exit(print_error(f"'{collection}' is not a valid collection"))
        collections = [collection]
    else:
        collections = get_collections()

    # check that local collections exist
    if not collections:
        sys.exit(
            print_warning(
                "No local collections yet exist. Create a new one with `meeple new`"
            )
        )

    # update collection data
    for collection in collections:
        # read board game ids from src file
        board_game_ids = read_collection(collection)
        if not board_game_ids:
            print(
                f"\tWarning: Could not update collection '{collection}' because it is empty. Add to it with `meeple add`"
            )
            continue

        # get items from BoardGameGeek
        api_result = get_bgg_items(board_game_ids)
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
            boardgames = sort_items(boardgames, "rank")
        if expansions:
            expansions = sort_items(expansions, "rating")

        # save results
        update_result = {
            "boardgames": [boardgame.__dict__ for boardgame in boardgames],
            "expansions": [expansion.__dict__ for expansion in expansions],
        }
        write_collection_data(collection, update_result)

    print_info("Updated local data")
