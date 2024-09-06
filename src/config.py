import os
import openai
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from openai import OpenAI


openai.api_key = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4o"
client = OpenAI()

chroma_client = chromadb.PersistentClient(path="./chromadb/")
embedding_function = OpenAIEmbeddingFunction(api_key=os.environ.get('OPENAI_API_KEY'), model_name=EMBEDDING_MODEL)
product_matcher_collection_name="cd-product_matcher"
existing_collections = chroma_client.list_collections()
if product_matcher_collection_name in [col.name for col in existing_collections]:
    product_matcher_collection = chroma_client.get_collection(name=product_matcher_collection_name)
else:
    product_matcher_collection = chroma_client.create_collection(
        name=product_matcher_collection_name, 
        metadata={"hnsw:space": "cosine"},
        embedding_function=embedding_function
    )

internal_product_csv_path = './data/Data_Internal.csv'
