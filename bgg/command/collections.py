import sys

import click

from bgg.util.collection_util import get_collections
from bgg.util.data_util import get_data, last_updated
from bgg.util.output_util import table


@click.command(help="List all local collections.")
@click.help_option("-h", "--help")
@click.option("-v", "--verbose", is_flag=True, help="Display additional information.")
# TODO: add option to sort list by different columns
def collections(verbose: bool):
    # process each data source file
    collections = get_collections()
    if not collections:
        sys.exit("No collections yet exist. Create a new one with `bgg new`")
    headers = ["Collection", "Boardgames", "Expansions", "Last Updated"]
    rows = []
    for collection in collections:
        data = get_data(collection)
        cols = []
        cols.append(collection)
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

    print(table(headers, rows))
