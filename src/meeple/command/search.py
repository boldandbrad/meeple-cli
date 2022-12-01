import click

from meeple.util.api_util import get_search


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
    # api_result.sort(key=lambda x: x["id"])
    # TODO: tabulate output
    for item in api_result:
        print(f"{item.id}\t{item.name}")
