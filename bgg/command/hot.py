import click

from bgg.util.api_util import get_hot
from bgg.util.output_util import color_rating, color_weight, table


@click.command()
@click.help_option("-h", "--help")
def hot():
    """Retrieve the current bgg hotness list."""
    # retrieve hotness data from BGG
    api_result = get_hot()

    # prepare table data
    headers = ["#", "ID", "Name"]
    rows = []
    for idx, item in enumerate(api_result):
        cols = []
        cols.append(idx + 1)
        cols.append(item.id)
        cols.append(item.name)
        rows.append(cols)

    print(table(headers, rows))
