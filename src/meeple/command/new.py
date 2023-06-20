from typing import List

import click

from meeple.util.collection_util import create_collection, is_active_collection
from meeple.util.message_util import error_msg, info_msg, under_msg


@click.command()
@click.argument("collection_names", nargs=-1)
@click.help_option("-h", "--help")
def new(collection_names: List[str]) -> None:
    """Create new collections.

    - COLLECTIONS are names of the collections to create.
    """
    if len(collection_names) > 1:
        info_msg("Creating new collections...")
        for collection_name in collection_names:
            # check that the given collection doesn't already exist
            if is_active_collection(collection_name):
                under_msg(
                    f"[dim]Skipped collection [u magenta]{collection_name}[/u magenta]. It already exists.[/dim]"
                )
            else:
                # create new collection
                create_collection(collection_name)
                under_msg(
                    f"Created new collection [u magenta]{collection_name}[/u magenta]."
                )

        info_msg("Created new collection(s).")
    else:
        collection_name = collection_names[0]
        # check that the given collection doesn't already exist
        if is_active_collection(collection_name):
            error_msg(
                f"Collection [u magenta]{collection_name}[/u magenta] already exists."
            )

        # create new collection
        create_collection(collection_name)
        info_msg(f"Created new collection [u magenta]{collection_name}[/u magenta].")
