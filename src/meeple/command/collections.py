import click

from meeple.util.collection_util import get_collections
from meeple.util.fmt_util import fmt_collection_name, fmt_date, fmt_headers
from meeple.util.message_util import no_collections_exist_error, warn_msg
from meeple.util.sort_util import COLLECTION_SORT_KEYS, sort_collections
from meeple.util.table_util import CollectionHeader, print_table


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
    if not collections:
        no_collections_exist_error()

    # check if any collections are pending changes
    pending_changes = False
    for collection in collections:
        if collection.is_pending_updates():
            pending_changes = True

    # sort output
    collections, sort_direction = sort_collections(collections, sort)

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
    for collection in collections:
        cols = [fmt_collection_name(collection)]
        # include additional data if the user chose verbose output
        if verbose:
            cols.extend(
                [
                    str(len(collection.get_board_games())),
                    str(len(collection.get_expansions())),
                    fmt_date(collection.data.last_updated),
                ]
            )

        rows.append(cols)

    # print warning if some collections need to be updated
    if pending_changes:
        warn_msg(
            "Some collections ([red]*[/red]) are pending changes. To apply, run [green]meeple update[/green]"
        )

    print_table(rows, headers)
