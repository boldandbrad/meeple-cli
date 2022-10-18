import webbrowser

import click

from bgg.util.api_util import get_items, BGG_DOMAIN
from bgg.util.input_util import bool_input


@click.command(help="Open a boardgame or expansion on the bgg website.")
@click.help_option("-h", "--help")
@click.argument("id")
def bgg_open(id: str):
    api_result = get_items([id])
    if not api_result:
        print("invalid id given")
    item = api_result[0]
    url = f"https://{BGG_DOMAIN}/{item['type']}/{id}"
    name = item["name"]
    if bool_input(f"Open {name} on {BGG_DOMAIN}?"):
        print(f"\tOpening {name} on {BGG_DOMAIN} ...")
        webbrowser.open(url)
    else:
        print(f"\tView {name} at {url}")
