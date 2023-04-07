import sys
import webbrowser

import click

from meeple.util.api_util import BGG_DOMAIN, get_bgg_items
from meeple.util.input_util import bool_input
from meeple.util.output_util import print_error, print_info


@click.command(name="open")
@click.argument("id", type=int)
@click.help_option("-h", "--help")
# TODO: add -y option to automatically confirm opening on browser
def open_on_bgg(id: int) -> None:
    """Open an item on BoardGameGeek.

    - ID is the BoardGameGeek ID of the board game/expansion to be opened on boardgamegeek.com.
    """
    # check that the given id is a valid BoardGameGeek ID
    bgg_id = id
    api_result = get_bgg_items([bgg_id])
    if not api_result:
        sys.exit(print_error(f"Provided '{bgg_id}' is not a valid BoardGameGeek ID"))

    # confirm the user wants to open the board game/expansion on BoardGameGeek website
    item = api_result[0]
    url = f"https://{BGG_DOMAIN}/{item.type}/{bgg_id}"
    name = item.name
    if bool_input(f"Open '{name}' on {BGG_DOMAIN}?"):
        print(f"\tOpening '{name}' on {BGG_DOMAIN} ...")
        webbrowser.open(url)
    else:
        print_info(f"View '{name}' at {url}")
