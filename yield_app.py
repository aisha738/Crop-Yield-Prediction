import streamlit as st
import pickle
import numpy as np

# Page Config (must be the first Streamlit command)
st.set_page_config(page_title="Crop Yield Prediction", layout="centered")

# Load Model
@st.cache_resource
def load_model():
    return pickle.load(open('crop_yield_pred.pkl', 'rb'))

model = load_model()

# App Title
st.title("🌱 Crop Yield Prediction")
st.write("This model predicts the yield for Cotton, Wheat, Barley, Soyabean, and Rice. Enter farming details below to get an estimate.")

# User Inputs
col1, col2 = st.columns(2)

with col1:
    region = st.selectbox("🌍 Region", ["North", "South", "East", "West"])
    soil_type = st.selectbox("🪵 Soil Type", ["Sandy", "Loam", "Chalky", "Silt", "Peaty"])
    crop = st.selectbox("🌾 Crop Type", ["Cotton", "Wheat", "Barley", "Soyabean", "Rice"])
    rainfall = st.number_input('🌧️ Rainfall (mm)', value=100.00, step=0.1)
    temperature = st.number_input('🌡️ Temperature (°C)', value=27.00, step=0.1)

with col2:
    fertilizer_used = st.checkbox('🧪 Fertilizer Used')
    irrigation_used = st.checkbox('🚰 Irrigation Used')
    weather_condition = st.selectbox("⛅ Weather Condition", ["Sunny", "Rainy", "Cloudy"])
    days_to_harvest = st.number_input('📅 Days to Harvest', value=100, step=1)

# Convert categorical inputs to numerical representations (if needed)
fertilizer_used = 1 if fertilizer_used else 0
irrigation_used = 1 if irrigation_used else 0

# Predict Button
if st.button('🚜 Predict Yield'):
    features = np.array([[region, soil_type, crop, rainfall, temperature, fertilizer_used, irrigation_used, weather_condition, days_to_harvest]])
    prediction = model.predict(features)
    st.success(f'🌾 Estimated Yield: {prediction[0]:.2f} tons/ha')

