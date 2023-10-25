import click

from meeple.util.api_util import get_bgg_item
from meeple.util.collection_util import get_collections
from meeple.util.fmt_util import (
    fmt_players,
    fmt_playtime,
    fmt_rank,
    fmt_rating,
    fmt_weight,
    fmt_year,
)
from meeple.util.message_util import invalid_id_error
from meeple.util.output_util import print_table


@click.command()
@click.argument("bgg_id", type=int)
@click.option("-v", "--verbose", is_flag=True, help="Output additional details.")
@click.help_option("-h", "--help")
def info(bgg_id: int, verbose: bool) -> None:
    """View item details.

    - BGG_ID is the BoardGameGeek ID of the board game/expansion to be detailed.
    """
    # check that the given id is a valid one
    bgg_item = get_bgg_item(bgg_id)
    if not bgg_item:
        invalid_id_error(bgg_id)

    # check which collections the item is contained in, if any
    in_collections = [
        collection.name
        for collection in get_collections()
        if bgg_item.id in collection.state.active_ids
    ]
    if in_collections:
        collections_str = (
            f"[u magenta]{'[/u magenta], [u magenta]'.join(in_collections)}[/u magenta]"
        )
    else:
        collections_str = "[dim]None[/dim]"

    stat_rows = [
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
                f"{bgg_item.fmt_name()} ({fmt_year(bgg_item.year)})",
                f"Collections: {collections_str}",
            ]
        ]
    )
    print_table(stat_rows, row_lines=True)

    # include additional data if verbose flag present
    if verbose:
        print_table(
            [
                ["Description", bgg_item.description],
                ["Designer(s)", ", ".join(bgg_item.credits.designers)],
                ["Artist(s)", ", ".join(bgg_item.credits.artists)],
                ["Publisher(s)", ", ".join(bgg_item.credits.publishers)],
            ],
            row_lines=True,
        )
