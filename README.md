# 🤖 GenAI Course Assistant

A Conversational Retrieval-Augmented Generation (RAG) Assistant built using Streamlit, Gemini, LangChain, FAISS, and Sentence Transformers.

## 🚀 Features

* Conversational Chat Interface
* Retrieval-Augmented Generation (RAG)
* Conversational Memory
* Semantic Search using Embeddings
* FAISS Vector Database
* Source Retrieval
* Streamlit UI

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini 2.5 Flash
* LangChain
* FAISS
* HuggingFace Embeddings
* Sentence Transformers

## 📚 How It Works

1. Extract transcript from a Generative AI YouTube course
2. Split text into chunks
3. Generate embeddings
4. Store embeddings in FAISS
5. Retrieve relevant chunks based on user queries
6. Generate contextual answers using Gemini

## ▶️ Run Locally

Install dependencies:

pip install -r requirements.txt

Create a .env file:

GOOGLE\_API\_KEY=your\_api\_key

Run the application:

streamlit run app.py

## 🎯 Future Improvements

* Voice Input
* Voice Output
* Multi-document RAG
* PDF Question Answering
* Cloud Deployment

