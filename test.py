from search_db import search_products

print("FreshMitha Product Search Test")

print("Type 'exit' to quit")

while True:

    query = input("\nAsk: ")

    if query.lower() == "exit":

        break

    results = search_products(query)

    print("\nResults:\n")

    for result in results:

        print(result)

        print("-" * 50)