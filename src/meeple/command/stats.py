import click

from meeple.util.collection_util import is_collection, is_pending_updates
from meeple.util.completion_util import complete_collections
from meeple.util.data_util import get_collection_data
from meeple.util.fmt_util import fmt_avg_rank, fmt_rating, fmt_weight
from meeple.util.message_util import error_msg, invalid_collection_error, warn_msg
from meeple.util.table_util import print_table


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
        invalid_collection_error(collection)

    board_games, expansions = get_collection_data(collection)
    # check that data exists for the given collection
    if not board_games and not expansions:
        error_msg(
            f"Local data not found for [u magenta]{collection}[/u magenta]. To update, run: [green]meeple update {collection}[/green]"
        )

    # determine what to include in results depending on given flags
    if item_type == "bg":
        out_list = board_games
    elif item_type == "ex":
        out_list = expansions
    else:
        out_list = board_games + expansions

    # check that data exists after applied filters
    if not out_list:
        error_msg(
            f"No items found matching provided filters for collection [u magenta]{collection}[/u magenta]."
        )

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

    # format output
    num_bgs_tag = f"{len(board_games)} Board Game(s)"
    num_exps_tag = f"{len(expansions)} Expansion(s)"
    if item_type == "bg":
        header = [f"[u magenta]{collection}[/u magenta]", num_bgs_tag]
    elif item_type == "ex":
        header = [f"[u magenta]{collection}[/u magenta]", num_exps_tag]
    else:
        header = [
            f"[u magenta]{collection}[/u magenta]",
            f"{num_bgs_tag} | {num_exps_tag}",
        ]

    if is_pending_updates(collection):
        warn_msg(
            f"Collection [u magenta]{collection}[/u magenta] has pending changes. To apply, run [green]meeple update {collection}[/green]"
        )

    print_table([header])
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
        row_lines=True,
    )
