from typing import List

import click

from meeple.util.collection_util import delete_collection, is_collection
from meeple.util.completion_util import complete_collections
from meeple.util.data_util import delete_collection_data, get_collection_data
from meeple.util.input_util import bool_input
from meeple.util.message_util import info_msg, invalid_collection_error, under_msg


def _delete_collection(collection_name: str) -> None:
    delete_collection(collection_name)
    board_games, expansions = get_collection_data(collection_name)
    if board_games or expansions:
        delete_collection_data(collection_name)


@click.command()
@click.argument("collections", nargs=-1, shell_complete=complete_collections)
@click.option("-y", "--yes", is_flag=True, help="Dangerous - Bypass confirmation.")
@click.help_option("-h", "--help")
def delete(collections: List[str], yes: bool) -> None:
    """Delete collections.

    - COLLECTIONS are names of the collections to delete.
    """
    # ask for confirmation or not depending on presence of flag
    if not yes:
        confirmation = bool_input(
            f"Are you sure you want to delete collection(s) [u magenta]{'[/u magenta], [u magenta]'.join(collections)}[/u magenta]?"
        )
    else:
        confirmation = True

    # delete collection and its data if confirmation succeeded
    if confirmation:
        if len(collections) > 1:
            info_msg("Deleting collections...")
            for collection in collections:
                # check that the given collection exists
                if is_collection(collection):
                    # delete collection
                    _delete_collection(collection)
                    under_msg(
                        f"Deleted collection [u magenta]{collection}[/u magenta]."
                    )
                else:
                    under_msg(
                        f"[dim]Skipped collection [u magenta]{collection}[/u magenta]. It already does not exist.[/dim]"
                    )
            info_msg("Deleted collection(s).")
        else:
            collection = collections[0]
            # check that the given collection exists
            if is_collection(collection):
                _delete_collection(collection)
                info_msg(f"Deleted collection [u magenta]{collection}[/u magenta].")
            else:
                invalid_collection_error(collection)
