import click

from meeple.util.collection_util import create_collection, is_collection
from meeple.util.message_util import error_msg, info_msg


@click.command()
@click.argument("collection")
@click.help_option("-h", "--help")
def new(collection: str) -> None:
    """Create a new collection.

    - COLLECTION is the name of the collection to be created.
    """
    # check that the given collection doesn't already exist
    if is_collection(collection):
        error_msg(f"Collection [u magenta]{collection}[/u magenta] already exists.")

    # create new collection
    create_collection(collection)
    info_msg(f"Created new collection [u magenta]{collection}[/u magenta].")
