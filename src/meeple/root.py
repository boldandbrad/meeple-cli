import click

from meeple.command import (
    add,
    collections,
    completions,
    delete,
    drop,
    find,
    hot,
    import_,
    info,
    list_,
    move,
    new,
    open_,
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
        list_,
        move,
        new,
        rename,
        stats,
        update,
    ],
    "BoardGameGeek Commands": [hot, import_, info, open_, search],
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
