<div align="center">

# 🛍️ ShopSphere AI

### Gemini-Powered Multi-Agent E-Commerce Assistant

*Ask anything. Get products, recommendations, and orders — instantly.*

<p>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Gemini_2.5_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Multi--Agent_AI-8A2BE2?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-Custom-green?style=for-the-badge"/>
</p>

</div>


## 🤔 What is ShopSphere AI?

ShopSphere AI is an intelligent e-commerce assistant that **understands what you want and acts on it**.

You type a message like *"Find me wireless headphones under ₹3000"* — and instead of showing you a search bar, ShopSphere AI routes your request to the right AI agent, fetches results, and responds conversationally.

It uses **Google Gemini 2.5 Flash** as the brain, with **4 specialized agents** working together behind the scenes.


## ✨ What Can It Do?

| You Say | ShopSphere Does |
|---|---|
| *"Show me laptops under ₹50,000"* | Searches and lists matching products |
| *"What should I buy based on my interests?"* | Gives personalized recommendations |
| *"Place an order for the Nike shoes"* | Confirms and places your order |
| *"Where is my order #1042?"* |shows order status |


## 🏗️ How It Works

```
You type a message
        │
        ▼
┌──────────────────────┐
│   Gemini Router Agent │  ← Understands your intent
└──────────┬───────────┘
           │
    ┌──────┼──────────────────┐
    ▼      ▼                  ▼
┌────────┐ ┌───────────────┐ ┌───────────┐
│Product │ │Recommendation │ │  Order    │
│ Agent  │ │    Agent      │ │  Agent    │
└────────┘ └───────────────┘ └───────────┘
    │              │               │
    └──────────────┴───────────────┘
                   │
            JSON Database
                   │
                   ▼
          Answer shown in chat
```

### The 4 Agents

| Agent | What It Does |
|---|---|
| 🧭 **Router Agent** | Reads your message and decides which agent should handle it |
| 🛍️ **Product Agent** | Searches the product catalog and returns matching items |
| 💡 **Recommendation Agent** | Suggests products based on your preferences and history |
| 📦 **Order Agent** | Places orders, tracks status, and manages your purchases |


## 🛠️ Tech Stack

| What | Technology Used |
|---|---|
| AI Model | Google Gemini 2.5 Flash |
| Backend | Python 3.10+ |
| Frontend | Streamlit |
| Database | JSON (file-based) |
| Testing | Python unittest |



## 📁 Project Structure

```
ShopSphere-AI/
│
├── agents/
│   ├── router_agent.py            # Routes user queries to the right agent
│   ├── product_agent.py           # Handles product search
│   ├── recommendation_agent.py    # Handles personalized suggestions
│   └── order_agent.py             # Handles orders and tracking
│
├── tools/                         # Shared helper functions
├── data/                          # Product and order JSON database
│
├── tests/
│   ├── test_router_agent.py
│   ├── test_product_agent.py
│   ├── test_recommendation_agent.py
│   └── test_order_agent.py
│
├── assets/                        # Images and UI assets
├── main.py                        # App entry point
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment variable
├──README.md
```

---

## 🚀 Run It Locally

**Step 1 — Clone the project**
```bash
git clone https://github.com/pandeysanskar19/ShopSphere-AI
cd ShopSphere-AI
```

**Step 2 — Create a virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**Step 3 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 4 — Add your API key**
```bash
cp .env.example .env
# Open .env and add your GEMINI_API_KEY
```

**Step 5 — Start the app**
```bash
streamlit run main.py
```

Open your browser at `http://localhost:8501` and start chatting 🎉

---

## 🧪 Run Tests

```bash
# Test individual agents
python -m tests.test_router_agent
python -m tests.test_product_agent
python -m tests.test_recommendation_agent
python -m tests.test_order_agent

# Run all tests at once
python -m pytest tests/
```

---

## 🔭 What's Coming Next

- [ ] Persistent user profiles and purchase history
- [ ] Semantic product search using vector database (FAISS / ChromaDB)
- [ ] Multi-turn memory across agent conversations
- [ ] Payment gateway simulation
- [ ] Deployment on Google Cloud Run

---

## 👥 Built By

| Name | Role |
|---|---|
| **Sanskar Pandey** | Lead Developer|
| **Shashmit Mishra** | Co-Developer |

B.Tech CSE (AI Specialization) — Pranveer Singh Institute Of Technology — AKTU University, 2028

For any Collaboration,contact:
Mail id:pandeysanskar1809@gmail.com

LinkedIn : https://www.linkedin.com/in/sanskar-pandey-b43689326/

## 📄 License

This project is protected under a **Custom Source License**.
- You can clone, study, and contribute
- You cannot sell, monetize, or deploy commercially without permission

See [LICENSE](LICENSE) for full details.



<div align="center">
  <i>Built with ❤️ using Google Gemini · Streamlit · Python</i>
</div>
