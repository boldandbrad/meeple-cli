import sys

import click

from meeple.util.collection_util import delete_collection, is_collection
from meeple.util.data_util import delete_data, get_data
from meeple.util.input_util import bool_input


@click.command()
@click.help_option("-h", "--help")
@click.argument("collection")
@click.option("-y", "--yes", is_flag=True, help="Dangerous - Bypass confirmation.")
def delete(collection: str, yes: bool):
    """Delete a local collection.

    - COLLECTION is the name of the collection to be deleted.
    """
    # check that the given collection exists
    if not is_collection(collection):
        sys.exit(f"Error: '{collection}' already does not exist.")

    # ask for confirmation or not depending on presence of flag
    if not yes:
        confirmation = bool_input(f"Are you sure you want to delete '{collection}'?")
    else:
        confirmation = True

    # delete collection and its data if confirmation succeeded
    if confirmation:
        delete_collection(collection)
        data = get_data(collection)
        if data:
            delete_data(collection)
        print(f"Successfully deleted collection '{collection}'.")
