import click

from meeple.util.collection_util import delete_collection, is_collection
from meeple.util.completion_util import complete_collections
from meeple.util.data_util import delete_collection_data, get_collection_data
from meeple.util.input_util import bool_input
from meeple.util.message_util import info_msg, invalid_collection_error


@click.command()
@click.argument("collection", shell_complete=complete_collections)
@click.option("-y", "--yes", is_flag=True, help="Dangerous - Bypass confirmation.")
@click.help_option("-h", "--help")
def delete(collection: str, yes: bool) -> None:
    """Delete a collection.

    - COLLECTION is the name of the collection to be deleted.
    """
    # check that the given collection exists
    if not is_collection(collection):
        invalid_collection_error(collection)

    # ask for confirmation or not depending on presence of flag
    if not yes:
        confirmation = bool_input(
            f"Are you sure you want to delete collection [u magenta]{collection}[/u magenta]?"
        )
    else:
        confirmation = True

    # delete collection and its data if confirmation succeeded
    if confirmation:
        delete_collection(collection)
        board_games, expansions = get_collection_data(collection)
        if board_games or expansions:
            delete_collection_data(collection)
        info_msg(f"Deleted collection [u magenta]{collection}[/u magenta].")
