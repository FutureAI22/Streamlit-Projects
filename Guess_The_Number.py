import streamlit as st
import random

# Streamlit app title
st.title("🎲 Number Guessing Game")

# Session state to store the random number
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)

# Session state to track game status
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.write("Guess a number between **1 and 100**.")

# User input
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Check button
if st.button("Check Guess"):
    if user_guess:
        if user_guess < st.session_state.random_number:
            st.warning("🔼 Try a little **higher**!")
        elif user_guess > st.session_state.random_number:
            st.warning("🔽 Try a little **lower**!")
        else:
            st.success(f"🎉 Congratulations! You guessed it right: **{st.session_state.random_number}**")
            st.session_state.game_over = True

# Reset button
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.random_number = random.randint(1, 100)
        st.session_state.game_over = False
        st.experimental_rerun()
