from enum import Enum

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.table import Table

# tables


def _fmt_header(header, sort_direction: str):
    return f"{header.value[0]} {sort_direction}"


class TableHeader(Enum):
    # general
    COUNT = ("#", "count", "right")
    ID = ("ID", "id", "right")
    NAME = ("Name", "name", "left")

    # items
    TYPE = ("Type", "type", "left")
    COLLECTION = ("Collection(s)", "collection", "left")
    YEAR = ("Year", "year", "right")
    RANK = ("Rank", "rank", "right")
    RATING = ("Rating", "rating", "right")
    WEIGHT = ("Weight", "weight", "right")
    PLAYERS = ("Players", "players", "right")
    MAX_PLAYERS = ("Max Players", "maxplayers", "right")
    TIME = ("Play Time", "time", "right")

    # collections
    BOARDGAMES = ("Board Games", "boardgames", "right")
    EXPANSIONS = ("Expansions", "expansions", "right")
    UPDATED = ("Last Updated", "updated", "left")

    # campaigns
    BACKERS = ("Backers", "backers", "right")
    PROGRESS = ("Progress", "progress", "right")
    ENDING = ("Ending", "ending", "left")


def print_table(
    rows: list,
    headers: list = [],
    sort_key: str = None,
    sort_direction: str = None,
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
        header_title = header.value[0]
        if sort_key and sort_direction and header.value[1] == sort_key:
            header_title = f"{header_title} {sort_direction}"
        table.add_column(header_title, justify=header.value[2])
    for row in rows:
        table.add_row(*row)

    console = Console()
    console.print(table)


# progress bars


class CustomProgress(Progress):
    def __init__(self, outlined: bool = True):
        self.outlined = outlined
        super().__init__(
            TextColumn("{task.description}"),
            BarColumn(pulse_style="magenta"),
            SpinnerColumn(),
            transient=True,
        )

    def get_renderables(self):
        if self.outlined:
            yield Panel(
                self.make_tasks_table(self.tasks),
                box=box.ROUNDED,
                expand=False,
                border_style="dim",
            )
        else:
            yield super().get_renderables()
