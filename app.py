import streamlit as st
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# -----------------------------
# Gemini Model
# -----------------------------
model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------
# Load Embedding Model
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# Load FAISS Database
# -----------------------------
db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="GenAI Course Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<style>
.main-title {
    font-size: 3rem;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #4F46E5, #06B6D4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0px;
}

.sub-title {
    text-align: center;
    color: #94A3B8;
    font-size: 1.1rem;
    margin-top: -10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid="stChatMessage"] {
    border-radius: 15px;
    padding: 12px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🤖 GenAI Course Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Powered by Gemini + FAISS + RAG</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.markdown("## 🚀 About")

    st.success("🟢 System Ready")

    st.markdown("""
    ### Tech Stack

    - Gemini 2.5 Flash
    - FAISS Vector Store
    - LangChain
    - Streamlit
    - Sentence Transformers

    ### Features

    ✅ Conversational Memory  
    ✅ Source Citations  
    ✅ Semantic Search  
    ✅ RAG Pipeline
    """)

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Chat History
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User Input
# -----------------------------
question = st.chat_input("Ask about Generative AI...")

if question:

    # Show User Message
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    # -----------------------------
    # Build Conversation History
    # -----------------------------
    history = ""

    for msg in st.session_state.messages[-6:]:
        history += f"{msg['role']}: {msg['content']}\n"

    search_query = f"""
    Conversation:
    {history}

    Current Question:
    {question}
    """

    # -----------------------------
    # Retrieve Relevant Chunks
    # -----------------------------
    results = db.similarity_search_with_score(
        search_query,
        k=5
    )

    context = "\n\n".join(
        [doc.page_content for doc, score in results]
    )

    # -----------------------------
    # Prompt
    # -----------------------------
    prompt = f"""
    You are a helpful Generative AI tutor.

    Answer ONLY using the retrieved context.

    If the answer is not available in the context, reply exactly:

    "I couldn't find that information in the course knowledge base."

    Keep answers clear, detailed, and beginner-friendly.

    Context:
    {context}

    Question:
    {question}
    """

    # -----------------------------
    # Generate Response
    # -----------------------------
    with st.spinner("Thinking..."):
        response = model.generate_content(prompt)

    answer = response.text

    # -----------------------------
    # Show Assistant Response
    # -----------------------------
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

    # -----------------------------
    # Retrieved Sources
    # -----------------------------
    with st.expander("📚 Retrieved Sources"):
        for i, (doc, score) in enumerate(results, 1):
            st.markdown(f"**Source {i}**")
            st.write(doc.page_content[:300] + "...")
            st.divider()