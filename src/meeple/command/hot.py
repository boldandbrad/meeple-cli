import click

from meeple.util.api_util import get_bgg_hot
from meeple.util.output_util import print_table


@click.command()
@click.help_option("-h", "--help")
# TODO: add verbosity flag to show more details for each item
def hot() -> None:
    """List current BoardGameGeek trending items."""
    # retrieve hotness data from BoardGameGeek
    api_result = get_bgg_hot()

    # prepare table data
    headers = ["#", "ID", "Name"]
    rows = []
    for idx, item in enumerate(api_result):
        cols = []
        cols.extend([str(idx + 1), str(item.id), item.name])
        rows.append(cols)

    print_table(rows, headers)
