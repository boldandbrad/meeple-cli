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
def add(collection: str, id: int) -> None:
    """Add an item to a collection.

    - COLLECTION is the name of the intended destination collection.

    - ID is the BoardGameGeek ID of the board game/expansion to be added.
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

    # if the given id is slated to be dropped, simply undo that
    if to_drop_ids and bgg_id in to_drop_ids:
        to_drop_ids.remove(bgg_id)
        item_ids.append(bgg_id)
        item_ids.sort()
    # if the given id does not exist in the collection, add the id
    elif bgg_id not in item_ids:
        to_add_ids.append(bgg_id)
        to_add_ids.sort()
    else:
        error_msg(
            f"[i blue]{bgg_item.name}[/i blue] already exists in collection [u magenta]{collection}[/u magenta]."
        )

    # persist changes
    update_collection(collection, item_ids, to_add_ids, to_drop_ids)
    info_msg(
        f"Added [i blue]{bgg_item.name}[/i blue] to collection [u magenta]{collection}[/u magenta]. To update, run: [green]meeple update[/green]"
    )
