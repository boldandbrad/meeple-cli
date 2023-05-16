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
@click.argument("from_collection", shell_complete=complete_collections)
@click.argument("to_collection", shell_complete=complete_collections)
@click.argument("id", type=int)
@click.help_option("-h", "--help")
def move(from_collection: str, to_collection: str, id: int) -> None:
    """Move an item from one collection to another.

    - FROM_COLLECTION is the name of the intended source collection.

    - TO_COLLECTION is the name of the intended destination collection.

    - ID is the BoardGameGeek ID of the board game/expansion to be moved.
    """
    # check that the given id is a valid BoardGameGeek ID
    bgg_id = id
    bgg_item = get_bgg_item(bgg_id)
    if not bgg_item:
        invalid_id_error(bgg_id)

    # check that the given from collection is a valid collection
    if not is_collection(from_collection):
        invalid_collection_error(from_collection)

    # get from collection item ids
    from_item_ids, from_to_add_ids, from_to_drop_ids = read_collection(from_collection)

    # check that the given to collection is a valid collection
    if not is_collection(to_collection):
        # TODO: prompt to create the dest collection
        invalid_collection_error(to_collection)

    # get destination collection item ids
    dest_item_ids, dest_to_add_ids, dest_to_drop_ids = read_collection(to_collection)

    # drop the id from the from collection
    # if the given id is slated to be added, simply undo that
    if from_to_add_ids and bgg_id in from_to_add_ids:
        from_to_add_ids.remove(bgg_id)
    # if the given id exists in the collection, drop the id
    elif from_item_ids and bgg_id in from_item_ids:
        from_item_ids.remove(bgg_id)
        from_to_drop_ids.append(bgg_id)
        from_to_drop_ids.sort()
    else:
        # TODO: prompt to just add to the destination collection anyway
        error_msg(
            f"[i blue]{bgg_item.name}[/i blue] already doesn't exist in collection [u magenta]{from_collection}[/u magenta]."
        )

    # add the id to the destination collection
    # if the given id is slated to be dropped, simply undo that
    if dest_to_drop_ids and bgg_id in dest_to_drop_ids:
        dest_to_drop_ids.remove(bgg_id)
        dest_item_ids.append(bgg_id)
        dest_item_ids.sort()
    # if the given id does not exist in the collection, add the id
    elif bgg_id not in dest_item_ids:
        dest_to_add_ids.append(bgg_id)
        dest_to_add_ids.sort()
    else:
        # TODO: prompt to just remove from the from collection anyway
        error_msg(
            f"[i blue]{bgg_item.name}[/i blue] already exists in collection [u magenta]{to_collection}[/u magenta]."
        )

    # persist changes
    update_collection(from_collection, from_item_ids, from_to_add_ids, from_to_drop_ids)
    update_collection(to_collection, dest_item_ids, dest_to_add_ids, dest_to_drop_ids)
    info_msg(
        f"Moved [i blue]{bgg_item.name}[/i blue] from collection [u magenta]{from_collection}[/u magenta] to collection [u magenta]{to_collection}[/u magenta]. To update, run: [green]meeple update[/green]"
    )
