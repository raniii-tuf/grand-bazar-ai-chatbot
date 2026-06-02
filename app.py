import streamlit as st

import ollama

from search_db import search_products

# Page Config

st.set_page_config(

    page_title="FreshMitha AI Assistant",

    page_icon="🍬",

    layout="wide"

)

st.title("🍬 FreshMitha AI Assistant")

st.caption("Ask about sweets, pitha, fish, pickles, snacks and groceries")

# Chat History

if "messages" not in st.session_state:

    st.session_state.messages = []

# Show Previous Messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# User Input

question = st.chat_input(

    "Ask about products, prices, categories..."

)

if question:

    # Show User Message

    st.session_state.messages.append(

        {"role": "user", "content": question}

    )

    with st.chat_message("user"):

        st.markdown(question)

    # Search Products

    products = search_products(question)

    context = "\n".join(products)

    # Prompt for Llama3

    prompt = f"""

You are FreshMitha AI Assistant.

Use ONLY the product information below.

{context}

Rules:

1. Mention product names.

2. Mention prices clearly.

3. Mention category and shop if available.

4. If product is not found, say:

   "Sorry, I could not find that product in our catalog."

5. Be friendly and concise.

Customer Question:

{question}

"""

    # Call Ollama

    response = ollama.chat(

        model="llama3",

        messages=[

            {

                "role": "user",

                "content": prompt

            }

        ]

    )

    answer = response["message"]["content"]

    # Show Assistant Message

    with st.chat_message("assistant"):

        st.markdown(answer)

    st.session_state.messages.append(

        {"role": "assistant", "content": answer}

    )