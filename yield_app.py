import streamlit as st
import pickle
import numpy as np

# Cache model loading for efficiency
@st.cache_resource
def load_model():
    return pickle.load(open('crop_yield_pred.pkl', 'rb'))

model = load_model()

# Page Config
st.set_page_config(page_title="Crop Yield Prediction", layout="centered")

st.title("🌱 Crop Yield Prediction App")
st.write("Predict your crop yield based on key farming factors.")

# User Inputs (aligned in a single row)
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    region = st.selectbox("📍 Region", ["North", "South", "East", "West"])
with col2:
    crop = st.selectbox("🌾 Crop", ["Cotton", "Wheat", "Barley", "Soyabean", "Rice"])
with col3:
    rainfall = st.number_input("🌧️ Rainfall (mm)", value=100.0, step=0.1)
with col4:
    temperature = st.number_input("🌡️ Temperature (°C)", value=27.0, step=0.1)
with col5:
    days_to_harvest = st.number_input("📅 Days to Harvest", value=100, step=1)
with col6:
    fertilizer_used = st.radio("🧪 Fertilizer Used?", ["Yes", "No"])
with col7:
    irrigation_used = st.radio("🚰 Irrigation Used?", ["Yes", "No"])

# Convert categorical inputs
fertilizer_used = 1 if fertilizer_used == "Yes" else 0
irrigation_used = 1 if irrigation_used == "Yes" else 0

# Predict Button
if st.button("🚜 Predict Yield"):
    features = np.array([[rainfall, temperature, fertilizer_used, irrigation_used, days_to_harvest]])
    prediction = model.predict(features)
    st.success(f'🌾 Estimated Yield: {prediction[0]:.2f} tons/ha')
