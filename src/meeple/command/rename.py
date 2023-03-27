import sys

import click

from meeple.util.collection_util import is_collection, rename_collection
from meeple.util.data_util import rename_collection_data_dir


@click.command()
@click.help_option("-h", "--help")
@click.argument("collection")
@click.argument("new_name")
def rename(collection: str, new_name: str):
    """Rename a local collection.

    - COLLECTION is the name of the collection to be renamed.
    - NEW_NAME is the new name to assign to the collection.
    """
    # check that the given collection is a valid collection
    if not is_collection(collection):
        sys.exit(f"Error: '{collection}' is not a valid collection.")

    # check that the given collection new name doesn't already exist
    if is_collection(new_name):
        sys.exit(f"Error: '{new_name}' already exists.")

    # create new collection
    rename_collection(collection, new_name)
    rename_collection_data_dir(collection, new_name)
    print(f"Successfully renamed collection '{collection}' to '{new_name}.")
