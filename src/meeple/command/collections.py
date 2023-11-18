import click

from meeple.util.collection_util import get_collections, update_collection
from meeple.util.fmt_util import fmt_cmd
from meeple.util.message_util import info_msg, no_collections_exist_error, warn_msg
from meeple.util.output_util import TableHeader, print_table
from meeple.util.sort_util import COLLECTION_SORT_KEYS, sort_collections


@click.command()
@click.option(
    "--sort",
    type=click.Choice(COLLECTION_SORT_KEYS, case_sensitive=False),
    default="updated",
    show_default=True,
    help="Sort collections by the provided value.",
)
@click.option("--update", is_flag=True, help="Update collection data.")
@click.option("-v", "--verbose", is_flag=True, help="Output additional details.")
@click.help_option("-h", "--help")
def collections(sort: str, update: bool, verbose: bool) -> None:
    """List all collections."""
    # attempt to retrieve collections
    collections = get_collections()
    if not collections:
        no_collections_exist_error()

    # update collection data if requested
    pending_updates = False
    if update:
        for collection in collections:
            update_collection(collection, update_data=True)
        info_msg("Collection data updated.")
    else:
        # check if any collections are pending updates
        for collection in collections:
            if collection.is_pending_updates():
                pending_updates = True
        if pending_updates:
            warn_msg(
                f"([red]*[/red]) Some collections are pending updates. To apply, run {fmt_cmd('meeple update')}"
            )

    # sort output
    collections, sort_direction = sort_collections(collections, sort)

    # prepare table data
    headers = [TableHeader.NAME]
    if verbose:
        headers.extend(
            [
                TableHeader.BOARDGAMES,
                TableHeader.EXPANSIONS,
                TableHeader.UPDATED,
            ]
        )

    rows = []
    for collection in collections:
        cols = [collection.fmt_name(styled=False, state=True)]
        # include additional data if the user chose verbose output
        if verbose:
            cols.extend(
                [
                    str(len(collection.get_board_games())),
                    str(len(collection.get_expansions())),
                    collection.data.fmt_last_updated(),
                ]
            )

        rows.append(cols)

    print_table(rows, headers, sort_key=sort, sort_direction=sort_direction)
