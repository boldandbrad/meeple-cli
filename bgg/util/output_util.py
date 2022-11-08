import click
from tabulate import tabulate


def color_weight(weight: float) -> str:
    if weight >= 4:
        return click.style(weight, fg="red")
    if weight >= 3:
        return click.style(weight, fg="yellow")
    if weight >= 2:
        return click.style(weight, fg="bright_yellow")
    return click.style(weight, fg="green")


def color_rating(rating: float) -> str:
    if rating >= 8:
        return click.style(rating, fg="green")
    if rating >= 7:
        return click.style(rating, fg="blue")
    if rating > 6:
        return click.style(rating, fg="magenta")
    return click.style(rating, fg="red")


# TODO: handle column overflow/widths
def table(headers: list, rows: [list], grid: bool = False) -> str:
    fmt = "rounded_outline"
    if grid:
        fmt = "rounded_grid"
    return tabulate(rows, headers=headers, tablefmt=fmt)
