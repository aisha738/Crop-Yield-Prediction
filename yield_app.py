import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt

# Cache Model Loading
@st.cache_resource
def load_model():
    return pickle.load(open('crop_yield_pred.pkl', 'rb'))

model = load_model()

# Page Config
st.set_page_config(
    page_title="Crop Yield Prediction",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom Styling
st.markdown(
    """
    <style>
        .stApp { background-color: #ffffff; }
        .main-title { color: #4CAF50; text-align: center; font-size: 32px; font-weight: bold; }
        .description { text-align: center; font-size: 18px; color: #666; }
        .footer { text-align: center; font-size: 14px; color: #999; }
    </style>
    """,
    unsafe_allow_html=True
)

# 🌱 App Title
st.markdown('<p class="main-title">🌱 Crop Yield Prediction App</p>', unsafe_allow_html=True)
st.markdown('<p class="description">Predict your crop yield based on key farming factors</p>', unsafe_allow_html=True)

# 📊 User Inputs
st.subheader("Input Parameters Below:")

col1, col2, col3, col4 = st.columns(4)

with col1:
    region = st.selectbox('🌍 Region', ['North', 'South', 'East', 'West'])
    rainfall = st.number_input('🌧️ Rainfall (mm)', value=100.00, step=0.1, help="Amount of rainfall in millimeters")

with col2:
    crop = st.selectbox('🌾 Crop Type', ['Cotton', 'Wheat', 'Barley', 'Soyabean', 'Rice'])
    temperature = st.number_input('🌡️ Temperature (°C)', value=27.00, step=0.1, help="Average temperature in degrees Celsius")

with col3:
    days_to_harvest = st.number_input('📅 Days to Harvest', value=100, step=1, help="Number of days before harvest")
    fertilizer_used = st.radio('🧪 Fertilizer Used?', ('Yes', 'No'), help="Select whether fertilizer was applied")

with col4:
    irrigation_used = st.radio('🚰 Irrigation Used?', ('Yes', 'No'), help="Select whether irrigation was applied")

# Convert categorical inputs
fertilizer_used = 1 if fertilizer_used == "Yes" else 0
irrigation_used = 1 if irrigation_used == "Yes" else 0

# 🏃 Predict Button
if st.button('🏃 Predict Yield'):
    features = np.array([[rainfall, temperature, fertilizer_used, irrigation_used, days_to_harvest]])
    prediction = model.predict(features)
    st.success(f'🌾 Estimated Yield: {prediction[0]:.2f} tons/ha')

    # Example average yield (Adjust based on real dataset)
    average_yield = 4.65  

    # 📊 Visualization: Predicted vs. Average Yield (Faster Rendering)
    st.bar_chart({"Yield Type": ["Predicted Yield", "Average Yield"], "Yield (tons/ha)": [prediction[0], average_yield]})

# 🔗 Footer
st.markdown('<p class="footer">Developed with ❤️ for smart agriculture</p>', unsafe_allow_html=True)

