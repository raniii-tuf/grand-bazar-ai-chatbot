import chromadb

from sentence_transformers import SentenceTransformer

# Load embedding model

model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB

client = chromadb.PersistentClient(path="./chroma_db")

# Open collection

collection = client.get_collection(

    name="freshmitha_products"

)

def search_products(query, n_results=5):

    # Convert query to embedding

    query_embedding = model.encode(query).tolist()

    # Search ChromaDB

    results = collection.query(

        query_embeddings=[query_embedding],

        n_results=n_results

    )

    return results["documents"][0]

# Test search directly

if __name__ == "__main__":

    while True:

        question = input("\nAsk: ")

        if question.lower() in ["exit", "quit"]:

            break

        products = search_products(question)

        print("\nResults:\n")

        for product in products:

            print(product)

            print("-" * 50)