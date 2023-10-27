import click

from meeple.util.api_util import get_bgg_hot
from meeple.util.output_util import ItemHeader, print_table


@click.command()
@click.help_option("-h", "--help")
def hot() -> None:
    """List current BoardGameGeek trending items."""
    # retrieve hotness data from BoardGameGeek
    api_result = get_bgg_hot()

    # prepare table data
    headers = [ItemHeader.COUNT, ItemHeader.ID, ItemHeader.NAME]

    rows = []
    for idx, item in enumerate(api_result):
        cols = []
        cols.extend([str(idx + 1), str(item.id), item.name])
        rows.append(cols)

    print_table(rows, headers)
