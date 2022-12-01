import click
from tabulate import tabulate


def color_weight(weight: float) -> str:
    weight_str = f"{weight:.2f}"
    if weight >= 4:
        return click.style(weight_str, fg="red")
    if weight >= 3:
        return click.style(weight_str, fg="yellow")
    if weight >= 2:
        return click.style(weight_str, fg="bright_yellow")
    return click.style(weight_str, fg="green")


def color_rating(rating: float) -> str:
    rating_str = f"{rating:.2f}"
    if rating >= 8:
        return click.style(rating_str, fg="green")
    if rating >= 7:
        return click.style(rating_str, fg="blue")
    if rating > 6:
        return click.style(rating_str, fg="magenta")
    return click.style(rating_str, fg="red")


# TODO: handle column overflow/widths
def table(headers: list, rows: [list], grid: bool = False) -> str:
    fmt = "rounded_outline"
    if grid:
        fmt = "rounded_grid"
    return tabulate(rows, headers=headers, tablefmt=fmt, floatfmt=".2f")
