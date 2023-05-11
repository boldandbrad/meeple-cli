import sys

import click

from meeple.util.api_util import search_bgg
from meeple.util.output_util import (
    ItemHeader,
    fmt_headers,
    fmt_year,
    print_table,
    print_warning,
)


@click.command()
@click.argument("query")
@click.help_option("-h", "--help")
def search(query: str) -> None:
    """Search BoardGameGeek for items.

    - QUERY is the text to be searched for on BoardGameGeek. If searching multiple words, surround with quotes.
    """
    # search BoardGameGeek with user provided query
    result_items = search_bgg(query)

    # check that data exists after applied filters
    if not result_items:
        sys.exit(
            print_warning(
                f"No items found on BoardGameGeek matching search term [i blue]{query}[i blue]."
            )
        )

    result_items.sort(key=lambda x: x.id)

    # prepare table data
    headers = [ItemHeader.ID, ItemHeader.NAME, ItemHeader.YEAR]
    headers = fmt_headers(headers, None, None)

    rows = []
    for item in result_items:
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
