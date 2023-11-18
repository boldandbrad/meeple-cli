import click

from meeple.util.collection_util import get_collection
from meeple.util.completion_util import complete_collections
from meeple.util.fmt_util import fmt_avg_rank, fmt_rating, fmt_weight
from meeple.util.message_util import (
    error_msg,
    info_msg,
    invalid_collection_error,
    warn_msg,
)
from meeple.util.output_util import TableHeader, print_table


@click.command()
@click.argument("collection_name", shell_complete=complete_collections)
@click.option(
    "-b",
    "--boardgames",
    "item_type",
    is_flag=True,
    flag_value="bg",
    help="Include only board games.",
)
@click.option(
    "-e",
    "--expansions",
    "item_type",
    is_flag=True,
    flag_value="ex",
    help="Include only expansions.",
)
@click.help_option("-h", "--help")
def stats(collection_name: str, item_type: str) -> None:
    """View collection statistics.

    - COLLECTION_NAME is the name of the collection to be detailed.
    """
    # check that the given collection is a valid collection
    collection = get_collection(collection_name)
    if not collection:
        invalid_collection_error(collection_name)

    # check that data exists for the given collection
    if not collection.data.items:
        error_msg(
            f"Data not found for collection {collection.fmt_name()}. To update, run: [green]meeple update {collection.name}[/green]"
        )

    # determine what to include in results depending on given flags
    if item_type == "bg":
        result_items = collection.get_board_games()
    elif item_type == "ex":
        result_items = collection.get_expansions()
    else:
        result_items = collection.data.items

    # check that data exists after applied filters
    if not result_items:
        error_msg(
            f"No items found matching provided filters for collection {collection.fmt_name()}."
        )

    # calculate stats
    sum_ratings = (
        num_rated
    ) = sum_rank = num_ranked = sum_weight = num_weighted = sum_players = 0

    for item in result_items:
        if item.rating > 0:
            num_rated += 1
            sum_ratings += item.rating
        if item.rank > 0:
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
        avg_rating = round(sum_ratings / len(result_items), 2)
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
    avg_max_players = round(sum_players / len(result_items), 2)

    if collection.is_pending_updates():
        warn_msg(
            f"Collection {collection.fmt_name()} has pending updates. To apply, run [green]meeple update {collection.name}[/green]"
        )

    info_msg(
        f"Showing average stats for {len(result_items)} of {len(collection.data.items)} items from collection {collection.fmt_name()}."
    )
    headers = [
        TableHeader.RANK,
        TableHeader.RATING,
        TableHeader.WEIGHT,
        TableHeader.MAX_PLAYERS,
    ]
    rows = [
        [
            f"{fmt_avg_rank(avg_rank)}",
            f"{fmt_rating(avg_rating)}",
            f"{fmt_weight(avg_weight)}",
            f"{avg_max_players}",
        ],
    ]
    print_table(rows, headers)
