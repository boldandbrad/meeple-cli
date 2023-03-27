import click
from tabulate import tabulate


def fmt_rank(rank: int) -> str:
    pass


def fmt_rating(rating: float) -> str:
    rating_str = f"{rating:.2f}"
    if rating >= 8:
        return click.style(rating_str, fg="green")
    if rating >= 7:
        return click.style(rating_str, fg="blue")
    if rating > 6:
        return click.style(rating_str, fg="magenta")
    return click.style(rating_str, fg="red")


def fmt_weight(weight: float) -> str:
    weight_str = f"{weight:.2f}"
    if weight >= 4:
        return click.style(weight_str, fg="red")
    if weight >= 3:
        return click.style(weight_str, fg="yellow")
    if weight >= 2:
        return click.style(weight_str, fg="bright_yellow")
    if weight == 0:
        return click.style("NA", fg="bright_black")
    return click.style(weight_str, fg="green")


# TODO: handle column overflow/widths/alignments
def to_table(headers: list, rows: [list], grid: bool = False) -> str:
    fmt = "rounded_outline"
    if grid:
        fmt = "rounded_grid"
    return tabulate(rows, headers=headers, tablefmt=fmt, floatfmt=".2f")
