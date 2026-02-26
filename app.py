import streamlit as st
import os

st.set_page_config(page_title="Real-Time Document Q&A", layout="centered")

st.title("📄 Real-Time Document Q&A Application")
st.write("Ask questions from documents inside the documents folder.")

DOCS_FOLDER = "documents"

# Read all text files
def load_documents():
    text = ""
    if not os.path.exists(DOCS_FOLDER):
        return "No documents folder found."
    for file in os.listdir(DOCS_FOLDER):
        if file.endswith(".txt"):
            with open(os.path.join(DOCS_FOLDER, file), "r", encoding="utf-8") as f:
                text += f.read() + "\n"
    return text

docs_text = load_documents()

question = st.text_input(" Enter your question:")

if question:
    if question.lower() in docs_text.lower():
        st.success(" Answer found in documents")
        st.write(docs_text)
    else:
        st.warning(" Answer not found in documents")