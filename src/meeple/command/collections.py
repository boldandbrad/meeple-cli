import sys

import click

from meeple.type.collection import Collection
from meeple.util.collection_util import get_collections
from meeple.util.data_util import get_collection_data, last_updated
from meeple.util.output_util import (
    CollectionHeader,
    fmt_headers,
    print_table,
    print_warning,
)
from meeple.util.sort_util import COLLECTION_SORT_KEYS, sort_collections


@click.command()
@click.option(
    "--sort",
    type=click.Choice(COLLECTION_SORT_KEYS, case_sensitive=False),
    default="updated",
    show_default=True,
    help="Sort output by the provided column.",
)
@click.option("-v", "--verbose", is_flag=True, help="Output additional details.")
@click.help_option("-h", "--help")
def collections(sort: str, verbose: bool) -> None:
    """List all collections."""
    # attempt to retrieve collections
    collections = get_collections()

    # check that local collections exist
    if not collections:
        sys.exit(
            print_warning(
                "No local collections yet exist. Create a new one with `meeple new`"
            )
        )

    collection_list = []
    for collection in collections:
        boardgames, expansions = get_collection_data(collection)
        collection_list.append(
            Collection(collection, boardgames, expansions, last_updated(collection))
        )

    # sort output
    collection_list, sort_direction = sort_collections(collection_list, sort)

    # prepare table data
    headers = [CollectionHeader.NAME]
    if verbose:
        headers.extend(
            [
                CollectionHeader.BOARDGAMES,
                CollectionHeader.EXPANSIONS,
                CollectionHeader.UPDATED,
            ]
        )

    # format headers
    headers = fmt_headers(headers, sort, sort_direction)

    rows = []
    for collection in collection_list:
        cols = [collection.name]
        # include additional data if the user chose verbose output
        if verbose:
            cols.extend(
                [
                    str(len(collection.boardgames)),
                    str(len(collection.expansions)),
                    collection.last_updated,
                ]
            )

        rows.append(cols)

    print_table(rows, headers)
