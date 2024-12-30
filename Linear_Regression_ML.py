import streamlit as st
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression

st.title("California Housing Price Prediction")

@st.cache_data
def load_data():
    # Load the California Housing dataset
    housing = fetch_california_housing(as_frame=True)
    df = housing.data
    df['MedHouseVal'] = housing.target  # Adding the target column
    feature_names = housing.feature_names
    return df, feature_names

# Load the data and feature names
df, feature_names = load_data()

# Prepare the model
model = LinearRegression()
model.fit(df[feature_names], df['MedHouseVal'])

# Sidebar for input features
st.sidebar.title("Input Features")
inputs = {}
for feature in feature_names:
    min_value = float(df[feature].min())
    max_value = float(df[feature].max())
    mean_value = float(df[feature].mean())
    inputs[feature] = st.sidebar.slider(feature, min_value, max_value, mean_value)

# Convert inputs to DataFrame
input_data = pd.DataFrame([inputs])

# Make a prediction
prediction = model.predict(input_data)

# Display the prediction
st.write("Prediction")
st.write(f"The predicted Median House Value is: ${prediction[0]*100000:.2f}")
