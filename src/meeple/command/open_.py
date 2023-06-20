import webbrowser

import click

from meeple.util.api_util import BGG_DOMAIN, get_bgg_item
from meeple.util.input_util import bool_input
from meeple.util.message_util import info_msg, invalid_id_error, under_msg


@click.command(name="open")
@click.argument("bgg_id", type=int)
@click.option("-y", "--yes", is_flag=True, help="Bypass confirmation.")
@click.help_option("-h", "--help")
def open_(bgg_id: int, yes: bool) -> None:
    """Open an item on BoardGameGeek.

    - BGG_ID is the BoardGameGeek ID of the board game/expansion to be opened on boardgamegeek.com.
    """
    # check that the given id is a valid BoardGameGeek ID
    item = get_bgg_item(bgg_id)
    if not item:
        invalid_id_error(bgg_id)

    # confirm the user wants to open the board game/expansion on BoardGameGeek website
    url = f"https://{BGG_DOMAIN}/{item.type}/{bgg_id}"
    name = item.name
    if yes or bool_input(f"Open [i blue]{name}[/i blue] on {BGG_DOMAIN}?"):
        under_msg(f"Opening [i blue]{name}[/i blue] on {BGG_DOMAIN} ...")
        webbrowser.open(url)
    else:
        info_msg(f"View [i blue]{name}[/i blue] at {url}")
