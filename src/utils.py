from src import config as C


def get_chromadb_collection():
    ## Loading Collection:
    product_matcher_collection = C.chroma_client.get_collection(name=C.product_matcher_collection, embedding_function=C.embedding_function)

    return product_matcher_collection


def get_data_count(collection=C.product_matcher_collection):
    return collection.count()

