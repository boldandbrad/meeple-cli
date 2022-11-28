import click

from bgg.command import (
    add,
    collections,
    delete,
    drop,
    hot,
    info,
    list_collection,
    move,
    new,
    open_on_bgg,
    search,
    stats,
    update,
)


@click.group(help="Local BoardGameGeek collection manager.")
@click.help_option("-h", "--help")
@click.version_option(
    None,  # use version auto discovery via setuptools
    "-v",
    "--version",
    package_name="bgg-cli",
    message="%(prog)s-cli, v%(version)s",
)
def cli():
    """Main 'bgg' command."""
    pass


cli.add_command(add, "add")
cli.add_command(collections, "collections")
cli.add_command(delete, "delete")
cli.add_command(drop, "drop")
cli.add_command(info, "info")
cli.add_command(hot, "hot")
cli.add_command(list_collection, "list")
cli.add_command(move, "move")
cli.add_command(new, "new")
cli.add_command(open_on_bgg, "open")
cli.add_command(search, "search")
cli.add_command(stats, "stats")
cli.add_command(update, "update")

if __name__ == "__main__":
    cli()
