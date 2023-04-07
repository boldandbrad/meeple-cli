import click

from meeple.command import (
    add,
    collections,
    completions,
    delete,
    drop,
    find,
    hot,
    info,
    list_collection,
    move,
    new,
    open_on_bgg,
    rename,
    search,
    stats,
    update,
)
from meeple.util.cmd_util import SectionedHelpGroup

commands = {
    "Collection Commands": [
        add,
        collections,
        delete,
        drop,
        find,
        list_collection,
        move,
        new,
        rename,
        stats,
        update,
    ],
    "BoardGameGeek Commands": [hot, info, open_on_bgg, search],
    "Other Commands": [completions],
}


@click.group(
    cls=SectionedHelpGroup,
    help="Local board game collection manager. Powered by BoardGameGeek.",
)
@click.help_option("-h", "--help")
@click.version_option(
    None,  # use version auto discovery
    "-v",
    "--version",
    package_name="meeple-cli",
    message="%(prog)s-cli, v%(version)s",
)
def cli() -> None:
    """Main 'meeple' command."""
    pass


for section, cmds in commands.items():
    for cmd in cmds:
        cli.add_command(cmd, section=section)

if __name__ == "__main__":
    cli()
