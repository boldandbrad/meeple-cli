from typing import Any


def sortby_rank(x: dict) -> Any:
    try:
        return int(x["rank"])
    except ValueError:
        return float("inf")
