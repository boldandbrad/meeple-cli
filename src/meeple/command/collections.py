import sys

import click

from meeple.util.collection_util import get_collections
from meeple.util.data_util import get_data, last_updated
from meeple.util.output_util import to_table


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
            "Warning: No local collections yet exist. Create a new one with `meeple new`"
        )

    # prepare table data
    headers = ["Collection", "Boardgames", "Expansions", "Last Updated"]
    rows = []
    for collection in collections:
        data = get_data(collection)
        cols = []
        cols.append(collection)

        # include additional data if the user choose verbose output
        if verbose:
            if data:
                cols.append(len(data["boardgames"]))
                cols.append(len(data["expansions"]))
                cols.append(last_updated(collection))
            else:
                cols.append(0)
                cols.append(0)
                cols.append("Never")

        rows.append(cols)

    print(to_table(headers, rows))
