# 📖 AI-Powered Creative Story Generator

An AI-powered web application that allows users to generate unique stories based on a selected genre, theme, and length, in **English or Hindi**, and listen to them as audio.

---

## 🚀 Features

- 🎭 Select story genre (Fantasy, Sci-Fi, Mystery, etc.)
- 🎨 Input a theme to personalize your story
- 📏 Choose story length: Short, Medium, or Long
- 🌐 Generate stories in **English or Hindi**
- 🔊 Listen to the story with auto-generated audio (TTS)
- ⚡ Powered by FastAPI (backend) and Streamlit (frontend)

---

## 🛠 Tech Stack

| Frontend   | Backend | AI & Utilities               |
| ---------- | ------- | ---------------------------- |
| Streamlit  | FastAPI | OpenAI / GenAI Model         |
| HTML / CSS | Uvicorn | gTTS (Google Text-to-Speech) |
| REST API   | Python  |                              |

---

## 📂 Project Structure

story-generator/

│

├── app.py                   # Streamlit frontend

├── main.py                  # FastAPI backend entrypoint

├── routes/

│   └── routes.py            # API logic (story generation, TTS)

├── static/                  # Folder for generated audio files

│   └── *.mp3

├── requirements.txt         # All dependencies

└── README.md                # Project documentation


## ⚙️ Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

git clone https://github.com/your-username/story-generator.git
cd story-generator

### 2. Create and Activate a Virtual Environment

python3 -m venv venv
source venv/bin/activate



### 3. **Run the Streamlit Frontend**

streamlit run app.py

It will open the app in your browser at: `http://localhost:8501`


## 📌 Example Usage

1. Choose a genre (e.g.,  **Fantasy** )
2. Enter a theme (e.g.,  *Lost Kingdom* )
3. Select a length ( **Short** ,  **Medium** , or  **Long** )
4. Choose a language (**English** or  **Hindi** )
5. Click "Generate Story"

You’ll get:

* An AI-generated story
* A playable audio version of the story
