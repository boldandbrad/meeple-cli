import sys
import webbrowser

import click

from bgg.util.api_util import BGG_DOMAIN, get_items
from bgg.util.input_util import bool_input


@click.command()
@click.help_option("-h", "--help")
@click.argument("id")
# TODO: add -y option to automatically confirm opening on browser
def open_on_bgg(id: str):
    """Open a boardgame or expansion on the bgg website.

    - ID is the BGG ID of the game/expansion to be opened on boardgamegeek.com.
    """
    # check that the given id is a valid BGG ID
    api_result = get_items([id])
    if not api_result:
        sys.exit("Error: '{id}' is not a valid BGG ID.")

    # confirm the user wants to open the game/expansion on BGG website
    item = api_result[0]
    url = f"https://{BGG_DOMAIN}/{item.type}/{id}"
    name = item.name
    if bool_input(f"Open {name} on {BGG_DOMAIN}?"):
        print(f"\tOpening {name} on {BGG_DOMAIN} ...")
        webbrowser.open(url)
    else:
        print(f"\tView {name} at {url}")
