import sys

import click

from meeple.util.collection_util import create_collection, is_collection
from meeple.util.output_util import print_error, print_info


@click.command()
@click.argument("collection")
@click.help_option("-h", "--help")
def new(collection: str) -> None:
    """Create a new collection.

    - COLLECTION is the name of the collection to be created.
    """
    # check that the given collection doesn't already exist
    if is_collection(collection):
        sys.exit(print_error(f"'{collection}' already exists"))

    # create new collection
    create_collection(collection)
    print_info(f"Created new collection '{collection}'")
