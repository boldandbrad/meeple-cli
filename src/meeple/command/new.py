import sys

import click

from meeple.util.collection_util import create_collection, is_collection
from meeple.util.output_util import print_error, print_info


@click.command()
@click.help_option("-h", "--help")
@click.argument("collection")
def new(collection: str):
    """Create a new local collection.

    - COLLECTION is the name of the collection to be created.
    """
    # check that the given collection doesn't already exist
    if is_collection(collection):
        sys.exit(print_error(f"'{collection}' already exists"))

    # create new collection
    create_collection(collection)
    print_info(f"Created new collection '{collection}'")
