import os
from dotenv import load_dotenv
from google import genai

from tools.order_tools import create_order

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def order_agent(user_query):

    if "macbook" in user_query.lower():

        order = create_order("MacBook Pro 14")

        return f"""
Order Created Successfully

Order ID: {order['order_id']}
Product: {order['product']}
Quantity: {order['quantity']}
Status: {order['status']}
"""

    prompt = f"""
    You are an E-commerce Order Assistant.

    User Request:
    {user_query}

    Help the user with ordering products.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text