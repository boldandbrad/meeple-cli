import click

from bgg.util.api_util import get_items, BOARDGAME_TYPE, EXPANSION_TYPE
from bgg.util.collection_util import get_collections, read_collection
from bgg.util.data_util import write_results
from bgg.util.sort_util import sortby_rank


@click.command(help="Update local bgg database.")
@click.help_option("-h", "--help")
def update():
    print("updating local data...")
    # process each data source file
    collections = get_collections()
    for collection in collections:
        # read board game ids from src file
        board_game_ids = read_collection(collection)
        if not board_game_ids:
            print(
                f"\tError: could not process '{collection}' because it does not contain non-empty id list 'bgg-ids' at root"
            )
            continue

        # get items from BGG
        api_result = get_items(board_game_ids)
        update_result = {"boardgames": [], "expansions": []}
        for item in api_result:
            item_type = item.type
            del item.type
            if item_type == BOARDGAME_TYPE:
                update_result["boardgames"].append(item.__dict__)
            if item_type == EXPANSION_TYPE:
                update_result["expansions"].append(item.__dict__)

        # sort boardgames by rank and expansions by rating
        if update_result["boardgames"]:
            update_result["boardgames"].sort(key=sortby_rank)
        if update_result["expansions"]:
            update_result["expansions"].sort(key=lambda x: x["rating"], reverse=True)

        write_results(collection, update_result)
