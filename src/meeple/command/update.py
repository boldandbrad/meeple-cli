import sys

import click

from meeple.util.api_util import BOARDGAME_TYPE, EXPANSION_TYPE, get_items
from meeple.util.collection_util import get_collections, is_collection, read_collection
from meeple.util.data_util import write_data
from meeple.util.sort_util import sortby_rank


@click.command()
@click.help_option("-h", "--help")
@click.argument("collection", required=False)
def update(collection: str):
    """Update local collection data.

    - COLLECTION (optional) is the name of the collection to be updated. If not provided, update all collections.
    """
    print("Updating local data...")
    # update only a specific collection, if given
    if collection:
        # check that the given collection is a valid collection
        if not is_collection(collection):
            sys.exit(f"Error: '{collection}' is not a valid collection.")
        collections = [collection]
    else:
        collections = get_collections()

    # check that local collections exist
    if not collections:
        sys.exit(
            "Warning: No local collections yet exist. Create a new one with `meeple new`"
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
        api_result = get_items(board_game_ids)
        update_result = {"boardgames": [], "expansions": []}
        for item in api_result:
            item_type = item.type
            del item.type
            if item_type == BOARDGAME_TYPE:
                update_result["boardgames"].append(item.__dict__)
            if item_type == EXPANSION_TYPE:
                update_result["expansions"].append(item.__dict__)

        # sort board games by rank and expansions by rating
        if update_result["boardgames"]:
            update_result["boardgames"].sort(key=sortby_rank)
        if update_result["expansions"]:
            update_result["expansions"].sort(key=lambda x: x["rating"], reverse=True)

        # save results
        write_data(collection, update_result)

    print("Successfully updated local data.")
