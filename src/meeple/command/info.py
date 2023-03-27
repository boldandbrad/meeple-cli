import sys

import click

from meeple.util.api_util import get_items
from meeple.util.output_util import fmt_rating, fmt_weight


@click.command()
@click.help_option("-h", "--help")
@click.argument("id")
def info(id: str):
    """Print out the details of a board game or expansion.

    - ID is the BoardGameGeek ID of the board game/expansion to be detailed.
    """
    # check that the given id is an integer
    if not id.isdigit():
        sys.exit("Error: ID must be an integer value.")

    # check that the given id is a valid one
    api_result = get_items([id])
    if not api_result:
        sys.exit(f"Error: '{id}' is not a valid BoardGameGeek ID.")

    item = api_result[0]
    # TODO: find a way to nicely tabulate this data
    print("────────────────────────────────────────────────")
    print(f"{item.name} ({item.year})")
    print("────────────────────────────────────────────────")
    print(f"{fmt_rating(item.rating)} Rating\tRank: {item.rank}\tID: {item.id}")
    print(
        f"{item.minplayers}-{item.maxplayers} Players\t{item.minplaytime}-{item.maxplaytime} Min\tWeight: {fmt_weight(item.weight)}/5"
    )
    print("────────────────────────────────────────────────")
