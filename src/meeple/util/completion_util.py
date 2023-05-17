from meeple.util.collection_util import get_collection_names


def complete_collections(ctx, param, incomplete):
    return [
        collection
        for collection in get_collection_names()
        if collection.startswith(incomplete)
    ]
