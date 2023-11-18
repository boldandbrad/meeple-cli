import webbrowser

import click

from meeple.util.api_util import BGG_DOMAIN, get_bgg_item, get_campaigns
from meeple.util.input_util import bool_input
from meeple.util.message_util import error_msg, info_msg, invalid_id_error, under_msg


@click.command(name="open")
@click.argument("bgg_id", type=int)
@click.option(
    "--campaign", is_flag=True, help="Open an item's crowdfunding campaign page."
)
@click.option("-y", "--yes", is_flag=True, help="Bypass confirmation.")
@click.help_option("-h", "--help")
def open_(bgg_id: int, campaign: bool, yes: bool) -> None:
    """Open items in the browser.

    - BGG_ID is the BoardGameGeek ID of the board game/expansion to be opened.
    """
    # check that the given id is a valid BoardGameGeek ID
    item = get_bgg_item(bgg_id)
    if not item:
        invalid_id_error(bgg_id)

    if campaign:
        campaigns = get_campaigns()
        matches = [
            campaign["orderUrl"]
            for campaign in campaigns
            if campaign["item"]["id"] == str(bgg_id)
        ]
        if matches:
            order_page_url = matches[0]
            if yes or bool_input(f"Open [i blue]{order_page_url}[/i blue]?"):
                under_msg(f"Opening [i blue]{order_page_url}[/i blue] ...")
                webbrowser.open(order_page_url)
            else:
                info_msg(
                    f"View campaign page for {bgg_id} at [u blue]{order_page_url}[/u blue]"
                )
        else:
            error_msg(f"[yellow]{bgg_id}[/yellow] does not have an active campaign.")
    else:
        # confirm the user wants to open the board game/expansion on BoardGameGeek website
        url = f"https://{BGG_DOMAIN}/{item.type}/{bgg_id}"
        name = item.name
        if yes or bool_input(f"Open [i blue]{name}[/i blue] on {BGG_DOMAIN}?"):
            under_msg(f"Opening [i blue]{name}[/i blue] on {BGG_DOMAIN} ...")
            webbrowser.open(url)
        else:
            info_msg(f"View [i blue]{name}[/i blue] at {url}")
