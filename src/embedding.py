from openai import OpenAI

from tqdm import tqdm
import pandas as pd

from src import config as C


client = OpenAI()

def get_embedding(text, model=C.EMBEDDING_MODEL):
    if not text:
        raise ValueError("Input text cannot be empty.")
    try:
        text = text.replace("\n", " ")
        return client.embeddings.create(input = [text], model=model).data[0].embedding
    except Exception as e:
        print(f"An error occurred in get_embedding: {e}")
        raise



def add_embeddings_to_collection(df, collection, text_column='LONG_NAME', model=C.EMBEDDING_MODEL):
    """
    Adds embeddings of the specified text column from the dataframe to the Chroma collection.

    :param df: pandas DataFrame containing the data
    :param collection: Chroma collection to add the embeddings to
    :param text_column: Column name in the dataframe containing the text to embed
    :param model: Embedding model to use
    """
    exceptions = []

    for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Processing rows"):
        text = row[text_column]
        if pd.notna(text):
            try:
                embedding = get_embedding(text, model=model)
                collection.add(
                    embeddings=[embedding],
                    metadatas=[{
                        "NAME": row.get("NAME", ""),
                        "OCS_NAME": row.get("OCS_NAME", ""),
                        "LONG_NAME": text
                    }],
                    ids=[f"id_{index}"]
                )
            except Exception as e:
                exceptions.append(f"Failed to add embedding for {text}: {e}")

    if exceptions:
        print("Exceptions occurred during processing:")
        for exception in exceptions:
            print(exception)