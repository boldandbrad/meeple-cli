import sys

import click

from bgg.util.api_util import get_items
from bgg.util.output_util import color_rating, color_weight


@click.command()
@click.help_option("-h", "--help")
@click.argument("id")
def info(id: str):
    """Print out the details of a boardgame or expansion.

    - ID is the BGG ID of the game/expansion to be detailed.
    """
    # check that the given id is an integer
    if not id.isdigit():
        sys.exit("Error: ID must be an integer value.")

    # check that the given id is a valid one
    api_result = get_items([id])
    if not api_result:
        sys.exit("Error: '{id}' is not a valid BGG ID.")

    item = api_result[0]
    # TODO: find a way to nicely tabulate this data
    print("────────────────────────────────────────────────")
    print(f"{item.name} ({item.year})")
    print("────────────────────────────────────────────────")
    print(f"{color_rating(item.rating)} Rating\tRank: {item.rank}\tID: {item.id}")
    print(
        f"{item.minplayers}-{item.maxplayers} Players\t{item.minplaytime}-{item.maxplaytime} Min\tWeight: {color_weight(item.weight)}/5"
    )
    print("────────────────────────────────────────────────")
