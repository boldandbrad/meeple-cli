import numbers

import arrow

from meeple.util.api_util import BOARDGAME_TYPE, EXPANSION_TYPE

NA_VALUE = "[dim]NA[/dim]"

SORT_ASC_SYMBOL = "[blue]˄[/blue]"
SORT_DESC_SYMBOL = "[blue]˅[/blue]"


def fmt_cmd(command: str) -> str:
    return f"[green]{command}[/green]"


def fmt_ending_date(date: str) -> str:
    date_obj = arrow.get(date)
    friendly_date = date_obj.humanize()
    if "hour" in friendly_date:
        return f"[red]{friendly_date}[/red]"
    elif "day" in friendly_date:
        return f"[yellow]{date_obj.format('MMM D')}[/yellow]"
    return date_obj.format("MMM D")


def fmt_funded(progress: int) -> str:
    if progress >= 100:
        return f"[green]{progress}%[/green]"
    return f"{progress}%"


def fmt_players(minplayers: str, maxplayers: str) -> str:
    if int(minplayers) == int(maxplayers) == 0:
        return NA_VALUE
    return f"{minplayers}-{maxplayers}"


def fmt_playtime(playtime: str) -> str:
    if int(playtime) == 0:
        return NA_VALUE
    return f"~{playtime} Min"


def fmt_avg_rank(rank: str) -> str:
    if not isinstance(rank, numbers.Number) or int(rank) == 0:
        return NA_VALUE
    rank_str = f"{rank:.2f}"
    return rank_str


def fmt_rank(rank: int) -> str:
    if rank == 0:
        return NA_VALUE
    return str(rank)


def fmt_rating(rating: float) -> str:
    rating_str = f"{rating:.2f}"
    if rating >= 8:
        return f"[green]{rating_str}[/green]"
    if rating >= 7:
        return f"[blue]{rating_str}[/blue]"
    if rating > 6:
        return f"[magenta]{rating_str}[/magenta]"
    if rating == 0:
        return NA_VALUE
    return f"[red]{rating_str}[/red]"


def fmt_item_type(item_type: str) -> str:
    if item_type == BOARDGAME_TYPE:
        return "Board Game"
    if item_type == EXPANSION_TYPE:
        return "Expansion"
    return NA_VALUE


def fmt_weight(weight: float) -> str:
    weight_str = f"{weight:.2f}"
    if weight >= 4:
        return f"[red]{weight_str}[/red]"
    if weight >= 3:
        return f"[yellow]{weight_str}[/yellow]"
    if weight >= 2:
        return f"[bright_yellow]{weight_str}[/bright_yellow]"
    if weight == 0:
        return NA_VALUE
    return f"[green]{weight_str}[/green]"


def fmt_year(year: str) -> str:
    if int(year) == 0:
        return NA_VALUE
    return year
