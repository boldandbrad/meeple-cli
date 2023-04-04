import numbers

from rich import box
from rich.console import Console
from rich.table import Table


def fmt_players(minplayers: str, maxplayers: str) -> str:
    return f"{minplayers}-{maxplayers}"


def fmt_playtime(minplaytime: str, maxplaytime: str) -> str:
    return f"{minplaytime}-{maxplaytime} Min"


def fmt_avg_rank(rank: str) -> str:
    if not isinstance(rank, numbers.Number) or int(rank) == 0:
        return "[bright_black]NA[/bright_black]"
    rank_str = f"{rank:.2f}"
    return rank_str


def fmt_rank(rank: str) -> str:
    if rank == "NA" or not rank.isdigit():
        return "[bright_black]NA[/bright_black]"
    return rank


def fmt_rating(rating: float) -> str:
    rating_str = f"{rating:.2f}"
    if rating >= 8:
        return f"[green]{rating_str}[/green]"
    if rating >= 7:
        return f"[blue]{rating_str}[/blue]"
    if rating > 6:
        return f"[magenta]{rating_str}[/magenta]"
    if rating == 0:
        return "[bright_black]NA[/bright_black]"
    return f"[red]{rating_str}[/red]"


def fmt_weight(weight: float) -> str:
    weight_str = f"{weight:.2f}"
    if weight >= 4:
        return f"[red]{weight_str}[/red]"
    if weight >= 3:
        return f"[yellow]{weight_str}[/yellow]"
    if weight >= 2:
        return f"[bright_yellow]{weight_str}[/bright_yellow]"
    if weight == 0:
        return "[bright_black]NA[/bright_black]"
    return f"[green]{weight_str}[/green]"


def print_error(message: str) -> None:
    print_table([["[red]Error[/red]", message]])


def print_info(message: str) -> None:
    print_table([[message]])


def print_warning(message: str) -> None:
    print_table([["[yellow]Warning[/yellow]", message]])


def print_table(
    rows: list, headers: list = [], lines: bool = False, zebra: bool = False
) -> None:
    row_styles = []
    if zebra:
        row_styles = ["", "dim"]
    table = Table(
        box=box.ROUNDED,
        show_header=(len(headers) != 0),
        show_lines=lines,
        row_styles=row_styles,
    )
    for header in headers:
        table.add_column(header)
    for row in rows:
        table.add_row(*row)
    console = Console()
    console.print(table)
