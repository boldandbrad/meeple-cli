import sys

import click

from meeple.util.api_util import get_item
from meeple.util.output_util import fmt_rank, fmt_rating, fmt_weight, print_table


@click.command()
@click.help_option("-h", "--help")
@click.argument("id")
def info(id: str):
    """Print out the details of a board game or expansion.

    - ID is the BoardGameGeek ID of the board game/expansion to be detailed.
    """
    # check that the given id is an integer
    if not id.isdigit():
        sys.exit(print_error("Provided ID must be an integer value"))

    # check that the given id is a valid one
    bgg_item = get_item(id)
    if not bgg_item:
        sys.exit(print_error(f"'{id}' is not a valid BoardGameGeek ID"))

    info_rows = [
        [
            f"Rating: {fmt_rating(bgg_item.rating)}",
            f"Players: {bgg_item.minplayers}-{bgg_item.maxplayers}",
            f"Min Age: {bgg_item.minage}",
        ],
        [
            f"Rank: {fmt_rank(bgg_item.rank)}",
            f"Time: {bgg_item.minplaytime}-{bgg_item.maxplaytime} Min",
            f"Weight: {fmt_weight(bgg_item.weight)}",
        ],
    ]
    print_table([[f"{bgg_item.id}", f"{bgg_item.name} ({bgg_item.year})"]])
    print_table(info_rows, lines=True)
