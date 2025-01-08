import streamlit as st
from transformers import pipeline

# Initialize the question-answering pipeline
st.write("Loading the model...")
question_answer = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
st.write("Model loaded successfully!")

# App title and description
st.title("Question Answering with Hugging Face Transformers")
st.write(
    """
    This app allows you to input any context (up to 200 words) and ask questions based on the provided context.
    The model will generate answers using Hugging Face's `distilbert-base-cased-distilled-squad`.
    """
)

# Input section for the context
context = st.text_area(
    "Enter your context (maximum 200 words):",
    placeholder="Type or paste your context here...",
    max_chars=1200,  # 200 words (approximately 6 characters per word)
    height=200
)

# Input section for questions
questions = st.text_area(
    "Enter your questions (one question per line):",
    placeholder="Type your questions here...\nExample:\n1. Who built the Great Wall of China?\n2. What is its purpose?",
    height=150
)

# Process the input when the "Submit" button is clicked
if st.button("Submit"):
    if not context.strip():
        st.error("Please provide a context.")
    elif not questions.strip():
        st.error("Please provide at least one question.")
    else:
        st.write("Processing your questions...")
        question_list = questions.splitlines()
        
        # Ensure there are no empty questions
        question_list = [q.strip() for q in question_list if q.strip()]
        
        if len(question_list) == 0:
            st.error("No valid questions provided.")
        else:
            # Generate and display answers
            st.write("### Answers:")
            for i, question in enumerate(question_list, start=1):
                try:
                    result = question_answer(question=question, context=context)
                    st.write(f"**Question {i}:** {question}")
                    st.write(f"**Answer:** {result['answer']} (Score: {result['score']:.2f})")
                    st.write("---")
                except Exception as e:
                    st.error(f"An error occurred while answering question {i}: {e}")
