import streamlit as st
import pandas as pd
import io
from src import matcher 
from src import utils as U

from src import config as C
from src import embedding as E

def process_csv(file):
    """
    Processes the uploaded CSV file by adding a new column with matched product names.

    :param file: Uploaded CSV file
    :return: Processed DataFrame
    """
    df = pd.read_csv(file)
    progress_bar = st.progress(0)
    total_rows = len(df)
    
    for i, row in df.iterrows():
        df.at[i, 'Internal Product Name'] = matcher.match_product_name(row['PRODUCT_NAME'])
        progress_bar.progress((i + 1) / total_rows)
    
    return df

def process_and_embed(csv_data, collection_name, embedding_function):
    internal_product_list = pd.read_csv(csv_data)
    
    # Check if the collection already exists
    existing_collections = C.chroma_client.list_collections()
    product_matcher_collection = C.chroma_client.get_collection(name=collection_name)

    
    E.add_embeddings_to_collection(internal_product_list, product_matcher_collection)

# Streamlit app layout
st.title("Compass Digital - Home Assignment")

# Display total amount of Internal Product Entries
st.sidebar.title("Internal Product Entries")
st.sidebar.write(f"Total Internal Product Entries: {U.get_data_count()}")

# Sidebar with usage instructions
st.sidebar.title("How to Use")
st.sidebar.write("""
1. **Product Name Matcher**: Enter the external product name in the input box and click "Match Product" to find the corresponding internal product name.
2. **Bulk Product Matching**: Upload a CSV file containing external product names. Click "Process and Download CSV" to get a new CSV file with matched internal product names.
3. **Bulk Data Loading**: Upload a CSV file and click "Process and Embed CSV" to process and embed the data.
""")

# Highlighted note
st.sidebar.markdown("""
Note: Please note that the external product name in the csv should have a column name called 'PRODUCT_NAME'.
""")


# Sidebar with submission information
st.sidebar.title("Submitted by")
st.sidebar.write("Raoof Naushad")
st.sidebar.write("email: raoofnaushad.7@gmail.com")
st.sidebar.write("contact: +19029897685")

# Input area for external product name
st.header("Product Name Matcher")
external_name = st.text_input("Enter External Product Name to match with Internal Products:")
if st.button("Match Product"):
    internal_name = matcher.match_product_name(external_name)
    if internal_name == "NULL":
        st.write("Match Not Found")
    else:
        st.write(f"Internal Product Name: {internal_name}")
        st.balloons()  # Celebration effect when a match is found

# File upload area for CSV files
st.header("Bulk Product Matching")
uploaded_file = st.file_uploader("Upload a CSV file for Product Matching", type=["csv"])
if uploaded_file is not None:
    if st.button("Process and Download CSV"):
        processed_df = process_csv(uploaded_file)
        csv = processed_df.to_csv(index=False)
        st.download_button(
            label="Download Processed CSV",
            data=csv,
            file_name="processed_file.csv",
            mime="text/csv"
        )

st.header("Bulk Data Loading")
uploaded_file_embed = st.file_uploader("Upload a CSV file for Data Loading", type=["csv"])
if uploaded_file_embed is not None:
    if st.button("Process and Embed CSV"):
        with st.spinner('Processing and embedding...'):
            process_and_embed(uploaded_file_embed, C.product_matcher_collection_name, C.embedding_function)
        st.success('Processing and embedding completed!')
        st.balloons()