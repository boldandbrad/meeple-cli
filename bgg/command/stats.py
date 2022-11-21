import click

from bgg.util.collection_util import is_collection
from bgg.util.data_util import get_data
from bgg.util.output_util import color_rating, color_weight


@click.command(help="Print out the details of a local collection.")
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
def stats(collection: str, type: str):
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

    sum_ratings = sum_rank = num_ranked = sum_weight = num_weighted = sum_players = 0

    for item in out_list:
        sum_ratings += item["rating"]
        if item["rank"].isdigit():
            num_ranked += 1
            sum_rank += int(item["rank"])
        if item["weight"] > 0:
            num_weighted += 1
            sum_weight += item["weight"]
        sum_players += int(item["maxplayers"])

    avg_rating = round(sum_ratings / len(out_list), 2)
    if num_ranked > 0:
        avg_rank = round(sum_rank / num_ranked, 2)
    else:
        avg_rank = "NA"
    avg_weight = round(sum_weight / num_weighted, 2)
    avg_max_players = round(sum_players / len(out_list), 2)

    # TODO: find a way to nicely tabulate this data
    print("────────────────────────────────────────────────")
    if type == "b":
        print(f"{collection} ({len(boardgames)} Boardgames)")
    elif type == "e":
        print(f"{collection} ({len(expansions)} Expansions)")
    else:
        print(
            f"{collection} ({len(boardgames)} Boardgames | {len(expansions)} Expansions)"
        )
    print("────────────────────────────────────────────────")
    print(f"{color_rating(avg_rating)} Avg. Rating\tAvg. Rank: {avg_rank:.2f}\t")
    print(
        f"{avg_max_players} Avg. Max Players\tAvg. Weight: {color_weight(avg_weight)}/5"
    )
    print("────────────────────────────────────────────────")
