import sys

import click

from meeple.util.collection_util import is_collection
from meeple.util.data_util import get_data
from meeple.util.output_util import fmt_rating, fmt_weight, to_table


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
# TODO: implement paging/scrolling for long lists? not sure how tabulate will like that
def list_collection(collection: str, only_include: str, verbose: bool):
    """List all board games/extensions in a collection.

    - COLLECTION is the name of the collection to be listed.
    """
    # check that the given collection is a valid collection
    if not is_collection(collection):
        sys.exit(f"Error: '{collection}' is not a valid collection.")

    item_dict = get_data(collection)
    # check that local data exists for the given collection
    # TODO: add error/better handling for when a collection has no data files and/or is empty?
    if not item_dict:
        sys.exit(
            f"Warning: local data not found for '{collection}'. update with `meeple update {collection}`"
        )

    boardgames = item_dict["boardgames"]
    expansions = item_dict["expansions"]

    # determine what to include in results depending on given flags
    if only_include == "bg":
        out_list = boardgames
    elif only_include == "ex":
        out_list = expansions
    else:
        out_list = boardgames + expansions

    # prepare table data
    headers = ["ID", "Name", "Year", "Rank", "Rating", "Weight", "Players", "Time"]
    rows = []
    for item in out_list:
        cols = []
        cols.append(item["id"])
        cols.append(item["name"])
        if verbose:
            cols.append(item["year"])
            cols.append(item["rank"])
            # TODO: format with 2 decimal points always
            cols.append(fmt_rating(item["rating"]))
            cols.append(fmt_weight(item["weight"]))
            cols.append(f"{item['minplayers']}-{item['maxplayers']}")
            cols.append(f"{item['minplaytime']}-{item['maxplaytime']}")
        rows.append(cols)

    # TODO: add "Showing all ___ in ___ collection." printout above table?
    print(to_table(headers, rows))
