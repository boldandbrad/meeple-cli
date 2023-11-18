import click

from meeple.command import (
    add,
    campaigns,
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
from meeple.util.fs_util import check_fs

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
    "BoardGameGeek Commands": [campaigns, hot, import_, info, open_, search],
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
@click.pass_context
def cli(ctx) -> None:
    """Main 'meeple' command."""
    if check_fs():
        ctx.invoke(update, collection_names=[], force=True)


for section, cmds in commands.items():
    for cmd in cmds:
        cli.add_command(cmd, section=section)

if __name__ == "__main__":
    cli()
