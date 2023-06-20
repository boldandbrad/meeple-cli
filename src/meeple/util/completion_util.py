from meeple.util.collection_util import get_collection_names


def complete_collections(ctx, param, incomplete):
    return [
        collection_name
        for collection_name in get_collection_names()
        if collection_name.startswith(incomplete)
    ]
