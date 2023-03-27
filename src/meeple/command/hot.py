import click

from meeple.util.api_util import get_hot
from meeple.util.output_util import to_table


@click.command()
@click.help_option("-h", "--help")
# TODO: add verbosity flag to show more details for each item
def hot():
    """Retrieve the current BoardGameGeek hotness list."""
    # retrieve hotness data from BoardGameGeek
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

    print(to_table(headers, rows))
