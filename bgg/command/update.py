import click

from bgg.util.api_util import get_items, API_Result
from bgg.util.fs_util import get_sources, read_source, write_results
from bgg.util.sort_util import sortby_rank


@click.command(help="Update local bgg database.")
@click.help_option("-h", "--help")
def update():
    print("updating...")
    # process each data source file
    sources = get_sources()
    for src in sources:
        # read board game ids from src file
        board_game_ids = read_source(src)
        if not board_game_ids:
            print(
                f"\tError: could not process '{src}' because it does not contain non-empty id list 'bgg-ids' at root"
            )
            continue

        # get items from BGG
        api_result = get_items(board_game_ids)

        # sort boardgames by rank and expansions by rating
        if api_result.boardgames:
            api_result.boardgames.sort(key=sortby_rank)
        if api_result.expansions:
            api_result.expansions.sort(key=lambda x: x["rating"], reverse=True)

        write_results(src, api_result)
