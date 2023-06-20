import click

from meeple.util.api_util import get_bgg_item
from meeple.util.fmt_util import (
    fmt_players,
    fmt_playtime,
    fmt_rank,
    fmt_rating,
    fmt_weight,
    fmt_year,
)
from meeple.util.message_util import invalid_id_error
from meeple.util.table_util import print_table


@click.command()
@click.argument("bgg_id", type=int)
@click.option("-v", "--verbose", is_flag=True, help="Output additional details.")
@click.help_option("-h", "--help")
def info(bgg_id: int, verbose: bool) -> None:
    """View detailed information of an item.

    - BGG_ID is the BoardGameGeek ID of the board game/expansion to be detailed.
    """
    # check that the given id is a valid one
    bgg_item = get_bgg_item(bgg_id)
    if not bgg_item:
        invalid_id_error(bgg_id)

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

    print_table(
        [
            [
                f"{bgg_item.id}",
                f"[i blue]{bgg_item.name}[/i blue] ({fmt_year(bgg_item.year)})",
            ]
        ]
    )
    print_table(info_rows, row_lines=True)

    # include additional data if verbose flag present
    if verbose:
        print_table(
            [
                ["Description", bgg_item.description],
            ]
        )
