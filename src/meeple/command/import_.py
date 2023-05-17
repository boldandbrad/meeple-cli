import click

from meeple.util.api_util import get_bgg_user, get_bgg_user_collection
from meeple.util.message_util import error_msg


@click.command(name="import")
@click.option("--username", required=True)
@click.help_option("-h", "--help")
def import_(username: str) -> None:
    """Import BoardGameGeek user collections."""
    # check that the given username is a valid BoardGameGeek username
    user = get_bgg_user(username)
    if not user.user_id:
        error_msg(f"[yellow]{username}[/yellow] is not a valid BoardGameGeek username.")

    # get user collection
    collection_items = get_bgg_user_collection(username)

    # check that the user collection is not empty
    if not collection_items:
        error_msg(
            f"Nothing to import. BoardGameGeek user [yellow]{username}[/yellow]'s collection is empty."
        )

    # TODO: figure out how to capture which statuses each item has in the user collection
    # TODO: prompt to user to determine if they want to create one collection with all items or create a separate collection for each status
    # TODO: create new collection(s), check that collection names that don't already exist. do we let the user pick custom names?
    # TODO: add ids to the new collection(s)

    print(collection_items)
