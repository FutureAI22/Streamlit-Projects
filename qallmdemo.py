import streamlit as st
from transformers import pipeline

# Specify the model explicitly
question_answer = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Example usage
result = question_answer(
    question="Who built the Great Wall of China?",
    context="The Great Wall of China was built by several dynasties, including the Qin and Ming dynasties."
)

# Display the result in Streamlit
st.write("Question Answering Result:")
st.json(result)
