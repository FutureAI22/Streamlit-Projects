import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

st.title("Housing Price Prediction App")

@st.cache_data
def load_and_prepare_data():
    # Load the dataset
    file_path = '/mnt/data/Housing.xlsx'
    housing_data = pd.ExcelFile(file_path)
    df = housing_data.parse('Housing')
    
    # Encode categorical columns
    categorical_cols = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 
                        'airconditioning', 'prefarea', 'furnishingstatus']
    encoders = {col: LabelEncoder() for col in categorical_cols}
    for col in categorical_cols:
        df[col] = encoders[col].fit_transform(df[col])
    
    # Separate features and target
    X = df.drop(columns=['price'])
    y = df['price']
    
    return df, X, y

# Load and prepare data
df, X, y = load_and_prepare_data()

# Train the model
model = LinearRegression()
model.fit(X, y)

# Sidebar for input features
st.sidebar.title("Input Features")
inputs = {}
for col in X.columns:
    if df[col].dtype == 'float64' or df[col].dtype == 'int64':
        min_val = float(df[col].min())
        max_val = float(df[col].max())
        mean_val = float(df[col].mean())
        inputs[col] = st.sidebar.slider(col, min_val, max_val, mean_val)
    else:
        options = df[col].unique()
        inputs[col] = st.sidebar.selectbox(col, options)

# Convert inputs to DataFrame
input_data = pd.DataFrame([inputs])

# Make a prediction
prediction = model.predict(input_data)

# Display the prediction
st.write("Prediction")
st.write(f"The predicted price of the house is: ₹{prediction[0]:,.2f}")
