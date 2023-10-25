import sys

from rich.console import Console

from meeple.util.output_util import print_table


def print_msg(message: str) -> None:
    console = Console()
    console.print(message)


def under_msg(message: str, indents: int = 1) -> None:
    spaces = indents * "  "
    print_msg(f"{spaces}[dim]╰╴[/dim][default]{message}[/default]")


def error_msg(message: str) -> None:
    """Print error message and exit."""
    sys.exit(print_table([["[red]Error[/red]", message]], dim_border=True))


def info_msg(message: str) -> None:
    print_table([[message]], dim_border=True)


def warn_msg(message: str) -> None:
    print_table([["[yellow]Warning[/yellow]", message]], dim_border=True)


# common error messages
def invalid_id_error(bgg_id: str) -> None:
    error_msg(f"[yellow]{bgg_id}[/yellow] is not a valid BoardGameGeek ID.")


def invalid_collection_error(collection: str) -> None:
    error_msg(f"[yellow]{collection}[/yellow] is not a valid collection.")


def no_collections_exist_error() -> None:
    error_msg("No collections yet exist. To create one, run: [green]meeple new[/green]")
