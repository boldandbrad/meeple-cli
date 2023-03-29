import click

from meeple.util.api_util import get_search
from meeple.util.output_util import print_table


@click.command()
@click.help_option("-h", "--help")
@click.argument("query")
# TODO: add option to sort output by different columns
# TODO: add verbosity flag to show more info about each result
def search(query: str):
    """Search BoardGameGeek for a board game or expansion.

    - QUERY is the text to be searched for on BoardGameGeek. If searching multiple words, surround with quotes.
    """
    # search BoardGameGeek with user provided query
    api_result = get_search(query)
    api_result.sort(key=lambda x: x.id)

    # prepare table data
    headers = ["ID", "Name", "Year"]
    rows = []
    for item in api_result:
        cols = []
        cols.append(str(item.id))
        cols.append(item.name)
        cols.append(str(item.year))
        rows.append(cols)

    print_table(rows, headers)
