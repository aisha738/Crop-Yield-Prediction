import streamlit as st
import numpy as np
import joblib

# Load Model Using joblib
with open("crop_yield.joblib", "rb") as file:
    model = joblib.load(file)

# Encoding Mapping
region_mapping = {"North": 0, "South": 1, "East": 2, "West": 3}
soil_type_mapping = {"Sandy": 0, "Loam": 1, "Chalky": 2, "Silt": 3, "Peaty": 4}
crop_mapping = {"Cotton": 0, "Wheat": 1, "Barley": 2, "Soyabean": 3, "Rice": 4}
weather_mapping = {"Sunny": 0, "Rainy": 1, "Cloudy": 2}

# Page Config
st.set_page_config(page_title="Crop Yield Prediction", layout="centered")

# App Title & Subtitle
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50; font-size: 60px;'>🌱 Crop Yield Prediction</h1>
    <h4 style='text-align: center; color: #666;'>This app helps you predict the yield for Cotton, Wheat, Barley, Soyabean, and Rice.</h4>
""", unsafe_allow_html=True)

# Subheader
st.subheader("Enter Parameters Below")

# User Input Form
region = st.selectbox("📍 Region", list(region_mapping.keys()))
soil_type = st.selectbox("🌱 Soil Type", list(soil_type_mapping.keys()))
crop = st.selectbox("🌾 Crop Type", list(crop_mapping.keys()))
rainfall = st.number_input('🌧️ Rainfall (mm)', value=100.0, step=0.1)
temperature = st.number_input('🌡️ Temperature (°C)', value=27.0, step=0.1)
fertilizer_used = st.selectbox('🧪 Fertilizer Used?', ["Yes", "No"])
irrigation_used = st.selectbox('🚰 Irrigation Used?', ["Yes", "No"])
weather_condition = st.selectbox("⛅ Weather Condition", list(weather_mapping.keys()))
days_to_harvest = st.number_input('📅 Days to Harvest', value=100, step=1)

# Convert categorical inputs to numeric
features = np.array([[  
    region_mapping[region], soil_type_mapping[soil_type], crop_mapping[crop],
    rainfall, temperature, 1 if fertilizer_used == "Yes" else 0,
    1 if irrigation_used == "Yes" else 0, weather_mapping[weather_condition],
    days_to_harvest
]])

# Styled Predict Button (Green, Centered, and Functional)
st.markdown(
    """
    <style>
        div.stButton > button {
            display: block;
            margin: auto;
            background-color: #4CAF50 !important;
            color: white !important;
            font-size: 18px !important;
            padding: 10px 25px !important;
            border-radius: 8px !important;
            border: none !important;
            cursor: pointer !important;
        }
        div.stButton > button:hover {
            background-color: #45a049 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Centering the button properly
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_button = st.button("🚜 Predict Yield")

# Prediction Function
if predict_button:
    try:
        prediction = model.predict(features)
        st.success(f'🌾 Estimated Yield: {prediction[0]:.2f} tons/ha')
    except Exception as e:
        st.error(f"Error: {e}")
