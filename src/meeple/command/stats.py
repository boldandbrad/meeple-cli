import sys

import click

from meeple.util.collection_util import is_collection
from meeple.util.data_util import get_data
from meeple.util.output_util import fmt_rating, fmt_weight


@click.command()
@click.help_option("-h", "--help")
@click.argument("collection")
@click.option(
    "-b",
    "--boardgames",
    "type",
    is_flag=True,
    flag_value="b",
    help="Include only board games in output.",
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
    """Print out the details of a local collection.

    - COLLECTION is the name of the collection to be detailed.
    """
    # check that the given collection is a valid collection
    if not is_collection(collection):
        sys.exit(f"Error: '{collection}' is not a valid collection.")

    item_dict = get_data(collection)
    # check that local data exists for the given collection
    # TODO: add error/better handling for when a collection has no data files and/or is empty?
    if not item_dict:
        sys.exit(
            f"Warning: local data not found for '{collection}'. update with `meeple update {collection}`"
        )

    boardgames = item_dict["boardgames"]
    expansions = item_dict["expansions"]

    # determine what to include in results depending on given flags
    if type == "b":
        out_list = boardgames
    elif type == "e":
        out_list = expansions
    else:
        out_list = boardgames + expansions

    # calculate stats
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
            f"{collection} ({len(boardgames)} Board games | {len(expansions)} Expansions)"
        )
    print("────────────────────────────────────────────────")
    print(f"{fmt_rating(avg_rating)} Avg. Rating\tAvg. Rank: {avg_rank:.2f}\t")
    print(
        f"{avg_max_players} Avg. Max Players\tAvg. Weight: {fmt_weight(avg_weight)}/5"
    )
    print("────────────────────────────────────────────────")
