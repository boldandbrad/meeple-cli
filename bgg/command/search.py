import click

from bgg.util.api_util import get_search, API_Result


@click.command(help="Get current bgg hotness list.")
@click.help_option("-h", "--help")
@click.argument("query")
def search(query: str):
    api_result = get_search(query)
    items = api_result["items"]["item"]
    if isinstance(items, list):
        for item in items:
            print(f"{int(item['@id'])}")
    else:
        item = items
        print(int(item["@id"]))
