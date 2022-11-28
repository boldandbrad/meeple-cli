import click

from bgg.util.api_util import get_search


@click.command()
@click.help_option("-h", "--help")
@click.argument("query")
# TODO: add option to sort output by different columns
# TODO: add verbosity flag to show more info about each result
def search(query: str):
    """Search bgg for a boardgame or expansion.

    - QUERY is the text to be searched for on BGG. If searching multiple words, surround with quotes.
    """
    # search BGG with user provided query
    api_result = get_search(query)
    # api_result.sort(key=lambda x: x["id"])
    # TODO: tabulate output
    for item in api_result:
        print(f"{item.id}\t{item.name}")
