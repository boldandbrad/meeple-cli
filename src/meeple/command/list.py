import sys

import click

from meeple.util.collection_util import is_collection
from meeple.util.data_util import get_collection_data
from meeple.util.output_util import (
    fmt_players,
    fmt_playtime,
    fmt_rating,
    fmt_weight,
    print_error,
    print_table,
    print_warning,
)


@click.command()
@click.help_option("-h", "--help")
@click.argument("collection")
@click.option(
    "-b",
    "--boardgames",
    "only_include",
    is_flag=True,
    flag_value="bg",
    help="Include only board games in output.",
)
@click.option(
    "-e",
    "--expansions",
    "only_include",
    is_flag=True,
    flag_value="ex",
    help="Include only expansions in output.",
)
@click.option("-v", "--verbose", is_flag=True, help="Display additional information.")
# TODO: add option to sort the list by a particular field
# TODO: add option to run update on the collection prior to list
# TODO: add option to show grid lines or not in the table
# TODO: implement paging/scrolling for long lists? not sure how rich will like that
def list_collection(collection: str, only_include: str, verbose: bool) -> None:
    """List all board games/extensions in a collection.

    - COLLECTION is the name of the collection to be listed.
    """
    # check that the given collection is a valid collection
    if not is_collection(collection):
        sys.exit(print_error(f"'{collection}' is not a valid collection"))

    boardgames, expansions = get_collection_data(collection)
    # check that local data exists for the given collection
    # TODO: add error/better handling for when a collection has no data files and/or is empty?
    if not boardgames and not expansions:
        sys.exit(
            print_warning(
                f"local data not found for '{collection}'. update with `meeple update {collection}`"
            )
        )

    # determine what to include in results depending on given flags
    if only_include == "bg":
        out_list = boardgames
    elif only_include == "ex":
        out_list = expansions
    else:
        out_list = boardgames + expansions

    # prepare table data
    headers = ["ID", "Name"]
    if verbose:
        headers = ["ID", "Name", "Year", "Rank", "Rating", "Weight", "Players", "Time"]

    rows = []
    for item in out_list:
        cols = []
        cols.extend([str(item.id), item.name])
        if verbose:
            cols.extend(
                [
                    str(item.year),
                    str(item.rank),
                    fmt_rating(item.rating),
                    fmt_weight(item.weight),
                    fmt_players(item.minplayers, item.maxplayers),
                    fmt_playtime(item.minplaytime, item.maxplaytime),
                ]
            )
        rows.append(cols)

    # TODO: add "Showing all ___ in ___ collection." printout above table?
    print_table(rows, headers)
