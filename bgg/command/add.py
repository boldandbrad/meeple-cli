import click

from bgg.util.collection_util import (
    get_collections,
    is_collection,
    read_collection,
    update_collection,
)


@click.command(help="Add a game/extension to a collection.")
@click.help_option("-h", "--help")
@click.argument("collection")
@click.argument("id")
def add(collection: str, id: int):
    print(f"adding {id} to {collection}...")
    if not id.isdigit():
        print("id must be an integer value.")
        return

    if not is_collection(collection):
        print(f"{collection} is not a valid collection.")
        return

    # TODO: check if id is a valid boardgame/expansion

    bgg_ids = read_collection(collection)
    if bgg_ids and int(id) in bgg_ids:
        print(f"{id} already exists in {collection}.")
        return
    bgg_ids.append(int(id))
    bgg_ids.sort()
    update_collection(collection, bgg_ids)
    print(f"{id} added to {collection}.")
