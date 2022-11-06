import click

from bgg.util.collection_util import is_collection, delete_collection


@click.command(help="Delete a local collection.")
@click.help_option("-h", "--help")
@click.argument("name")
def delete(name: str):
    if not is_collection(name):
        print(f"collection {name} does not exist.")
        return
    delete_collection(name)
    print(f"{name} collection has been deleted.")
