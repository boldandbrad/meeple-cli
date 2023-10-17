import click

from meeple.util.collection_util import (
    get_collection,
    is_active_collection,
    rename_collection,
)
from meeple.util.completion_util import complete_collections
from meeple.util.message_util import error_msg, info_msg, invalid_collection_error


@click.command()
@click.argument("collection_name", shell_complete=complete_collections)
@click.argument("new_name")
@click.help_option("-h", "--help")
def rename(collection_name: str, new_name: str) -> None:
    """Rename a collection.

    - COLLECTION_NAME is the name of the collection to be renamed.
    - NEW_NAME is the new name to assign to the collection.
    """
    # check that the given collection is a valid collection
    collection = get_collection(collection_name)
    if not collection:
        invalid_collection_error(collection_name)

    # check that the given collection new name doesn't already exist
    if is_active_collection(new_name):
        error_msg(f"Collection [u magenta]{collection}[/u magenta] already exists.")

    # create new collection
    rename_collection(collection, new_name)
    info_msg(
        f"Renamed collection {collection.fmt_name()} to [u magenta]{new_name}[/u magenta]."
    )
