import click

from bgg.util.collection_util import (
    get_collections,
    is_collection,
    read_collection,
    update_collection,
)


@click.command(help="Remove a game/extension from a collection.")
@click.help_option("-h", "--help")
@click.argument("collection")
@click.argument("id")
def drop(collection: str, id: int):
    print(f"dropping {id} from {collection}...")
    if not id.isdigit():
        print("id must be an integer value.")
        return

    if not is_collection(collection):
        print(f"{collection} is not a valid collection")
        return

    bgg_ids = read_collection(collection)
    if int(id) not in bgg_ids:
        print(f"{id} already doesn't exit exist in {collection}.")
        return
    bgg_ids.remove(int(id))
    update_collection(collection, bgg_ids)
    print(f"{id} dropped from {collection}.")
