import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model from a Pickle file
with open('predict.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define the feature names
FEATURES = ['Type', 'Air temperature [K]', 'Process temperature [K]', 
            'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]','operational_hours']

# Streamlit App
st.image('bg.jpeg', use_column_width=True)  # Replace 'bg.jpeg' with the path to your banner image
st.title('Machine Life Prediction')

# Create user input fields
st.sidebar.header('User Input Parameters')

def user_input_features():
    # Inputs for categorical and numerical features
    feature_values = {
        'Type': st.sidebar.selectbox('Type', options=[0, 1, 2]),  # Example categorical values
        'Air temperature [K]': st.sidebar.slider('Air temperature [K]', min_value=0, max_value=500, value=300),
        'Process temperature [K]': st.sidebar.slider('Process temperature [K]', min_value=0, max_value=500, value=300),
        'Rotational speed [rpm]': st.sidebar.slider('Rotational speed [rpm]', min_value=0, max_value=5000, value=1500),
        'Tool wear [min]': st.sidebar.slider('Tool wear [min]', min_value=0, max_value=2000, value=500),
        'operational_hours': st.sidebar.slider('operational_hours', min_value=0, max_value=2000, value=500)
    }
    
    return pd.DataFrame(feature_values, index=[0])

# Get user inputs
input_data = user_input_features()

# Display the user inputs
st.subheader("User Input Parameters")
st.write(input_data)

# Add a "Submit" button
if st.button('Submit'):
    # Make a prediction when the button is clicked
    prediction = model.predict(input_data)
    
    # Display the prediction
    st.subheader('Prediction')
    if prediction[0] == 1:
        st.write('Issue Arised: Needs to be Checked')
    else:
        st.write('NO Issue Arised: Your Machine Will Work Just Fine.')

    # Optionally: show the prediction probability
    if hasattr(model, 'predict_proba'):
        prediction_proba = model.predict_proba(input_data)
        st.subheader('Prediction Probability')
        st.write(prediction_proba)
