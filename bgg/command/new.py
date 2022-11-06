import click

from bgg.util.collection_util import is_collection, create_collection


@click.command(help="Create a new local collection.")
@click.help_option("-h", "--help")
@click.argument("name")
def new(name: str):
    if is_collection(name):
        print(f"collection {name} already exists.")
        return
    create_collection(name)
    print(f"{name} collection created.")
