import click

from bgg.util.collection_util import is_collection, read_collection
from bgg.util.data_util import get_data
from bgg.util.api_util import get_items


@click.command(help="List all games/extensions in a collection.")
@click.help_option("-h", "--help")
@click.argument("collection")
@click.option("-b", "--boardgames", "type", is_flag=True, flag_value="b")
@click.option("-e", "--expansions", "type", is_flag=True, flag_value="e")
# TODO: add option to run update on the collection prior to list
def list_collection(collection: str, type: str):
    if not is_collection(collection):
        print(f"{collection} is not a valid collection")
        return

    item_dict = get_data(collection)
    if not item_dict:
        print(
            f"local data not found for {collection}. update with `bgg update {collection}`"
        )
        return

    boardgames = item_dict["boardgames"]
    expansions = item_dict["expansions"]

    if type == "b":
        out_list = boardgames
    elif type == "e":
        out_list = expansions
    else:
        out_list = boardgames + expansions

    for item in out_list:
        print(f"{str(item['id'])}\t{item['name']}")
