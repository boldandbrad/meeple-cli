import click

from bgg.util.collection_util import is_collection, delete_collection
from bgg.util.data_util import get_data, delete_data
from bgg.util.input_util import bool_input


@click.command(help="Delete a local collection.")
@click.help_option("-h", "--help")
@click.argument("name")
@click.option("-y", "--yes", is_flag=True, help="Dangerous - Bypass confirmation.")
def delete(name: str, yes: bool):
    if not is_collection(name):
        print(f"collection {name} does not exist.")
        return
    if not yes:
        confirmation = bool_input(f"Are you sure you want to delete {name}?")
    else:
        confirmation = True
    if confirmation:
        delete_collection(name)
        data = get_data(name)
        if data:
            delete_data(name)
        print(f"{name} collection has been deleted.")
