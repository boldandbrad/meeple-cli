from typing import List

import click

from meeple.util.collection_util import delete_collection, get_collection
from meeple.util.completion_util import complete_collections
from meeple.util.input_util import bool_input
from meeple.util.message_util import info_msg, invalid_collection_error, under_msg


@click.command()
@click.argument("collection_names", nargs=-1, shell_complete=complete_collections)
@click.option("-y", "--yes", is_flag=True, help="Dangerous - Bypass confirmation.")
@click.help_option("-h", "--help")
def delete(collection_names: List[str], yes: bool) -> None:
    """Delete collections.

    - COLLECTION_NAMES are names of the collections to delete.
    """
    # ask for confirmation or not depending on presence of flag
    if not yes:
        confirmation = bool_input(
            f"Are you sure you want to delete collection(s) [u magenta]{'[/u magenta], [u magenta]'.join(collection_names)}[/u magenta]?"
        )
    else:
        confirmation = True

    # delete collection and its data if confirmation succeeded
    if confirmation:
        if len(collection_names) > 1:
            info_msg("Deleting collections...")
            for collection_name in collection_names:
                # check that the given collection exists
                collection = get_collection(collection_name)
                if collection:
                    # delete collection
                    delete_collection(collection)
                    under_msg(f"Deleted collection {collection.fmt_name()}.")
                else:
                    under_msg(
                        f"[dim]Skipped collection {collection.fmt_name()}. It already does not exist.[/dim]"
                    )
            info_msg("Deleted collection(s).")
        else:
            collection_name = collection_names[0]
            # check that the given collection exists
            collection = get_collection(collection_name)
            if collection:
                delete_collection(collection)
                info_msg(f"Deleted collection {collection.fmt_name()}.")
            else:
                invalid_collection_error(collection_name)
