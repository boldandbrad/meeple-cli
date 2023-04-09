import sys

import click

from meeple.type.collection import Collection
from meeple.util.collection_util import are_collections, get_collections
from meeple.util.completion_util import complete_collections
from meeple.util.data_util import get_collection_data
from meeple.util.filter_util import filterby_players, filterby_playtime, filterby_weight
from meeple.util.output_util import (
    fmt_players,
    fmt_playtime,
    fmt_rank,
    fmt_rating,
    fmt_type,
    fmt_weight,
    fmt_year,
    print_error,
    print_table,
)
from meeple.util.sort_util import ITEM_SORT_KEYS, sort_items


@click.command()
@click.argument("collections", nargs=-1, shell_complete=complete_collections)
@click.option(
    "-b",
    "--boardgames",
    "item_type",
    is_flag=True,
    flag_value="bg",
    help="Output only board games.",
)
@click.option(
    "-e",
    "--expansions",
    "item_type",
    is_flag=True,
    flag_value="ex",
    help="Output only expansions.",
)
@click.option(
    "--players",
    type=int,
    help="Output only board games/expansions that support the provided player count.",
)
@click.option(
    "--sort",
    type=click.Choice(ITEM_SORT_KEYS, case_sensitive=False),
    default="rating",
    show_default=True,
    help="Sort output by the provided column.",
)
@click.option(
    "--max-time",
    type=int,
    help="Output only board games/expansions that fit the provided play time (Min).",
)
@click.option(
    "--weight",
    type=click.Choice(["1", "2", "3", "4"]),
    help="Output only board games/expansions that match the provided relative weight. (Ex: 2 = 2.00-2.99)",
)
@click.option("-v", "--verbose", is_flag=True, help="Output additional details.")
@click.help_option("-h", "--help")
def find(
    collections: [str],
    item_type: str,
    players: int,
    sort: str,
    max_time: int,
    verbose: bool,
    weight: int,
) -> None:
    """Search collections for items.

    - COLLECTIONS are the names of a collections to query. [default: all]
    """
    # check if provided collections exist
    if not are_collections(collections):
        sys.exit(print_error("Not all provided collections are valid collections."))

    # if no collections provided, default to all local collections
    if not collections:
        collections = get_collections()

    # get collection items
    result_items = []
    collection_list = []
    for collection in collections:
        boardgames, expansions = get_collection_data(collection)
        collection_list.append(Collection(collection, boardgames, expansions, None))

        # determine what to include in results depending on given flags
        if item_type == "bg":
            result_items.extend(boardgames)
        elif item_type == "ex":
            result_items.extend(expansions)
        else:
            result_items.extend(boardgames + expansions)

    # remove duplicates
    result_items = list(set(result_items))

    # apply provided filters
    if players:
        result_items = filterby_players(result_items, players)
    if max_time:
        result_items = filterby_playtime(result_items, max_time)
    if weight:
        result_items = filterby_weight(result_items, weight)

    # sort output
    result_items = sort_items(result_items, sort)

    # prepare table headers
    headers = ["ID", "Name"]
    # include type column if neither type is ommitted
    if item_type not in ("bg", "ex"):
        headers.append("Type")
    # include collections column if more than one collection was included
    if len(collections) > 1:
        headers.append("Collection(s)")
    # include additional columns if verbose flag present
    if verbose:
        headers.extend(["Year", "Rank", "Rating", "Weight", "Players", "Play Time"])

    # prepare table data
    rows = []
    for item in result_items:
        cols = [str(item.id), item.name]
        # include type data if neither type is ommitted
        if item_type not in ("bg", "ex"):
            cols.append(fmt_type(item.type))
        # include collections data if more than one collection was included
        if len(collections) > 1:
            # determine which collections the item exists in
            containing_collections = set(
                [
                    collection.name
                    for collection in collection_list
                    if item in collection.boardgames or item in collection.expansions
                ]
            )
            cols.append(", ".join(containing_collections))
        # include additional data if verbose flag present
        if verbose:
            cols.extend(
                [
                    fmt_year(item.year),
                    fmt_rank(item.rank),
                    fmt_rating(item.rating),
                    fmt_weight(item.weight),
                    fmt_players(item.minplayers, item.maxplayers),
                    fmt_playtime(item.playtime),
                ]
            )
        rows.append(cols)

    print_table(rows, headers)
