from typing import List

import click

from meeple.type import BGG_COLLECTION_STATUSES, BGGCollectionItem
from meeple.util.api_util import get_bgg_user, get_bgg_user_collection
from meeple.util.collection_util import create_collection, unique_collection_name
from meeple.util.input_util import choice_input
from meeple.util.message_util import error_msg, info_msg, under_msg

ONE_IMPORT_METHOD = "one"
MANY_IMPORT_METHOD = "many"


def _import_collection(
    collection_items: List[BGGCollectionItem],
    collection_name: str,
    dry_run: bool,
    verbose: bool,
):
    # assign a unique collection name
    collection_name = unique_collection_name(collection_name)
    # simulate import
    if dry_run:
        under_msg(
            f"Import collection [u magenta]{collection_name}[/u magenta] containing {len(collection_items)} item(s)."
        )
    # perform import
    else:
        collection_ids = [item.bgg_id for item in collection_items]
        create_collection(collection_name, to_add_ids=collection_ids)
        under_msg(
            f"Imported collection [u magenta]{collection_name}[/u magenta] containing {len(collection_items)} item(s)."
        )
    if verbose:
        for item in collection_items:
            under_msg(
                f"{item.fmt_name()} ([dim]{item.bgg_id}[/dim])",
                indents=2,
            )


@click.command(name="import")
@click.argument("bgg-user")
@click.option(
    "--one",
    "import_method",
    flag_value=ONE_IMPORT_METHOD,
    help="Import as one collection.",
)
@click.option(
    "--many",
    "import_method",
    flag_value=MANY_IMPORT_METHOD,
    help="Import as separate collections by status.",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Simulate import operations without persisting.",
)
@click.option("-v", "--verbose", is_flag=True, help="Output additional details.")
@click.help_option("-h", "--help")
def import_(bgg_user: str, import_method: bool, dry_run: bool, verbose: bool) -> None:
    """Import BoardGameGeek user collections.

    - BGG_USER is a BoardGameGeek username.
    """
    # check that the given BoardGameGeek username is a valid
    user = get_bgg_user(bgg_user)
    if not user.user_id:
        error_msg(f"[yellow]{bgg_user}[/yellow] is not a valid BoardGameGeek username.")

    # get user collection items
    collection_items = get_bgg_user_collection(bgg_user)

    # check that the user collection is not empty
    if not collection_items:
        error_msg(
            f"Nothing to import. BoardGameGeek user [yellow]{bgg_user}[/yellow]'s collection is empty."
        )

    # prompt the user for import method
    if not import_method:
        import_method = choice_input(
            f"Would you like to import [magenta]{bgg_user}[/magenta]'s user collection items into one collection or many by item status?",
            [ONE_IMPORT_METHOD, MANY_IMPORT_METHOD],
        )

    if dry_run:
        info_msg("Simulating collection import...")
    else:
        info_msg("Importing collection(s)...")

    # create new collection(s) using the chosen import method or preform dry run
    match import_method:
        # import single collection with all items
        case "one":
            _import_collection(collection_items, bgg_user, dry_run, verbose)

        # import a separate collection for each used item status
        case "many":
            # separate items into their respective status collections and import each
            for status in BGG_COLLECTION_STATUSES:
                # get items with status
                status_items = [
                    item for item in collection_items if status in item.statuses
                ]
                # import the collection if it contains items
                if status_items:
                    _import_collection(
                        status_items, f"{bgg_user}-{status}", dry_run, verbose
                    )

    if not dry_run:
        info_msg("Imported collection(s). To update, run [green]meeple update[/green]")
