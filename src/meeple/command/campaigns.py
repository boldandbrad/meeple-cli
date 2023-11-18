import click

from meeple.util.api_util import get_campaigns
from meeple.util.fmt_util import fmt_ending_date, fmt_funded
from meeple.util.output_util import TableHeader, print_table
from meeple.util.sort_util import sort_campaigns


@click.command(name="campaigns")
@click.help_option("-h", "--help")
def campaigns() -> None:
    """List active crowdfunding campaigns."""

    resp_dict = get_campaigns()

    # prepare table data
    headers = [
        TableHeader.ID,
        TableHeader.NAME,
        TableHeader.PROGRESS,
        TableHeader.BACKERS,
        TableHeader.ENDING,
    ]

    resp_dict, sort_direction = sort_campaigns(resp_dict, "ending")

    rows = []
    for item in resp_dict:
        cols = []
        cols.extend(
            [
                item["item"]["id"],
                item["name"],
                fmt_funded(item["progress"]),
                f"{item['backersCount']}",
                fmt_ending_date(item["endDate"]),
            ]
        )
        rows.append(cols)

    print_table(rows, headers, sort_key="ending", sort_direction=sort_direction)
