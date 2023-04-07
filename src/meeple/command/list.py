import sys

import click

from meeple.util.collection_util import is_collection
from meeple.util.completion_util import complete_collections
from meeple.util.data_util import get_collection_data
from meeple.util.output_util import (
    fmt_players,
    fmt_playtime,
    fmt_rank,
    fmt_rating,
    fmt_weight,
    fmt_year,
    print_error,
    print_table,
    print_warning,
)
from meeple.util.sort_util import sort_items


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
    type=click.Choice(
        ["rank", "rating", "weight", "year", "name", "id"], case_sensitive=False
    ),
    default="rating",
    show_default=True,
    help="Sort output by the provided column.",
)
@click.option("-v", "--verbose", is_flag=True, help="Output additional details.")
@click.help_option("-h", "--help")
# TODO: add option to run update on the collection prior to list
# TODO: add option to show grid lines or not in the table
# TODO: implement paging/scrolling for long lists? not sure how rich will like that
def list_collection(collection: str, item_type: str, sort: str, verbose: bool) -> None:
    """List contents of a collection.

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
    if item_type == "bg":
        out_list = boardgames
    elif item_type == "ex":
        out_list = expansions
    else:
        out_list = boardgames + expansions

    # sort output
    out_list = sort_items(out_list, sort)

    # prepare table data
    # TODO: add indicator to currently sorted by column
    headers = ["ID", "Name"]
    if verbose:
        headers.extend(["Year", "Rank", "Rating", "Weight", "Players", "Time"])

    rows = []
    for item in out_list:
        cols = [str(item.id), item.name]
        # include additional data if the user chose verbose output
        if verbose:
            cols.extend(
                [
                    fmt_year(item.year),
                    fmt_rank(str(item.rank)),
                    fmt_rating(item.rating),
                    fmt_weight(item.weight),
                    fmt_players(item.minplayers, item.maxplayers),
                    fmt_playtime(item.minplaytime, item.maxplaytime),
                ]
            )

        rows.append(cols)

    # TODO: add "Showing all ___ in ___ collection." printout above table?
    print_table(rows, headers)
