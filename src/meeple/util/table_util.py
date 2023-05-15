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
    BOARDGAMES = ("Boardgames", "boardgames")
    EXPANSIONS = ("Expansions", "expansions")
    UPDATED = ("Last Updated", "updated")


def print_table(
    rows: list,
    headers: list = [],
    lines: bool = False,
    dim_border: bool = False,
    zebra: bool = False,
) -> None:
    row_styles = []
    border_styles = []
    if zebra:
        row_styles = ["", "dim"]
    if dim_border:
        border_styles = "dim"
    table = Table(
        box=box.ROUNDED,
        show_header=(len(headers) != 0),
        show_lines=lines,
        row_styles=row_styles,
        border_style=border_styles,
    )
    for header in headers:
        table.add_column(header)
    for row in rows:
        table.add_row(*row)
    console = Console()
    console.print(table)
