import click


@click.command(help="CLI passkey maker.")
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

    print("welcome to bgg-cli")
