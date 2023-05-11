import sys

import click

from meeple.util.collection_util import is_collection
from meeple.util.completion_util import complete_collections
from meeple.util.data_util import get_collection_data
from meeple.util.output_util import (
    ItemHeader,
    fmt_headers,
    fmt_players,
    fmt_playtime,
    fmt_rank,
    fmt_rating,
    fmt_type,
    fmt_weight,
    fmt_year,
    print_error,
    print_table,
    print_warning,
)
from meeple.util.sort_util import ITEM_SORT_KEYS, sort_items


@click.command(name="list")
@click.argument("collection", shell_complete=complete_collections)
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
    "--sort",
    type=click.Choice(ITEM_SORT_KEYS, case_sensitive=False),
    default="rating",
    show_default=True,
    help="Sort output by the provided column.",
)
@click.option("-v", "--verbose", is_flag=True, help="Output additional details.")
@click.help_option("-h", "--help")
# TODO: add option to show grid lines or not in the table
def list_collection(collection: str, item_type: str, sort: str, verbose: bool) -> None:
    """List contents of a collection.

    - COLLECTION is the name of the collection to be listed.
    """
    # check that the given collection is a valid collection
    if not is_collection(collection):
        sys.exit(
            print_error(f"[yellow]{collection}[/yellow] is not a valid collection.")
        )

    boardgames, expansions = get_collection_data(collection)

    # check that local data exists for the given collection
    # TODO: add better error handling for when a collection has no data files and/or is empty?
    if not boardgames and not expansions:
        sys.exit(
            print_error(
                f"Local data not found for [u magenta]{collection}[/u magenta]. To update, run: [green]meeple update {collection}[/green]"
            )
        )

    # determine what to include in results depending on given flags
    if item_type == "bg":
        out_list = boardgames
    elif item_type == "ex":
        out_list = expansions
    else:
        out_list = boardgames + expansions

    # check that data exists after applied filters
    if not out_list:
        sys.exit(
            print_warning(
                f"No items found matching provided filters for collection [u magenta]{collection}[/u magenta]."
            )
        )

    # sort output
    out_list, sort_direction = sort_items(out_list, sort)

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
    for item in out_list:
        cols = [str(item.id), item.name]
        # include type data if neither type is ommitted
        if item_type not in ("bg", "ex"):
            cols.append(fmt_type(item.type))
        # include additional data if the user chose verbose output
        if verbose:
            cols.extend(
                [
                    fmt_year(item.year),
                    fmt_rank(str(item.rank)),
                    fmt_rating(item.rating),
                    fmt_weight(item.weight),
                    fmt_players(item.minplayers, item.maxplayers),
                    fmt_playtime(item.playtime),
                ]
            )

        rows.append(cols)

    print_table(rows, headers)
