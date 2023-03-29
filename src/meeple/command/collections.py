import sys

import click

from meeple.util.collection_util import get_collections
from meeple.util.data_util import get_data, last_updated
from meeple.util.output_util import print_table, print_warning


@click.command()
@click.help_option("-h", "--help")
@click.option("-v", "--verbose", is_flag=True, help="Display additional information.")
# TODO: add option to sort list by different columns
def collections(verbose: bool):
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
        headers.append("Boardgames")
        headers.append("Expansions")
        headers.append("Last Updated")
    rows = []
    for collection in collections:
        data = get_data(collection)
        cols = []
        cols.append(collection)

        # include additional data if the user choose verbose output
        if verbose:
            if data:
                cols.append(str(len(data["boardgames"])))
                cols.append(str(len(data["expansions"])))
                cols.append(last_updated(collection))
            else:
                cols.append("0")
                cols.append("0")
                cols.append("Never")

        rows.append(cols)

    print_table(rows, headers)
