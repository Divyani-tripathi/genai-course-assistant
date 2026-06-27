import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Configure Gemini
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

# Load embeddings model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS database
db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)
chat_history = []

while True:
    question = input("\nAsk a question (or type exit): ")

    if question.lower() == "exit":
        break

    # Include recent conversation
    history_text = "\n".join(chat_history[-4:])

    search_query = f"""
    Previous Conversation:
    {history_text}

    Current Question:
    {question}
    """

    docs = db.similarity_search(search_query, k=5)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are a helpful AI tutor.

    Previous Conversation:
    {history_text}

    Context:
    {context}

    Current Question:
    {question}

    Answer based only on the context and conversation.
    """

    response = model.generate_content(prompt)

    print("\nAnswer:\n")
    print(response.text)

    chat_history.append(f"User: {question}")
    chat_history.append(f"Assistant: {response.text}")