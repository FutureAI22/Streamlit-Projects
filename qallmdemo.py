from transformers import pipeline

# Initialize the question-answering pipeline
question_answerer = pipeline("question-answering")

# Context (the paragraph)
context = """The Great Wall of China is one of the most remarkable architectural feats in human history. Constructed over several dynasties, including the Qin, Han, and Ming, it spans more than 13,000 miles. Originally built to defend against invasions from northern tribes, the wall also served as a symbol of China’s strength and unity. Emperor Qin Shi Huang, known for unifying China, played a pivotal role in initiating the construction of the wall in 221 BCE. Despite its defensive purpose, the wall also facilitated trade and cultural exchange along the Silk Road, connecting China to other civilizations."""

# Questions
questions = [
    "Who initiated the construction of the Great Wall of China?",
    "What was the primary purpose of the Great Wall of China?",
    "Which dynasties contributed to the construction of the Great Wall of China?"
]

# Answer each question
for question in questions:
    answer = question_answerer(question=question, context=context)
    print(f"Question: {question}")
    print(f"Answer: {answer['answer']}\n")
