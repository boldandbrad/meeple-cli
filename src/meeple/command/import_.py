import click

from meeple.util.api_util import get_bgg_user, get_bgg_user_collection
from meeple.util.input_util import choice_input
from meeple.util.message_util import error_msg


@click.command(name="import")
@click.option("--username", required=True)
@click.help_option("-h", "--help")
# TODO: add dry-run option to show what collections and items would be created without persisting changes
# TODO: add single/multiple options or a flag to bypass import method prompt
def import_(username: str) -> None:
    """Import BoardGameGeek user collections."""
    # check that the given username is a valid BoardGameGeek username
    user = get_bgg_user(username)
    if not user.user_id:
        error_msg(f"[yellow]{username}[/yellow] is not a valid BoardGameGeek username.")

    # get user collection items
    collection_items = get_bgg_user_collection(username)

    # check that the user collection is not empty
    if not collection_items:
        error_msg(
            f"Nothing to import. BoardGameGeek user [yellow]{username}[/yellow]'s collection is empty."
        )

    # prompt to user for import method
    import_method = choice_input(
        f"Would you like to import [magenta]{username}[/magenta]'s user collection items into a single collection or into multiple by item status?",
        ["single", "multiple"],
    )

    # TODO: create new collection(s), check that collection names that don't already exist. do we let the user pick custom names?

    # TODO: add ids to the new collection(s)
    print(import_method)
    print(collection_items)
