import os
from dotenv import load_dotenv
from google import genai

from tools.product_tools import get_product

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def product_agent(user_query):

    products = [
        "iPhone 15 Pro",
        "Samsung Galaxy S24",
        "MacBook Pro 14",
        "Dell XPS 15"
    ]

    product_data = []

    for product_name in products:
        p = get_product(product_name)
        if p:
            product_data.append(p)

    prompt = f"""
    You are an E-commerce Product Specialist.

    Product Database:
    {product_data}

    User Question:
    {user_query}

    Instructions:
    - Answer only using product database.
    - Mention stock availability.
    - Mention price.
    - Be professional.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text