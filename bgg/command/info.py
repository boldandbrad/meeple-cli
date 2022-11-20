import click

from bgg.util.api_util import get_items
from bgg.util.output_util import color_weight, color_rating


@click.command(help="Print out the details of a boardgame or expansion.")
@click.help_option("-h", "--help")
@click.argument("id")
def info(id: str):
    api_result = get_items([id])
    if not api_result:
        print("invalid id given")
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
