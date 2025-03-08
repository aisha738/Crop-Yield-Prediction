import streamlit as st
import pickle
import numpy as np

# Load Model
model = pickle.load(open('crop_yield_pred.pkl', 'rb'))

# Encoding Mapping
region_mapping = {"North": 0, "South": 1, "East": 2, "West": 3}
soil_type_mapping = {"Sandy": 0, "Loam": 1, "Chalky": 2, "Silt": 3, "Peaty": 4}
crop_mapping = {"Cotton": 0, "Wheat": 1, "Barley": 2, "Soyabean": 3, "Rice": 4}
weather_mapping = {"Sunny": 0, "Rainy": 1, "Cloudy": 2}

# Page Config
st.set_page_config(page_title="Crop Yield Prediction", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
        .main-title { 
            color: #4CAF50; 
            text-align: center; 
            font-size: 48px; 
            font-weight: bold; 
        }
        .description {
            text-align: center;
            font-size: 20px;
            color: #666;
        }
        .stButton>button {
            display: block;
            margin: 0 auto;
            width: 220px;
            font-size: 18px;
            font-weight: bold;
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #999;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 🌱 App Title
st.markdown('<p class="main-title">🌱 Crop Yield Prediction App</p>', unsafe_allow_html=True)
st.markdown('<p class="description">Predict your crop yield based on key farming factors</p>', unsafe_allow_html=True)

# 📊 User Inputs
st.subheader("Input Parameters Below:")

col1, col2 = st.columns(2)

with col1:
    region = st.selectbox("📍 Region", options=list(region_mapping.keys()), help="Select the region of cultivation")
    soil_type = st.selectbox("🌱 Soil Type", options=list(soil_type_mapping.keys()), help="Select the soil type")
    crop = st.selectbox("🌾 Crop Type", options=list(crop_mapping.keys()), help="Select the crop being cultivated")
    rainfall = st.number_input('🌧️ Rainfall (mm)', value=100.00, step=0.1, help="Amount of rainfall in millimeters")
    temperature = st.number_input('🌡️ Temperature (°C)', value=27.00, step=0.1, help="Average temperature in degrees Celsius")

with col2:
    fertilizer_used = st.selectbox('🧪 Fertilizer Used?', ["Yes", "No"], help="Select whether fertilizer was applied")
    irrigation_used = st.selectbox('🚰 Irrigation Used?', ["Yes", "No"], help="Select whether irrigation was applied")
    weather_condition = st.selectbox("⛅ Weather Condition", options=list(weather_mapping.keys()), help="Select the general weather condition")
    days_to_harvest = st.number_input('📅 Days to Harvest', value=100, step=1, help="Number of days before harvest")

# Convert categorical inputs to numeric
region_encoded = region_mapping[region]
soil_type_encoded = soil_type_mapping[soil_type]
crop_encoded = crop_mapping[crop]
weather_encoded = weather_mapping[weather_condition]
fertilizer_encoded = 1 if fertilizer_used == "Yes" else 0
irrigation_encoded = 1 if irrigation_used == "Yes" else 0

# Convert inputs to a NumPy array
features = np.array([[region_encoded, soil_type_encoded, crop_encoded, rainfall, temperature, fertilizer_encoded, irrigation_encoded, weather_encoded, days_to_harvest]])

# 🚜 Centered Predict Button
if st.button('🚜 Predict Yield'):
    try:
        prediction = model.predict(features)
        st.success(f'🌾 Estimated Yield: {prediction[0]:.2f} tons/ha')
    except Exception as e:
        st.error(f"An error occurred: {e}")

# 🔗 Footer
st.markdown('<p class="footer">Developed with ❤️ for smart agriculture</p>', unsafe_allow_html=True)
