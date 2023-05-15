from enum import Enum

from rich import box
from rich.console import Console
from rich.table import Table


class ItemHeader(Enum):
    COUNT = ("#", "count")
    ID = ("ID", "id")
    NAME = ("Name", "name")
    TYPE = ("Type", "type")
    COLLECTION = ("Collection(s)", "collection")
    YEAR = ("Year", "year")
    RANK = ("Rank", "rank")
    RATING = ("Rating", "rating")
    WEIGHT = ("Weight", "weight")
    PLAYERS = ("Players", "players")
    TIME = ("Play Time", "time")


class CollectionHeader(Enum):
    NAME = ("Name", "name")
    BOARDGAMES = ("Board Games", "boardgames")
    EXPANSIONS = ("Expansions", "expansions")
    UPDATED = ("Last Updated", "updated")


def print_table(
    rows: list,
    headers: list = [],
    dim_border: bool = False,
    zebra_rows: bool = False,
    row_lines: bool = False,
) -> None:
    border_styles, row_styles = [], []
    if dim_border:
        border_styles = "dim"
    if zebra_rows:
        row_styles = ["", "dim"]

    table = Table(
        box=box.ROUNDED,
        show_header=(len(headers) != 0),
        row_styles=row_styles,
        border_style=border_styles,
        show_lines=row_lines,
    )

    for header in headers:
        table.add_column(header)
    for row in rows:
        table.add_row(*row)

    console = Console()
    console.print(table)
