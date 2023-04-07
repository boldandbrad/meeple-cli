import sys

import click

from meeple.util.collection_util import is_collection
from meeple.util.completion_util import complete_collections
from meeple.util.data_util import get_collection_data
from meeple.util.output_util import (
    fmt_avg_rank,
    fmt_rating,
    fmt_weight,
    print_error,
    print_info,
    print_table,
    print_warning,
)


@click.command()
@click.argument("collection", shell_complete=complete_collections)
@click.option(
    "-b",
    "--boardgames",
    "item_type",
    is_flag=True,
    flag_value="bg",
    help="Output only board games.",
)
@click.option(
    "-e",
    "--expansions",
    "item_type",
    is_flag=True,
    flag_value="ex",
    help="Output only expansions.",
)
@click.help_option("-h", "--help")
def stats(collection: str, item_type: str) -> None:
    """Print out the details of a collection.

    - COLLECTION is the name of the collection to be detailed.
    """
    # check that the given collection is a valid collection
    if not is_collection(collection):
        sys.exit(print_error(f"'{collection}' is not a valid collection"))

    boardgames, expansions = get_collection_data(collection)
    # check that local data exists for the given collection
    # TODO: add error/better handling for when a collection has no data files and/or is empty?
    if not boardgames and not expansions:
        sys.exit(
            print_warning(
                f"local data not found for '{collection}'. update with `meeple update {collection}`"
            )
        )

    # determine what to include in results depending on given flags
    if item_type == "bg":
        out_list = boardgames
    elif item_type == "ex":
        out_list = expansions
    else:
        out_list = boardgames + expansions

    # calculate stats
    sum_ratings = (
        num_rated
    ) = sum_rank = num_ranked = sum_weight = num_weighted = sum_players = 0

    for item in out_list:
        if item.rating > 0:
            num_rated += 1
            sum_ratings += item.rating
        if item.rank.isdigit():
            num_ranked += 1
            sum_rank += int(item.rank)
        if item.weight > 0:
            num_weighted += 1
            sum_weight += item.weight
        if int(item.maxplayers) > 10:
            sum_players += 10
        else:
            sum_players += int(item.maxplayers)

    if num_rated > 0:
        avg_rating = round(sum_ratings / len(out_list), 2)
    else:
        avg_rating = 0
    if num_ranked > 0:
        avg_rank = round(sum_rank / num_ranked, 2)
    else:
        avg_rank = 0
    if num_weighted > 0:
        avg_weight = round(sum_weight / num_weighted, 2)
    else:
        avg_weight = 0
    avg_max_players = round(sum_players / len(out_list), 2)

    if item_type == "bg":
        header = f"{collection} ({len(boardgames)} Boardgames)"
    elif item_type == "ex":
        header = f"{collection} ({len(expansions)} Expansions)"
    else:
        header = f"{collection} ({len(boardgames)} Board games | {len(expansions)} Expansions)"

    print_info(header)
    print_table(
        [
            [
                f"Avg. Rating: {fmt_rating(avg_rating)}",
                f"Avg. Max Players: {avg_max_players}",
            ],
            [
                f"Avg. Rank: {fmt_avg_rank(avg_rank)}",
                f"Avg. Weight: {fmt_weight(avg_weight)}",
            ],
        ],
        lines=True,
    )
