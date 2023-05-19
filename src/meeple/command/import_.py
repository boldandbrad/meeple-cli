import click

from meeple.util.api_util import get_bgg_user, get_bgg_user_collection
from meeple.util.collection_util import create_collection, unique_collection_name
from meeple.util.input_util import choice_input
from meeple.util.message_util import error_msg, info_msg, under_msg


def _import_collection(
    collection_items, collection_name: str, bgg_user: str, dry_run: bool, verbose: bool
) -> None:
    # assign a unique collection name
    collection_name = unique_collection_name(collection_name)
    # show expected changes if import were performed
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
                f"[i blue]{item.name}[/i blue] ([dim]{item.bgg_id}[/dim])",
                indents=2,
            )


@click.command(name="import")
@click.option("--bgg-user", required=True, help="BoardGameGeek username.")
@click.option(
    "--dry-run",
    is_flag=True,
    help="Summarize potential import operations without persisting.",
)
@click.option("-v", "--verbose", is_flag=True, help="Output additional details.")
@click.help_option("-h", "--help")
# TODO: add single/multiple options or a flag to bypass import method prompt
def import_(bgg_user: str, dry_run: bool, verbose: bool) -> None:
    """Import BoardGameGeek user collections."""
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

    # prompt to user for import method
    import_method = choice_input(
        f"Would you like to import [magenta]{bgg_user}[/magenta]'s user collection items into a single collection or into multiple by item status?",
        ["single", "multiple"],
    )

    if dry_run:
        info_msg("Simulating collection import...")
    else:
        info_msg("Importing collection(s)...")

    # create new collection(s) using the chosen import method or preform dry run
    match import_method:
        # import single collection with all items
        case "single":
            _import_collection(collection_items, bgg_user, bgg_user, dry_run, verbose)

        # import a separate collection for each used item status
        case "multiple":
            # separate items into their respective collections
            own_items = [item for item in collection_items if item.status.own]
            prevowned_items = [
                item for item in collection_items if item.status.prevowned
            ]
            fortrade_items = [item for item in collection_items if item.status.fortrade]
            wanttoplay_items = [
                item for item in collection_items if item.status.wanttoplay
            ]
            wanttobuy_items = [
                item for item in collection_items if item.status.wanttobuy
            ]
            want_items = [item for item in collection_items if item.status.want]
            wishlist_items = [item for item in collection_items if item.status.wishlist]

            if own_items:
                _import_collection(
                    own_items, f"{bgg_user}-own", bgg_user, dry_run, verbose
                )
            if prevowned_items:
                _import_collection(
                    prevowned_items, f"{bgg_user}-prevowned", bgg_user, dry_run, verbose
                )
            if fortrade_items:
                _import_collection(
                    fortrade_items, f"{bgg_user}-fortrade", bgg_user, dry_run, verbose
                )
            if wanttoplay_items:
                _import_collection(
                    wanttoplay_items,
                    f"{bgg_user}-wanttoplay",
                    bgg_user,
                    dry_run,
                    verbose,
                )
            if wanttobuy_items:
                _import_collection(
                    wanttobuy_items, f"{bgg_user}-wanttobuy", bgg_user, dry_run, verbose
                )
            if want_items:
                _import_collection(
                    want_items, f"{bgg_user}-want", bgg_user, dry_run, verbose
                )
            if wishlist_items:
                _import_collection(
                    wishlist_items, f"{bgg_user}-wishlist", bgg_user, dry_run, verbose
                )

    if not dry_run:
        info_msg("Imported collection(s). To update, run [green]meeple update[/green]")
