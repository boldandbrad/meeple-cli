from meeple.util.collection_util import get_collections


def complete_collections(ctx, param, incomplete):
    return [
        collection
        for collection in get_collections()
        if collection.startswith(incomplete)
    ]
