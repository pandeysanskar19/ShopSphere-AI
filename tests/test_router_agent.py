from agents.orchestrator_agent import orchestrator_agent

queries = [

    "What is the price of MacBook Pro 14?",

    "Suggest a laptop for AI development",

    "I want to buy MacBook Pro 14"

]

for query in queries:

    print("\n" + "="*60)
    print("USER:", query)
    print("="*60)

    response = orchestrator_agent(query)

    print(response)