import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# --- NEW IMPORTS FOR EMBEDDINGS AND TOGETHER AI LLM ---
from langchain_community.embeddings import HuggingFaceEmbeddings # For open-source embeddings
# CORRECTED IMPORT: TogetherLLM is now imported from langchain_together.llms
from langchain_together.llms import Together # For Together AI models

from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain

# --- API KEY & ENV HANDLING ---
# Import for loading .env file (recommended for API keys)
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# --- Configuration for Together AI ---
# Get Together AI API key from environment variable
# IMPORTANT: Store your token in a file named .env in the same directory as this script.
# The .env file should contain: TOGETHER_API_KEY="sk-tg-YOUR_ACTUAL_TOGETHER_AI_TOKEN_HERE"
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# Define the Together AI model you want to use for the LLM
# You can find models at https://www.together.ai/models
# Recommended instruction-tuned models for Q&A:
# "mistralai/Mixtral-8x7B-Instruct-v0.1" (Very powerful, might be slower)
# "google/gemma-7b-it" (Good balance, faster)
# "meta-llama/Llama-2-7b-chat-hf" (Requires Meta's Llama access via Hugging Face)
TOGETHER_MODEL_ID = "mistralai/Mixtral-8x7B-Instruct-v0.1" # You can change this model ID


# --- Error Handling for Missing API Key ---
if not TOGETHER_API_KEY:
    st.error("Error: Together AI API key not found.")
    st.info("Please create a .env file in your project directory with TOGETHER_API_KEY=\"sk-tg-YOUR_ACTUAL_TOGETHER_AI_TOKEN_HERE\".")
    st.info("You can generate your Together AI API key at https://api.together.xyz/settings/api-keys")
    st.stop() # Stop the Streamlit app if the token is missing


st.header("My first Chatbot")


with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")


# Extract the text and process if a file is uploaded
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # --- Generating Embeddings ---
    # Using a general-purpose sentence transformer for embeddings
    # This model will be downloaded locally by sentence-transformers library on first run.
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Creating vector store - FAISS
    vector_store = FAISS.from_texts(chunks, embeddings)

    # Get user question
    user_question = st.text_input("Type Your question here")

    # Do similarity search and get response if user asks a question
    if user_question:
        match = vector_store.similarity_search(user_question)

        # --- Define the LLM (Using TogetherLLM) ---
        llm = Together(
            model=TOGETHER_MODEL_ID, # The model ID from Together AI
            together_api_key=TOGETHER_API_KEY, # Pass the Together AI API key
            temperature=0.1, # Controls randomness: 0.0 for deterministic, higher for more creative
            max_tokens=1000 # Max number of tokens to generate in the response
        )

        # Output results
        # chain -> take the question, get relevant document, pass it to the LLM, generate the output
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents = match, question = user_question)
        st.write(response)
