
import pandas as pd
import json

from src import prompts as P
from src import config as C


def query_collection(collection, query, max_results):
    """
    Queries the Chroma collection and returns the top results with metadata.

    :param collection: Chroma collection to query
    :param query: Query text
    :param max_results: Maximum number of results to return
    :return: DataFrame with the top results including NAME, OCS_NAME, and LONG_NAME
    """
    results = collection.query(query_texts=[query], n_results=max_results, include=['distances', 'metadatas'])
    
    # Flatten the results
    ids = results['ids'][0]
    scores = results['distances'][0]
    metadatas = results['metadatas'][0]
    
    # Create a DataFrame with the results
    result_df = pd.DataFrame({
        'id': ids,
        'score': scores,
        'NAME': [metadata.get('NAME', '') for metadata in metadatas],
        'OCS_NAME': [metadata.get('OCS_NAME', '') for metadata in metadatas],
        'LONG_NAME': [metadata.get('LONG_NAME', '') for metadata in metadatas]
    })
    
    return result_df


def match_products_and_get_response(external_product_information, potential_matching_internal_products):
    """
    Matches products using the OpenAI API and returns the response in JSON format.

    :param external_product_information: Information about the external product
    :param potential_matching_internal_products: List of potentially matching internal products
    :return: JSON response with match information
    """
    # Format the user prompt
    user_prompt = f"""
    Here is the external product information:
    {external_product_information}
    
    Here is the list of potentially matching:
    {potential_matching_internal_products}
    
    Please note that the response needs to be in json and in the required format.
    """
    
    # Call the OpenAI API
    try:
        messages = [
                {"role": "system", "content": P.SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ]

        # Call the chat completion endpoint with the constructed messages
        response = C.client.chat.completions.create(
            model=C.LLM_MODEL,
            messages=messages,
            response_format={'type': 'json_object'}
        )

        # Extract and parse the response
        response_content = response.choices[0].message.content
        response_json = json.loads(response_content)

        return response_json

    except json.JSONDecodeError as e:
        print(f"Error decoding the JSON format: {e}")
        return {"is_matched": False, "match": "NULL"}
    except Exception as e:
        print(f"An error occurred while calling the OpenAI API: {e}")
        return {"is_matched": False, "match": "NULL"}
    



def match_product_name(external_product_information, collection = C.product_matcher_collection):
    """
    Main process to match external product information with internal products.

    :param external_product_information: Information about the external product
    :param collection: ChromaDB collection to query
    :param internal_product_list: DataFrame of internal products
    :return: JSON response with match information
    """
    # Query the collection to get the top 10 matches
    max_results = 10
    top_results = query_collection(collection, external_product_information, max_results)
    
    # Extract relevant fields for the top 10 matches
    potential_matching_internal_products = top_results[['NAME', 'OCS_NAME', 'LONG_NAME']].head(max_results).to_dict(orient='records')
    
    # Format the potential matching internal products as a string
    potential_matching_internal_products_str = "\n".join(
        [f"NAME: {item['NAME']}, OCS_NAME: {item['OCS_NAME']}, LONG_NAME: {item['LONG_NAME']}" for item in potential_matching_internal_products]
    )
    
    # Get the response from the match_products_and_get_response function
    response = match_products_and_get_response(external_product_information, potential_matching_internal_products_str)
    
    return response['match']