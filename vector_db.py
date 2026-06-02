import pandas as pd

import chromadb

from sentence_transformers import SentenceTransformer

# Load embedding model

model = SentenceTransformer("all-MiniLM-L6-v2")

# Load CSV

df = pd.read_csv("products.csv")

# Create ChromaDB client

client = chromadb.PersistentClient(path="./chroma_db")

# Create collection

collection = client.get_or_create_collection(

    name="freshmitha_products"

)

# Add products to vector database

for index, row in df.iterrows():

    product_text = f"""

Product: {row['Product']}

Price: {row['Price']}

Description: {row['Description']}

Category: {row['Category']}

Shop: {row['Shop']}

"""

    embedding = model.encode(product_text).tolist()

    collection.add(

        ids=[str(index)],

        documents=[product_text],

        embeddings=[embedding],

        metadatas=[{

            "product": str(row['Product']),

            "price": str(row['Price']),

            "category": str(row['Category']),

            "shop": str(row['Shop'])

        }]

    )

print("✅ Products added successfully to ChromaDB")