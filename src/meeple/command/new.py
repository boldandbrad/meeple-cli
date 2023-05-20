from typing import List

import click

from meeple.util.collection_util import create_collection, is_collection
from meeple.util.message_util import error_msg, info_msg, under_msg


@click.command()
@click.argument("collections", nargs=-1)
@click.help_option("-h", "--help")
def new(collections: List[str]) -> None:
    """Create new collections.

    - COLLECTIONS are names of the collections to create.
    """
    if len(collections) > 1:
        info_msg("Creating new collections...")
        for collection in collections:
            # check that the given collection doesn't already exist
            if is_collection(collection):
                under_msg(
                    f"[dim]Skipped collection [u magenta]{collection}[/u magenta]. It already exists.[/dim]"
                )
            else:
                # create new collection
                create_collection(collection)
                under_msg(
                    f"Created new collection [u magenta]{collection}[/u magenta]."
                )

        info_msg("Created new collection(s).")
    else:
        collection = collections[0]
        # check that the given collection doesn't already exist
        if is_collection(collection):
            error_msg(f"Collection [u magenta]{collection}[/u magenta] already exists.")

        # create new collection
        create_collection(collection)
        info_msg(f"Created new collection [u magenta]{collection}[/u magenta].")
