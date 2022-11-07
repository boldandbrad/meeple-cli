import click

from os.path import splitext

from bgg.util.collection_util import get_collections
from bgg.util.data_util import get_data, last_updated
from bgg.util.output_util import table


@click.command(help="List all local collections.")
@click.help_option("-h", "--help")
@click.option("-v", "--verbose", is_flag=True)
# TODO: add option to sort list by different columns
def collections(verbose: bool):
    # process each data source file
    collections = get_collections()
    headers = ["Collection", "Boardgames", "Expansions", "Last Updated"]
    rows = []
    for collection in collections:
        data = get_data(collection)
        cols = []
        cols.append(collection)
        if verbose:
            cols.append(len(data["boardgames"]))
            cols.append(len(data["expansions"]))
            cols.append(last_updated(collection))
        rows.append(cols)

    print(table(headers, rows))
