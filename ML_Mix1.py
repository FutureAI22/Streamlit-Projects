import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris

st.title("ML Model Selector")

# Model selection
model_choice = st.sidebar.selectbox("Choose a Model", ["Classifier Model", "Linear Regression Model"])

if model_choice == "Classifier Model":
    st.header("Classifier Model: Predict Iris Species")

    @st.cache_data
    def load_classifier_data():
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns=iris.feature_names)
        df['species'] = iris.target
        return df, iris.target_names

    # Load data and train the classifier
    df, target_names = load_classifier_data()
    classifier_model = RandomForestClassifier()
    classifier_model.fit(df.iloc[:, :-1], df['species'])

    # Input features
    st.sidebar.title("Input Features for Iris Prediction")
    sepal_length = st.sidebar.slider("Sepal Length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
    sepal_width = st.sidebar.slider("Sepal Width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
    petal_length = st.sidebar.slider("Petal Length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
    petal_width = st.sidebar.slider("Petal Width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

    # Make a prediction
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = classifier_model.predict(input_data)
    predicted_species = target_names[prediction[0]]

    # Display the prediction
    st.write("Prediction")
    st.write(f"The predicted species is: {predicted_species}")

elif model_choice == "Linear Regression Model":
    st.header("Linear Regression Model: Predict Housing Prices in USD")

    @st.cache_data
    def load_regression_data():
        file_name = './Housing.xlsx'  # Ensure this file is in the same directory
        housing_data = pd.ExcelFile(file_name)
        df = housing_data.parse('Housing')
        X = df.drop(columns=['price'])  # Changed 'Price' to 'price'
        y = df['price']  # Changed 'Price' to 'price'
        return df, X, y

    # Load data and train the regression model
    df, X, y = load_regression_data()
    regression_model = LinearRegression()
    regression_model.fit(X, y)

    # Sidebar inputs for regression
    st.sidebar.title("Input Features for Housing Price Prediction")
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
    prediction = regression_model.predict(input_data)

    # Display the prediction
    st.write("Prediction")
    st.write(f"The predicted price of the house is: ${prediction[0]:,.2f} USD")
