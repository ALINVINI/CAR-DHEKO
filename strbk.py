import streamlit as st
import numpy as np
import pickle
from PIL import Image

# Load the model
with open(r'C:\streamlit_app\linear_regression_model.pkl', 'rb') as model_file:
    linear_model = pickle.load(model_file)

# Load the encoder
with open(r'C:\streamlit_app\encoder.pkl', 'rb') as encoder_file:
    encoder = pickle.load(encoder_file)

# Set custom styles for background colors and formatting
st.markdown(
    """
    <style>
    .header {
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border-radius: 5px;
    }
    .result-box {
        background-color: #e1f5fe;
        color: #000;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='header'><h1>Car Price Prediction</h1></div>", unsafe_allow_html=True)

# Display sample car image
car_image = Image.open(r'C:\streamlit_app\car-5548242_640.jpg')  # Replace with your car image path
st.image(car_image, caption='Sample Car', use_column_width=True)

# Input fields for user data
ft = st.selectbox("Fuel Type", ['Cng', 'Diesel', 'Electric', 'Lpg', 'Petrol'])
bt = st.selectbox("Body Type", ['Convertibles', 'Coupe', 'Hatchback', 'Hybrids', 'MUV', 
                                  'Minivans', 'Pickup Trucks', 'SUV', 'Sedan', 'Wagon'])
km = st.number_input("Kilometers Driven", min_value=0)
transmission = st.selectbox("Transmission", ['Automatic', 'Manual'])
ownerNo = st.number_input("Number of Owners", min_value=0)
model = st.selectbox("Car Model", encoder.categories_[4].tolist())  # Assuming the car model is the 5th category
modelYear = st.number_input("Model Year", min_value=1900, max_value=2024)
Mileage = st.number_input("Mileage", min_value=0)
Engine = st.number_input("Engine", min_value=0)
Seats = st.number_input("Seats", min_value=1, max_value=10)
city = st.selectbox("City", ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Jaipur', 'Kolkata'])

if st.button("Predict Price"):
    # Prepare input data for prediction
    input_data = np.array([[ft, bt, float(km), transmission, int(ownerNo), model, int(modelYear), 
                            float(Mileage), float(Engine), int(Seats), city]], dtype=object)

    try:
        # Separate categorical and numerical features
        categorical_features = input_data[:, [0, 1, 3,4, 5,9, 10]]
        numerical_features = input_data[:, [2, 6, 7, 8]]
        
        # Encode categorical features
        input_encoded = encoder.transform(categorical_features)
        
        # Stack numerical and encoded categorical data
        input_final = np.hstack([numerical_features, input_encoded])

        # Predict the price
        predicted_price = linear_model.predict(input_final)
        
        # Round the price
        rounded_price = round(predicted_price[0])

        # Display the result with background color and rounded price
        st.markdown(
            f"<div class='result-box'><h2>The predicted price of the car is: ₹{rounded_price:,}</h2></div>",
            unsafe_allow_html=True
        )
    
    except ValueError as e:
        st.error(f"Error: {e}")
        st.warning("Please ensure all input values are valid and within expected categories.")
