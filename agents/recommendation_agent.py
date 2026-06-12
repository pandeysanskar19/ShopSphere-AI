from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def recommendation_agent(user_query):

    with open("data/products.json", "r") as f:
        products = json.load(f)

    prompt = f"""
You are an expert E-Commerce Recommendation Agent.

Available Products:
{json.dumps(products, indent=2)}

Customer Query:
{user_query}

Recommend the best products.

For each recommendation provide:
1. Product Name
2. Price
3. Why it matches the customer needs
4. Final recommendation

Keep response concise and professional.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text