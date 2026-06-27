from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load transcript
with open("genai_course.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Transcript loaded!")

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_text(text)

print(f"Created {len(chunks)} chunks")

# Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector store
vectorstore = FAISS.from_texts(
    texts=chunks,
    embedding=embeddings
)

# Save FAISS index
vectorstore.save_local("faiss_index")

print("FAISS database saved successfully!")