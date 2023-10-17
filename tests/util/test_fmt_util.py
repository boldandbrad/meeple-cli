from meeple.util.api_util import BOARDGAME_TYPE, EXPANSION_TYPE
from meeple.util.fmt_util import (
    NA_VALUE,
    fmt_avg_rank,
    fmt_item_type,
    fmt_players,
    fmt_playtime,
    fmt_rank,
    fmt_rating,
    fmt_weight,
    fmt_year,
)


def test_fmt_players():
    na_output = fmt_players(0, 0)
    assert na_output == NA_VALUE

    output = fmt_players(1, 2)
    assert output == "1-2"


def test_fmt_playtime():
    na_output = fmt_playtime(0)
    assert na_output == NA_VALUE

    output = fmt_playtime(30)
    assert output == "~30 Min"


def test_fmt_avg_rank():
    na_output = fmt_avg_rank("Not Ranked")
    assert na_output == NA_VALUE

    na_output_2 = fmt_avg_rank(0)
    assert na_output_2 == NA_VALUE

    output = fmt_avg_rank(50.3444)
    assert output == "50.34"


def test_fmt_rank():
    na_output = fmt_rank(0)
    assert na_output == NA_VALUE

    output = fmt_rank(50)
    assert output == "50"


def test_fmt_rating():
    na_output = fmt_rating(0)
    assert na_output == NA_VALUE

    green_output = fmt_rating(8.5)
    assert green_output == "[green]8.50[/green]"

    blue_output = fmt_rating(7.5)
    assert blue_output == "[blue]7.50[/blue]"

    purple_output = fmt_rating(6.5)
    assert purple_output == "[magenta]6.50[/magenta]"

    red_output = fmt_rating(5.5)
    assert red_output == "[red]5.50[/red]"


def test_fmt_item_type():
    na_output = fmt_item_type("other")
    assert na_output == NA_VALUE

    bg_output = fmt_item_type(BOARDGAME_TYPE)
    assert bg_output == "Board Game"

    ex_output = fmt_item_type(EXPANSION_TYPE)
    assert ex_output == "Expansion"


def test_fmt_weight():
    na_output = fmt_weight(0)
    assert na_output == NA_VALUE

    red_output = fmt_weight(4.5)
    assert red_output == "[red]4.50[/red]"

    orange_output = fmt_weight(3.5)
    assert orange_output == "[yellow]3.50[/yellow]"

    yellow_output = fmt_weight(2.5)
    assert yellow_output == "[bright_yellow]2.50[/bright_yellow]"

    green_output = fmt_weight(1.5)
    assert green_output == "[green]1.50[/green]"


def test_fmt_year():
    na_output = fmt_year(0)
    assert na_output == NA_VALUE

    other_output = fmt_year("2000")
    assert other_output == "2000"
