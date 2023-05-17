import click

from meeple.util.api_util import get_bgg_user, get_bgg_user_collection
from meeple.util.collection_util import create_collection, unique_collection_name
from meeple.util.input_util import choice_input
from meeple.util.message_util import error_msg, info_msg, print_msg


def _import_collection(collection_items, collection_name, username, dry_run) -> None:
    # assign a unique collection name
    collection_name = unique_collection_name(collection_name)
    # show expected changes if import were performed
    if dry_run:
        info_msg(
            f"Import collection [u magenta]{collection_name}[/u magenta] containing {len(collection_items)} items."
        )
        for item in collection_items:
            print_msg(
                f" ╰╴ [i blue]{item.name}[/i blue] ([default dim]{item.bgg_id}[/default dim])"
            )
    # perform import
    else:
        collection_ids = [item.bgg_id for item in collection_items]
        create_collection(collection_name, to_add_ids=collection_ids)
        info_msg(
            f"Imported [magenta]{username}[/magenta]'s BoardGameGeek collection [u magenta]{collection_name}[/u magenta] containing {len(collection_items)} items. To update, run [green]meeple update[/green]"
        )


@click.command(name="import")
@click.option("--username", required=True)
@click.option("--dry-run", is_flag=True)
@click.help_option("-h", "--help")
# TODO: add dry-run option to show what collections and items would be created without persisting changes
# TODO: add single/multiple options or a flag to bypass import method prompt
def import_(username: str, dry_run: bool) -> None:
    """Import BoardGameGeek user collections."""
    # check that the given username is a valid BoardGameGeek username
    user = get_bgg_user(username)
    if not user.user_id:
        error_msg(f"[yellow]{username}[/yellow] is not a valid BoardGameGeek username.")

    # get user collection items
    collection_items = get_bgg_user_collection(username)

    # check that the user collection is not empty
    if not collection_items:
        error_msg(
            f"Nothing to import. BoardGameGeek user [yellow]{username}[/yellow]'s collection is empty."
        )

    # prompt to user for import method
    import_method = choice_input(
        f"Would you like to import [magenta]{username}[/magenta]'s user collection items into a single collection or into multiple by item status?",
        ["single", "multiple"],
    )

    # create new collection(s) using the chosen import method
    match import_method:
        # import single collection with all items
        case "single":
            _import_collection(collection_items, username, username, dry_run)

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
                _import_collection(own_items, f"{username}-own", username, dry_run)
            if prevowned_items:
                _import_collection(
                    prevowned_items, f"{username}-prevowned", username, dry_run
                )
            if fortrade_items:
                _import_collection(
                    fortrade_items, f"{username}-fortrade", username, dry_run
                )
            if wanttoplay_items:
                _import_collection(
                    wanttoplay_items, f"{username}-wanttoplay", username, dry_run
                )
            if wanttobuy_items:
                _import_collection(
                    wanttobuy_items, f"{username}-wanttobuy", username, dry_run
                )
            if want_items:
                _import_collection(want_items, f"{username}-want", username, dry_run)
            if wishlist_items:
                _import_collection(
                    wishlist_items, f"{username}-wishlist", username, dry_run
                )
