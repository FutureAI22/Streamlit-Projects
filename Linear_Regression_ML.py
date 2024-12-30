import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Housing Price Prediction App (in USD)")

@st.cache_data
def load_and_prepare_data():
    # Use the file name directly since it's in the same folder as the Python file
    file_name = 'Housing.xlsx'
    housing_data = pd.ExcelFile(file_name)
    df = housing_data.parse('Housing')
    
    # Separate features and target
    X = df.drop(columns=['price'])
    y = df['price']  # Price is already in USD
    
    return df, X, y

# Load and prepare data
df, X, y = load_and_prepare_data()

# Train the model
model = LinearRegression()
model.fit(X, y)

# Sidebar for input features with explanations
st.sidebar.title("Input Features")
st.sidebar.write("""
Adjust the following features to predict the house price in USD:
- **Area**: Total area of the house in square feet.
- **Bedrooms**: Number of bedrooms in the house.
- **Bathrooms**: Number of bathrooms in the house.
- **Stories**: Number of stories in the house.
- **Main Road**: Whether the house is located on a main road (Yes = 1, No = 0).
- **Guest Room**: Whether the house includes a guest room (Yes = 1, No = 0).
- **Basement**: Whether the house has a basement (Yes = 1, No = 0).
- **Hot Water Heating**: Whether the house has hot water heating (Yes = 1, No = 0).
- **Air Conditioning**: Whether the house has air conditioning (Yes = 1, No = 0).
- **Furnishing Status**: Furnishing status of the house (1 = Furnished, 2 = Semi-Furnished, 3 = Unfurnished).
""")

inputs = {}

# Integer sliders for area, bedrooms, bathrooms, and stories
inputs['area'] = st.sidebar.slider("Area (in sq. ft.)", int(df['area'].min()), int(df['area'].max()), int(df['area'].mean()))
inputs['bedrooms'] = st.sidebar.slider("Bedrooms", int(df['bedrooms'].min()), int(df['bedrooms'].max()), int(df['bedrooms'].mean()))
inputs['bathrooms'] = st.sidebar.slider("Bathrooms", int(df['bathrooms'].min()), int(df['bathrooms'].max()), int(df['bathrooms'].mean()))
inputs['stories'] = st.sidebar.slider("Stories", int(df['stories'].min()), int(df['stories'].max()), int(df['stories'].mean()))

# Binary inputs for mainroad, guestroom, basement, hotwaterheating, airconditioning
binary_features = {
    'mainroad-1': "Main Road (Yes = 1, No = 0)",
    'guestroom-1': "Guest Room (Yes = 1, No = 0)",
    'basement-1': "Basement (Yes = 1, No = 0)",
    'hotwaterheating-1': "Hot Water Heating (Yes = 1, No = 0)",
    'airconditioning-1': "Air Conditioning (Yes = 1, No = 0)"
}
for feature, description in binary_features.items():
    inputs[feature] = st.sidebar.radio(description, (1, 0))

# Dropdown for furnishingstatus
inputs['furnishingstatus-1'] = st.sidebar.selectbox(
    "Furnishing Status (1 = Furnished, 2 = Semi-Furnished, 3 = Unfurnished)",
    [1, 2, 3]
)

# Convert inputs to DataFrame
input_data = pd.DataFrame([inputs])

# Make a prediction
prediction = model.predict(input_data)

# Display the prediction in USD
st.write("Prediction")
st.write(f"The predicted price of the house is: ${prediction[0]:,.2f} USD")
