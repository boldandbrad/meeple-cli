from datetime import date
from typing import List

import click

from meeple.type.collection import Collection
from meeple.util.collection_util import (
    get_collection,
    get_collections,
    is_active_collection,
    update_collection,
)
from meeple.util.completion_util import complete_collections
from meeple.util.message_util import (
    error_msg,
    info_msg,
    invalid_collection_error,
    no_collections_exist_error,
    under_msg,
)


@click.command()
@click.argument(
    "collection_names", nargs=-1, required=False, shell_complete=complete_collections
)
@click.option("-f", "--force", is_flag=True, help="Force update.")
@click.help_option("-h", "--help")
def update(collection_names: List[str], force: bool) -> None:
    """Update collection data.

    - COLLECTIONS (optional) are names of collections to update. [default: all]
    """
    # attempt to get the given collection(s)
    if collection_names:
        collections = [
            get_collection(collection_name)
            if is_active_collection(collection_name)
            else Collection(collection_name)
            for collection_name in collection_names
        ]
    # otherwise, attempt to get all active collections
    else:
        collections = get_collections()

    # check that collections exist
    if not collections:
        no_collections_exist_error()

    # attempt to update multiple collections
    if len(collections) > 1:
        info_msg("Updating collection data...")

        # update collection data
        for collection in collections:
            # check if collection exists
            if not is_active_collection(collection.name):
                under_msg(
                    f"[dim]Skipped collection {collection.fmt_name()}. It does not exist.[/dim]"
                )
                continue

            # print warning and skip if collection is empty
            if not collection.state:
                under_msg(
                    f"[yellow]Warning[/yellow]: Could not update collection {collection.fmt_name()} because it is empty. To add to it, run: [green]meeple add[/green]"
                )
                continue

            # skip if collection not pending updates, has been updated today, and force flag not provided
            if (
                not force
                and not collection.is_pending_updates()
                and collection.data.last_updated == str(date.today())
            ):
                under_msg(
                    f"[dim]Skipped collection {collection.fmt_name()}. Already up to date.[/dim]"
                )
                continue

            update_collection(collection, update_data=True)
            under_msg(f"Updated collection {collection.fmt_name()}.")

        info_msg("Updated collection data.")

    # update just one collection
    else:
        # check if collection exists
        collection = collections[0]
        if not is_active_collection(collection.name):
            invalid_collection_error(collection.name)

        # check if collection state is empty
        if not collection.state:
            error_msg(
                f"Could not update collection {collection.fmt_name()} because it is empty. To add to it, run: [green]meeple add[/green]"
            )

        # skip if collection not pending updates, has been updated today, and force flag not provided
        if (
            not force
            and not collection.is_pending_updates()
            and collection.data.last_updated == str(date.today())
        ):
            error_msg(
                f"Could not update collection {collection.fmt_name()}. Already up to date."
            )

        update_collection(collection, update_data=True)
        info_msg(f"Updated collection {collection.fmt_name()}.")
