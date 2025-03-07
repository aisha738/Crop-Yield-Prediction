import streamlit as st
import pickle
import numpy as np

# Load Model
@st.cache_resource
def load_model():
    return pickle.load(open('crop_yield_pred.pkl', 'rb'))

model = load_model()

# Page Config
st.set_page_config(page_title="Crop Yield Prediction", layout="centered")

# App Title
st.title("🌱 Crop Yield Prediction")
st.write("Enter farming details to predict crop yield.")

# User Inputs
col1, col2 = st.columns(2)

with col1:
    rainfall = st.number_input('🌧️ Rainfall (mm)', value=100.00, step=0.1)
    temperature = st.number_input('🌡️ Temperature (°C)', value=27.00, step=0.1)
    days_to_harvest = st.number_input('📅 Days to Harvest', value=100, step=1)
    region = st.selectbox("🌍 Region", ["North", "South", "East", "West"])

with col2:
    crop = st.selectbox("🌾 Crop Type", ["Cotton", "Wheat", "Barley", "Soyabean", "Rice"])
    fertilizer_used = st.checkbox('🧪 Fertilizer Used')
    irrigation_used = st.checkbox('🚰 Irrigation Used')

# Convert categorical inputs
fertilizer_used = 1 if fertilizer_used else 0
irrigation_used = 1 if irrigation_used else 0

# Predict Button
if st.button('🚜 Predict Yield'):
    features = np.array([[rainfall, temperature, fertilizer_used, irrigation_used, days_to_harvest]])
    prediction = model.predict(features)
    st.success(f'🌾 Estimated Yield: {prediction[0]:.2f} tons/ha')
