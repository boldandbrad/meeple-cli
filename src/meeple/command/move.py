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
@click.argument("from_collection_name", shell_complete=complete_collections)
@click.argument("to_collection_name", shell_complete=complete_collections)
@click.argument("bgg_id", type=int)
@click.option("--update", is_flag=True, help="Update collection data.")
@click.help_option("-h", "--help")
def move(
    from_collection_name: str, to_collection_name: str, bgg_id: int, update: bool
) -> None:
    """Move an item from one collection to another.

    - FROM_COLLECTION_NAME is the name of the intended source collection.

    - TO_COLLECTION_NAME is the name of the intended destination collection.

    - BGG_ID is the BoardGameGeek ID of the board game/expansion to be moved.
    """
    # check that the given id is a valid BoardGameGeek ID
    bgg_item = get_bgg_item(bgg_id)
    if not bgg_item:
        invalid_id_error(bgg_id)

    # check that the given from collection is a valid collection
    from_collection = get_collection(from_collection_name)
    if not from_collection:
        invalid_collection_error(from_collection_name)

    # check that the given to collection is a valid collection
    to_collection = get_collection(to_collection_name)
    if not to_collection:
        # TODO: prompt to create the dest collection
        invalid_collection_error(to_collection_name)

    # drop the id from the from collection
    # if the given id is slated to be added, simply undo that
    if bgg_id in from_collection.state.to_add_ids:
        from_collection.state.to_add_ids.remove(bgg_id)
    # if the given id exists in the collection, drop the id
    elif bgg_id in from_collection.state.active_ids:
        from_collection.state.active_ids.remove(bgg_id)
        from_collection.state.to_drop_ids.append(bgg_id)
        from_collection.state.to_drop_ids.sort()
    else:
        # TODO: prompt to just add to the destination collection anyway
        error_msg(
            f"{bgg_item.fmt_name()} already doesn't exist in collection [u magenta]{from_collection.name}[/u magenta]."
        )

    # add the id to the destination collection
    # if the given id is slated to be dropped, simply undo that
    if bgg_id in to_collection.state.to_drop_ids:
        to_collection.state.to_drop_ids.remove(bgg_id)
        to_collection.state.active_ids.append(bgg_id)
        to_collection.state.active_ids.sort()
    # if the given id does not exist in the collection, add the id
    elif bgg_id not in to_collection.state.active_ids:
        to_collection.state.to_add_ids.append(bgg_id)
        to_collection.state.to_add_ids.sort()
    else:
        # TODO: prompt to just remove from the from collection anyway
        error_msg(
            f"{bgg_item.fmt_name()} already exists in collection [u magenta]{to_collection.name}[/u magenta]."
        )

    # persist changes
    update_collection(from_collection, update_data=update)
    update_collection(to_collection, update_data=update)
    if update:
        info_msg(
            f"Moved {bgg_item.fmt_name()} from collection [u magenta]{from_collection.name}[/u magenta] to collection [u magenta]{to_collection.name}[/u magenta] and updated collections."
        )
    else:
        info_msg(
            f"Moved {bgg_item.fmt_name()} from collection [u magenta]{from_collection.name}[/u magenta] to collection [u magenta]{to_collection.name}[/u magenta]. To update, run: [green]meeple update[/green]"
        )
