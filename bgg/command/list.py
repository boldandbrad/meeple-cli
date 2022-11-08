import click

from bgg.util.collection_util import is_collection
from bgg.util.data_util import get_data
from bgg.util.output_util import color_weight, color_rating, table


@click.command(help="List all games/extensions in a collection.")
@click.help_option("-h", "--help")
@click.argument("collection")
@click.option(
    "-b",
    "--boardgames",
    "type",
    is_flag=True,
    flag_value="b",
    help="Include only boardgames in output.",
)
@click.option(
    "-e",
    "--expansions",
    "type",
    is_flag=True,
    flag_value="e",
    help="Include only expansions in output.",
)
@click.option("-v", "--verbose", is_flag=True, help="Display additional information.")
# TODO: add option to sort the list by a particular field
# TODO: add option to run update on the collection prior to list
# TODO: add option to show grid lines or not in the table
# TODO: implement paging/scrolling for long lists? not sure how tabulate will like that
def list_collection(collection: str, type: str, verbose: bool):
    if not is_collection(collection):
        print(f"{collection} is not a valid collection")
        return

    item_dict = get_data(collection)
    if not item_dict:
        print(
            f"local data not found for {collection}. update with `bgg update {collection}`"
        )
        return
    # add error/better handling for when a collection has no data files and/or is empty
    boardgames = item_dict["boardgames"]
    expansions = item_dict["expansions"]

    if type == "b":
        out_list = boardgames
    elif type == "e":
        out_list = expansions
    else:
        out_list = boardgames + expansions

    headers = ["ID", "Name", "Year", "Rank", "Rating", "Weight", "Players", "Time"]
    rows = []
    for item in out_list:
        cols = []
        cols.append(item["id"])
        cols.append(item["name"])
        if verbose:
            cols.append(item["year"])
            cols.append(item["rank"])
            # TODO: format with 2 decimal points always
            cols.append(color_rating(item["rating"]))
            cols.append(color_weight(item["weight"]))
            cols.append(f"{item['minplayers']}-{item['maxplayers']}")
            cols.append(f"{item['minplaytime']}-{item['maxplaytime']}")
        rows.append(cols)

    # TODO: add "Showing all ___ in ___ collection." printout about table
    print(table(headers, rows))
