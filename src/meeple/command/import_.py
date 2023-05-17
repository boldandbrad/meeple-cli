import click

from meeple.util.api_util import get_bgg_user, get_bgg_user_collection
from meeple.util.collection_util import create_collection, unique_collection_name
from meeple.util.input_util import choice_input
from meeple.util.message_util import error_msg, info_msg, print_msg


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
            # assign a unique collection name
            collection_name = unique_collection_name(username)
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
                    f"Imported [magenta]{username}[/magenta]'s BoardGameGeek collection to collection [u magenta]{collection_name}[/u magenta]. To update, run [green]meeple update[/green]"
                )
        # import a separate collection for each used item status
        case "multiple":
            own = []
            prevowned = []
            fortrade = []
            wanttoplay = []
            wanttobuy = []
            want = []
            wishlist = []
            for item in collection_items:
                if item.status.own:
                    own.append(item)
                if item.status.prevowned:
                    prevowned.append(item)
                if item.status.fortrade:
                    fortrade.append(item)
                if item.status.wanttoplay:
                    wanttoplay.append(item)
                if item.status.wanttobuy:
                    wanttobuy.append(item)
                if item.status.want:
                    want.append(item)
                if item.status.wishlist:
                    wishlist.append(item)

            print("coming soon...")
