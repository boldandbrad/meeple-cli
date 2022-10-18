import click

from bgg.util.api_util import get_search


@click.command(help="Search bgg for a boardgame or expansion.")
@click.help_option("-h", "--help")
@click.argument("query")
def search(query: str):
    api_result = get_search(query)
    # api_result.sort(key=lambda x: x["id"])
    for item in api_result:
        print(f"{item['id']}\t{item['name']}")
