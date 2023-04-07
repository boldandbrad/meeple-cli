import sys

import click

from meeple.util.collection_util import is_collection, rename_collection
from meeple.util.completion_util import complete_collections
from meeple.util.data_util import rename_collection_data_dir
from meeple.util.output_util import print_error, print_info


@click.command()
@click.argument("collection", shell_complete=complete_collections)
@click.argument("new_name")
@click.help_option("-h", "--help")
def rename(collection: str, new_name: str) -> None:
    """Rename a local collection.

    - COLLECTION is the name of the collection to be renamed.
    - NEW_NAME is the new name to assign to the collection.
    """
    # check that the given collection is a valid collection
    if not is_collection(collection):
        sys.exit(print_error(f"'{collection}' is not a valid collection"))

    # check that the given collection new name doesn't already exist
    if is_collection(new_name):
        sys.exit(print_error(f"'{new_name}' already exists"))

    # create new collection
    rename_collection(collection, new_name)
    rename_collection_data_dir(collection, new_name)
    print_info(f"Renamed collection '{collection}' to '{new_name}'")
