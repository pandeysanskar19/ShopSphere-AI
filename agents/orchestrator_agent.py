# Gemini-powered Router Agent
# Classifies user intent and delegates tasks
# to specialized AI agents.


import os

from dotenv import load_dotenv
from google import genai

from agents.product_agent import product_agent
from agents.recommendation_agent import recommendation_agent
from agents.order_agent import order_agent

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def classify_intent(user_query):
    try:
        prompt = f"""
You are an intent classification system.

Classify the user query into exactly ONE category:

product
recommendation
order

Rules:

product
- asking price
- asking stock
- asking availability
- asking specifications
- asking product details

recommendation
- asking suggestions
- asking recommendations
- asking best product

order
- wants to buy
- wants to purchase
- wants to place an order
- wants checkout

Examples:

What is the price of MacBook Pro?
product

Tell me about iPhone 15
product

Suggest a laptop for AI development
recommendation

Best laptop for coding
recommendation

I want to buy MacBook Pro
order

Place an order for iPhone 15
order

Purchase Dell XPS 15
order

User Query:
{user_query}

Return ONLY:
product
recommendation
order
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip().lower()

    except Exception:
        query = user_query.lower()

        if any(word in query for word in [
            "buy",
            "order",
            "purchase",
            "checkout"
        ]):
            return "order"

        elif any(word in query for word in [
            "recommend",
            "suggest",
            "best"
        ]):
            return "recommendation"

        return "product"


def orchestrator_agent(user_query):

    intent = classify_intent(user_query)

    print(f"\n[ROUTER] Intent = {intent}")

    if "order" in intent:
        return order_agent(user_query)

    elif "recommend" in intent:
        return recommendation_agent(user_query)

    else:
        return product_agent(user_query)