import streamlit as st
from agents.orchestrator_agent import orchestrator_agent

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="ShopSphere AI",
    page_icon="🛒",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.main-title{
    text-align:center;
    font-size:3rem;
    font-weight:700;
    margin-bottom:0;
}

.sub-title{
    text-align:center;
    color:#9ca3af;
    font-size:1.1rem;
    margin-bottom:2rem;
}

.feature-card{
    border:1px solid rgba(255,255,255,0.1);
    border-radius:15px;
    padding:20px;
    text-align:center;
    background-color:rgba(255,255,255,0.03);
}

.footer{
    text-align:center;
    color:gray;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    """
    <div class="main-title">
        🛒 ShopSphere AI
    </div>

    <div class="sub-title">
        Gemini-Powered Multi-Agent E-Commerce Assistant
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# FEATURE SECTION
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📦 Product Agent</h3>
        <p>Product Search, Pricing & Inventory Lookup</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🎯 Recommendation Agent</h3>
        <p>AI-Powered Personalized Product Suggestions</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>🛍️ Order Agent</h3>
        <p>Order Creation & Management</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🤖 System Info")

    st.success("Gemini Router Agent")

    st.markdown("""
### Architecture

User Query
                
↓
                
Gemini Router Agent
                
↓
                
• Product Agent

• Recommendation Agent

• Order Agent

### Tech Stack

- Python
- Streamlit
- Gemini 2.5 Flash
- Multi-Agent Architecture
- JSON Database
                
👨‍💻 Built By

ShopSphere AI is developed by:

-Sanskar Pandey & Shashmit Mishra
                
-AI & Software Development Enthusiasts               
""")

# --------------------------------------------------
# CHAT MEMORY
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# DISPLAY CHAT
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

prompt = st.chat_input(
    "Ask about products, recommendations, or orders..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("ShopSphere AI is thinking..."):

            try:
                response = orchestrator_agent(prompt)

            except Exception as e:
                response = f"Error: {str(e)}"

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown(
    """
    <div class="footer">
        Built with Gemini 2.5 Flash • Multi-Agent Architecture • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)