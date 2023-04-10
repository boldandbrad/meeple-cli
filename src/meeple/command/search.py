import click

from meeple.util.api_util import search_bgg
from meeple.util.output_util import fmt_year, print_table


@click.command()
@click.argument("query")
@click.help_option("-h", "--help")
def search(query: str) -> None:
    """Search BoardGameGeek for items.

    - QUERY is the text to be searched for on BoardGameGeek. If searching multiple words, surround with quotes.
    """
    # search BoardGameGeek with user provided query
    api_result = search_bgg(query)
    api_result.sort(key=lambda x: x.id)

    # prepare table data
    headers = ["ID", "Name", "Year"]
    rows = []
    for item in api_result:
        cols = []
        cols.extend(
            [
                str(item.id),
                item.name,
                fmt_year(item.year),
            ]
        )
        rows.append(cols)

    print_table(rows, headers)
