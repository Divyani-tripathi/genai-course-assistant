# 🤖 GenAI Course Assistant

A Conversational Retrieval-Augmented Generation (RAG) assistant built using **Streamlit**, **Google Gemini**, **LangChain**, **FAISS**, and **Sentence Transformers**. The assistant answers questions from a Generative AI course by retrieving relevant information from a custom knowledge base before generating responses.

---

## 🚀 Features

* 💬 Conversational Chat Interface
* 🔍 Retrieval-Augmented Generation (RAG)
* 🧠 Conversational Memory
* 📚 Semantic Search using Sentence Embeddings
* ⚡ FAISS Vector Database
* 📖 Retrieved Source Display
* 🎨 Interactive Streamlit UI
* 🔐 Secure API Key Management using `.env`

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini 2.5 Flash
* LangChain
* FAISS
* HuggingFace Embeddings
* Sentence Transformers
* python-dotenv

---

## 📚 How It Works

1. Extract transcript from a Generative AI YouTube course.
2. Split the transcript into smaller chunks.
3. Convert text chunks into embeddings.
4. Store embeddings in a FAISS vector database.
5. Retrieve the most relevant chunks for a user query.
6. Send the retrieved context to Gemini.
7. Generate a context-aware answer.
8. Display the retrieved source passages.

---

## 📂 Project Structure

```text
Gen_Rag_project/
│
├── app.py
├── create_vector_db.py
├── get_transcript.py
├── rag_chat.py
├── test_retrieval.py
├── genai_course.txt
├── requirements.txt
├── README.md
│
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
│
└── ScreenShot/
```

---

## ▶️ Run Locally

### Clone the repository

```bash
git clone https://github.com/Divyani-tripathi/genai-course-assistant.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GOOGLE_API_KEY=your_api_key_here
```

### Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### Home Page

![Home](ScreenShot/homepage.png)

### Chat Interface

![Chat](ScreenShot/chat.png)

### Retrieved Sources

![Sources](ScreenShot/source.png)

---

## 🎯 Future Improvements

* 🎤 Voice Input
* 🔊 Voice Output
* 📄 PDF Question Answering
* 📚 Multi-document RAG
* 🌐 Cloud Deployment
* 💾 Chat History Persistence

---

## 👩‍💻 Author

**Divyani Rajdas Tripathi**

* GitHub: https://github.com/Divyani-tripathi
* LinkedIn: https://www.linkedin.com/in/divyani-tripathi-a52178327

---

⭐ If you found this project useful, consider giving it a star.

