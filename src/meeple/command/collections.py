import sys

import click

from meeple.util.collection_util import get_collections
from meeple.util.data_util import get_collection_data, last_updated
from meeple.util.output_util import print_table, print_warning


@click.command()
@click.help_option("-h", "--help")
@click.option("-v", "--verbose", is_flag=True, help="Display additional information.")
# TODO: add option to sort list by different columns
def collections(verbose: bool) -> None:
    """List all local collections."""
    # attempt to retrieve collections
    collections = get_collections()

    # check that local collections exist
    if not collections:
        sys.exit(
            print_warning(
                "No local collections yet exist. Create a new one with `meeple new`"
            )
        )

    # prepare table data
    headers = ["Collection"]
    if verbose:
        headers.extend(["Boardgames", "Expansions", "Last Updated"])
    rows = []
    for collection in collections:
        boardgames, expansions = get_collection_data(collection)
        cols = [collection]
        # include additional data if the user choose verbose output
        if verbose:
            cols.extend(
                [
                    str(len(boardgames)),
                    str(len(expansions)),
                    last_updated(collection),
                ]
            )

        rows.append(cols)

    print_table(rows, headers)
