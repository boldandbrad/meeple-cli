import sys

import click

from meeple.util.collection_util import delete_collection, is_collection
from meeple.util.completion_util import complete_collections
from meeple.util.data_util import delete_collection_data, get_collection_data
from meeple.util.input_util import bool_input
from meeple.util.output_util import print_error, print_info


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
        sys.exit(print_error(f"'{collection}' already does not exist"))

    # ask for confirmation or not depending on presence of flag
    if not yes:
        confirmation = bool_input(f"Are you sure you want to delete '{collection}'?")
    else:
        confirmation = True

    # delete collection and its data if confirmation succeeded
    if confirmation:
        delete_collection(collection)
        boardgames, expansions = get_collection_data(collection)
        if boardgames or expansions:
            delete_collection_data(collection)
        print_info(f"Deleted collection '{collection}'")
