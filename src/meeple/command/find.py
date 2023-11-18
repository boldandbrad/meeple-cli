import click

from meeple.util.collection_util import (
    are_active_collections,
    get_collection,
    get_collections,
)
from meeple.util.completion_util import complete_collections
from meeple.util.filter_util import filterby_players, filterby_playtime, filterby_weight
from meeple.util.fmt_util import (
    fmt_item_type,
    fmt_players,
    fmt_playtime,
    fmt_rank,
    fmt_rating,
    fmt_weight,
    fmt_year,
)
from meeple.util.message_util import error_msg, info_msg, no_collections_exist_error
from meeple.util.output_util import TableHeader, print_table
from meeple.util.sort_util import ITEM_SORT_KEYS, sort_items


@click.command()
@click.argument("collection_names", nargs=-1, shell_complete=complete_collections)
@click.option(
    "-b",
    "--boardgames",
    "item_type",
    is_flag=True,
    flag_value="bg",
    help="Find only board games.",
)
@click.option(
    "-e",
    "--expansions",
    "item_type",
    is_flag=True,
    flag_value="ex",
    help="Find only expansions.",
)
@click.option(
    "--players",
    type=int,
    help="Find only items that support the provided player count.",
)
@click.option(
    "--max-time",
    type=int,
    help="Find only items that fit the provided play time (Min).",
)
@click.option(
    "--weight",
    type=click.Choice(["1", "2", "3", "4"]),
    help="Find only items that match the provided weight class. (Ex: 2 = 2.00-2.99)",
)
@click.option(
    "--sort",
    type=click.Choice(ITEM_SORT_KEYS, case_sensitive=False),
    default="rating",
    show_default=True,
    help="Sort items by the provided value.",
)
@click.option("-v", "--verbose", is_flag=True, help="Output additional details.")
@click.help_option("-h", "--help")
def find(
    collection_names: [str],
    item_type: str,
    players: int,
    sort: str,
    max_time: int,
    verbose: bool,
    weight: int,
) -> None:
    """Search collections for items.

    - COLLECTION_NAMES are names of the collections to query. [default: all]
    """
    # check if provided collections exist, and get them
    if collection_names:
        if not are_active_collections(collection_names):
            error_msg("Not all provided collections are valid collections.")
        collections = [get_collection(name) for name in collection_names]
    # if no collections provided, default to all local collections
    else:
        collections = get_collections()

    # check that local collections exist
    if not collections:
        no_collections_exist_error()

    # get collection items
    result_items = []
    total_unique_items = []
    collection_list = []
    for collection in collections:
        collection_list.append(collection)

        # determine what to include in results depending on given flags
        if item_type == "bg":
            result_items.extend(collection.get_board_games())
        elif item_type == "ex":
            result_items.extend(collection.get_expansions())
        else:
            result_items.extend(collection.data.items)

        total_unique_items.extend(collection.data.items)

    # remove duplicates
    result_items = list(set(result_items))
    total_unique_items = list(set(total_unique_items))

    # apply provided filters
    if players:
        result_items = filterby_players(result_items, players)
    if max_time:
        result_items = filterby_playtime(result_items, max_time)
    if weight:
        result_items = filterby_weight(result_items, weight)

    # check that data exists after applied filters
    if not result_items:
        error_msg(
            f"No items found matching provided filters for collection(s) [u magenta]{'[/u magenta], [u magenta]'.join([collection.name for collection in collections])}[/u magenta]."
        )

    # sort output
    result_items, sort_direction = sort_items(result_items, sort)

    # prepare table headers
    headers = [TableHeader.ID, TableHeader.NAME]
    # include type column if neither type is ommitted
    if item_type not in ("bg", "ex"):
        headers.append(TableHeader.TYPE)
    # include collections column if more than one collection was included
    if len(collections) > 1:
        headers.append(TableHeader.COLLECTION)
    # include additional columns if verbose flag present
    if verbose:
        headers.extend(
            [
                TableHeader.YEAR,
                TableHeader.RANK,
                TableHeader.RATING,
                TableHeader.WEIGHT,
                TableHeader.PLAYERS,
                TableHeader.TIME,
            ]
        )

    # prepare table data
    rows = []
    for item in result_items:
        cols = [str(item.id), item.name]
        # include type data if neither type is ommitted
        if item_type not in ("bg", "ex"):
            cols.append(fmt_item_type(item.type))
        # include collections data if more than one collection was included
        if len(collections) > 1:
            # determine which collections the item exists in
            containing_collections = set(
                [
                    collection.name
                    for collection in collection_list
                    if item in collection.data.items
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

    if verbose:
        info_msg(
            f"Showing {len(result_items)} of {len(total_unique_items)} unique items from collection(s) [u magenta]{'[/u magenta], [u magenta]'.join([collection.name for collection in collections])}[/u magenta]."
        )
    print_table(rows, headers, sort_key=sort, sort_direction=sort_direction)
