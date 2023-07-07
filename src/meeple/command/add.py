import click

from meeple.util.api_util import get_bgg_item
from meeple.util.collection_util import get_collection, update_collection
from meeple.util.completion_util import complete_collections
from meeple.util.message_util import (
    error_msg,
    info_msg,
    invalid_collection_error,
    invalid_id_error,
)


@click.command()
@click.argument("collection_name", shell_complete=complete_collections)
@click.argument("bgg_id", type=int)
@click.option("--update", is_flag=True, help="Update collection data.")
@click.help_option("-h", "--help")
def add(collection_name: str, bgg_id: int, update: bool) -> None:
    """Add an item to a collection.

    - COLLECTION_NAME is the name of the intended destination collection.

    - BGG_ID is the BoardGameGeek ID of the board game/expansion to be added.
    """
    # check that the given id is a valid BoardGameGeek ID
    bgg_item = get_bgg_item(bgg_id)
    if not bgg_item:
        invalid_id_error(bgg_id)

    # check that the given collection is a valid collection
    collection = get_collection(collection_name)
    if not collection:
        invalid_collection_error(collection_name)

    # if the given id is slated to be dropped, simply undo that
    if bgg_id in collection.state.to_drop_ids:
        collection.state.to_drop_ids.remove(bgg_id)
        collection.state.active_ids.append(bgg_id)
        collection.state.active_ids.sort()
    # if the given id does not exist in the collection, add the id
    elif bgg_id not in collection.state.active_ids:
        collection.state.to_add_ids.append(bgg_id)
        collection.state.to_add_ids.sort()
    else:
        error_msg(
            f"[i blue]{bgg_item.name}[/i blue] already exists in collection [u magenta]{collection.name}[/u magenta]."
        )

    # persist changes
    update_collection(collection, update_data=update)
    if update:
        info_msg(
            f"Added [i blue]{bgg_item.name}[/i blue] to collection [u magenta]{collection.name}[/u magenta] and updated collection."
        )
    else:
        info_msg(
            f"Added [i blue]{bgg_item.name}[/i blue] to collection [u magenta]{collection.name}[/u magenta]. To update, run: [green]meeple update[/green]"
        )
