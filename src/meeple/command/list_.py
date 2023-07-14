import click

from meeple.util.collection_util import get_collection
from meeple.util.completion_util import complete_collections
from meeple.util.fmt_util import (
    fmt_headers,
    fmt_item_type,
    fmt_players,
    fmt_playtime,
    fmt_rank,
    fmt_rating,
    fmt_weight,
    fmt_year,
)
from meeple.util.message_util import (
    error_msg,
    info_msg,
    invalid_collection_error,
    warn_msg,
)
from meeple.util.sort_util import ITEM_SORT_KEYS, sort_items
from meeple.util.table_util import ItemHeader, print_table


@click.command(name="list")
@click.argument("collection_name", shell_complete=complete_collections)
@click.option(
    "-b",
    "--boardgames",
    "item_type",
    is_flag=True,
    flag_value="bg",
    help="List only board games.",
)
@click.option(
    "-e",
    "--expansions",
    "item_type",
    is_flag=True,
    flag_value="ex",
    help="List only expansions.",
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
# TODO: add option to show grid lines or not in the table
def list_(collection_name: str, item_type: str, sort: str, verbose: bool) -> None:
    """List contents of a collection.

    - COLLECTION_NAME is the name of the collection to be listed.
    """
    # check that the given collection is a valid collection
    collection = get_collection(collection_name)
    if not collection:
        invalid_collection_error(collection_name)

    # check that local data exists for the given collection
    if not collection.data.items:
        error_msg(
            f"Data not found for collection [u magenta]{collection.name}[/u magenta]. To update, run: [green]meeple update {collection.name}[/green]"
        )

    # determine what to include in results depending on given flags
    if item_type == "bg":
        result_items = collection.get_board_games()
    elif item_type == "ex":
        result_items = collection.get_expansions()
    else:
        result_items = collection.data.items

    # check that data exists after applied filters
    if not result_items:
        error_msg(
            f"No items found matching provided filters for collection [u magenta]{collection.name}[/u magenta]."
        )

    # check if the collection is pending updates
    if collection.is_pending_updates():
        warn_msg(
            f"Collection [u magenta]{collection.name}[/u magenta] has pending changes. To apply, run [green]meeple update {collection.name}[/green]"
        )

    # sort output
    result_items, sort_direction = sort_items(result_items, sort)

    # prepare table data
    headers = [ItemHeader.ID, ItemHeader.NAME]
    # include type column if neither type is ommitted
    if item_type not in ("bg", "ex"):
        headers.append(ItemHeader.TYPE)
    if verbose:
        headers.extend(
            [
                ItemHeader.YEAR,
                ItemHeader.RANK,
                ItemHeader.RATING,
                ItemHeader.WEIGHT,
                ItemHeader.PLAYERS,
                ItemHeader.TIME,
            ]
        )

    # format headers
    headers = fmt_headers(headers, sort, sort_direction)

    rows = []
    for item in result_items:
        cols = [str(item.id), item.name]
        # include type data if neither type is ommitted
        if item_type not in ("bg", "ex"):
            cols.append(fmt_item_type(item.type))
        # include additional data if the user chose verbose output
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
            f"Showing {len(result_items)} of {len(collection.data.items)} items from collection [u magenta]{collection.name}[/u magenta]."
        )
    print_table(rows, headers)
