import click

from meeple.util.api_util import get_bgg_item
from meeple.util.collection_util import (
    is_collection,
    read_collection,
    update_collection,
)
from meeple.util.completion_util import complete_collections
from meeple.util.message_util import (
    error_msg,
    info_msg,
    invalid_collection_error,
    invalid_id_error,
)


@click.command()
@click.argument("collection", shell_complete=complete_collections)
@click.argument("id", type=int)
@click.help_option("-h", "--help")
def drop(collection: str, id: int) -> None:
    """Remove an item from a collection.

    - COLLECTION is the name of the collection to be modified.

    - ID is the BoardGameGeek ID of the board game/expansion to be removed.
    """
    # check that the given id is a valid BoardGameGeek ID
    bgg_id = id
    bgg_item = get_bgg_item(bgg_id)
    if not bgg_item:
        invalid_id_error(bgg_id)

    # check that the given collection is a valid collection
    if not is_collection(collection):
        invalid_collection_error(collection)

    # get collection item ids
    item_ids, to_add_ids, to_drop_ids = read_collection(collection)

    # if the given id is slated to be added, simply undo that
    if to_add_ids and bgg_id in to_add_ids:
        to_add_ids.remove(bgg_id)
    # if the given id exists in the collection, drop the id
    elif item_ids and bgg_id in item_ids:
        item_ids.remove(bgg_id)
        to_drop_ids.append(bgg_id)
        to_drop_ids.sort()
    else:
        error_msg(
            f"[i blue]{bgg_item.name}[/i blue] already doesn't exist in collection [u magenta]{collection}[/u magenta]."
        )

    # persist changes
    update_collection(collection, item_ids, to_add_ids, to_drop_ids)
    info_msg(
        f"Dropped [i blue]{bgg_item.name}[/i blue] from collection [u magenta]{collection}[/u magenta]. To update, run: [green]meeple update[/green]"
    )
