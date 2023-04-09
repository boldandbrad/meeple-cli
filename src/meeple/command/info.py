import sys

import click

from meeple.util.api_util import get_bgg_item
from meeple.util.output_util import (
    fmt_players,
    fmt_playtime,
    fmt_rank,
    fmt_rating,
    fmt_weight,
    fmt_year,
    print_error,
    print_table,
)


@click.command()
@click.argument("id", type=int)
@click.option("-v", "--verbose", is_flag=True, help="Output additional details.")
@click.help_option("-h", "--help")
def info(id: int, verbose: bool) -> None:
    """Print out the details of an item.

    - ID is the BoardGameGeek ID of the board game/expansion to be detailed.
    """
    # check that the given id is a valid one
    bgg_id = id
    bgg_item = get_bgg_item(bgg_id)
    if not bgg_item:
        sys.exit(print_error(f"'{bgg_id}' is not a valid BoardGameGeek ID"))

    info_rows = [
        [
            f"Rating: {fmt_rating(bgg_item.rating)}",
            f"Players: {fmt_players(bgg_item.minplayers, bgg_item.maxplayers)}",
            f"Min Age: {bgg_item.minage}",
        ],
        [
            f"Rank: {fmt_rank(bgg_item.rank)}",
            f"Play Time: {fmt_playtime(bgg_item.playtime)}",
            f"Weight: {fmt_weight(bgg_item.weight)}",
        ],
    ]
    print_table([[f"{bgg_item.id}", f"{bgg_item.name} ({fmt_year(bgg_item.year)})"]])
    print_table(info_rows, lines=True)
    # include additional data if verbose flag present
    if verbose:
        print_table(
            [
                ["Description", bgg_item.description],
            ]
        )
