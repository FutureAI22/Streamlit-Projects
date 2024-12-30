import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import os

st.title("Linear Regression Model: Predict Housing Prices in USD")

@st.cache_data
def load_and_prepare_data():
    # Ensure the dataset file exists
    file_name = 'Housing.xlsx'
    if not os.path.exists(file_name):
        st.error(f"The file {file_name} was not found in the current directory.")
        st.stop()
    
    housing_data = pd.ExcelFile(file_name)
    df = housing_data.parse('Housing')
    
    # Separate features and target
    X = df.drop(columns=['price'])
    y = df['price']  # Ensure 'price' matches the column name in the dataset
    
    return df, X, y

# Debugging
st.write("Current Working Directory:", os.getcwd())
st.write("Files in the Current Directory:", os.listdir())

# Load and prepare data
df, X, y = load_and_prepare_data()

# Train the model
model = LinearRegression()
model.fit(X, y)

# Sidebar for inputs
st.sidebar.title("Input Features for Housing Price Prediction")
inputs = {}

inputs['area'] = st.sidebar.slider("Area (in sq. ft.)", int(df['area'].min()), int(df['area'].max()), int(df['area'].mean()))
inputs['bedrooms'] = st.sidebar.slider("Bedrooms", int(df['bedrooms'].min()), int(df['bedrooms'].max()), int(df['bedrooms'].mean()))
inputs['bathrooms'] = st.sidebar.slider("Bathrooms", int(df['bathrooms'].min()), int(df['bathrooms'].max()), int(df['bathrooms'].mean()))
inputs['stories'] = st.sidebar.slider("Stories", int(df['stories'].min()), int(df['stories'].max()), int(df['stories'].mean()))

binary_features = {
    'mainroad-1': "Main Road (Yes = 1, No = 0)",
    'guestroom-1': "Guest Room (Yes = 1, No = 0)",
    'basement-1': "Basement (Yes = 1, No = 0)",
    'hotwaterheating-1': "Hot Water Heating (Yes = 1, No = 0)",
    'airconditioning-1': "Air Conditioning (Yes = 1, No = 0)"
}
for feature, description in binary_features.items():
    inputs[feature] = st.sidebar.radio(description, (1, 0))

inputs['furnishingstatus-1'] = st.sidebar.selectbox(
    "Furnishing Status (1 = Furnished, 2 = Semi-Furnished, 3 = Unfurnished)",
    [1, 2, 3]
)

# Convert inputs to DataFrame
input_data = pd.DataFrame([inputs])

# Make a prediction
prediction = model.predict(input_data)

# Display the prediction
st.write("Prediction")
st.write(f"The predicted price of the house is: ${prediction[0]:,.2f} USD")
