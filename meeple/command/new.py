import sys

import click

from meeple.util.collection_util import create_collection, is_collection


@click.command()
@click.help_option("-h", "--help")
@click.argument("collection")
def new(collection: str):
    """Create a new local collection.

    - COLLECTION is the name of the collection to be created.
    """
    # check that the given collection doesn't already exist
    if is_collection(collection):
        sys.exit(f"Error: '{collection}' already exists.")

    # create new collection
    create_collection(collection)
    print(f"Successfully created new collection '{collection}'.")
