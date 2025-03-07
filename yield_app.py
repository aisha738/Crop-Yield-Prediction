import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Page Config (must be the first Streamlit command)
st.set_page_config(page_title="Crop Yield Prediction", layout="centered")

# Load Model
@st.cache_resource
def load_model():
    return pickle.load(open('crop_yield_pred.pkl', 'rb'))

model = load_model()

# Mappings
crop_mapping = {"Barley": 0, "Cotton": 1, "Maize": 2, "Rice": 3, "Soyabean": 4, "Wheat": 5}
boolean_mapping = {False: 0, True: 1}
soil_type_mapping = {"Sandy": 4, "Clay": 1, "Loam": 2, "Silt": 5, "Peaty": 3, "Chalky": 6}
weather_mapping = {"Cloudy": 0, "Rainy": 1, "Sunny": 2}
region_mapping = {"West": 3, "South": 2, "North": 1, "East": 4}

# App Title
st.title("🌱 Crop Yield Prediction")
st.write("This model predicts the yield for Cotton, Wheat, Barley, Soyabean, and Rice. Enter farming details below to get an estimate.")

# User Inputs
col1, col2 = st.columns(2)

with col1:
    region = st.selectbox("🌍 Region", list(region_mapping.keys()))
    soil_type = st.selectbox("🪵 Soil Type", list(soil_type_mapping.keys()))
    crop = st.selectbox("🌾 Crop Type", list(crop_mapping.keys()))
    rainfall = st.number_input('🌧️ Rainfall (mm)', value=100.00, step=0.1)
    temperature = st.number_input('🌡️ Temperature (°C)', value=27.00, step=0.1)

with col2:
    fertilizer_used = st.checkbox('🧪 Fertilizer Used')
    irrigation_used = st.checkbox('🚰 Irrigation Used')
    weather_condition = st.selectbox("⛅ Weather Condition", list(weather_mapping.keys()))
    days_to_harvest = st.number_input('📅 Days to Harvest', value=100, step=1)

# Convert categorical inputs to numerical representations
region = region_mapping[region]
soil_type = soil_type_mapping[soil_type]
crop = crop_mapping[crop]
weather_condition = weather_mapping[weather_condition]
fertilizer_used = boolean_mapping[fertilizer_used]
irrigation_used = boolean_mapping[irrigation_used]

# Predict Button
if st.button('🚜 Predict Yield'):
    # Create a numpy array with the input features
    features = np.array([[region, soil_type, crop, rainfall, temperature, fertilizer_used, irrigation_used, weather_condition, days_to_harvest]])
    
    # Make prediction
    prediction = model.predict(features)
    
    # Display the result
    st.success(f'🌾 Estimated Yield: {prediction[0]:.2f} tons/ha')
