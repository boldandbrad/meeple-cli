import click

from os.path import splitext

from bgg.util.collection_util import get_collections


@click.command(help="List all local collections.")
@click.help_option("-h", "--help")
# @click.option("-v", "--verbose", is_flag=True) # print number of games and some stats alongside the collection name
def collections():
    # process each data source file
    collections = get_collections()
    for collection in collections:
        print(collection)
