import click

from bgg.util.collection_util import is_collection, delete_collection
from bgg.util.data_util import delete_data


@click.command(help="Delete a local collection.")
@click.help_option("-h", "--help")
@click.argument("name")
# TODO: add confirmation dialog/input by default, with a "-y" cli option to auto accept
def delete(name: str):
    if not is_collection(name):
        print(f"collection {name} does not exist.")
        return
    delete_collection(name)
    delete_data(name)
    print(f"{name} collection has been deleted.")
