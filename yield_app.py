import streamlit as st
import gdown
import joblib
import numpy as np
import matplotlib.pyplot as plt

# 🔹 Google Drive model loading
file_id = "1s9tR5Rji6ecVqzU8R9X5E5UkL53JWGlS" 
url = f"https://drive.google.com/uc?id={file_id}"
output = "crop_yield_pred.pkl"

@st.cache_data
def load_model():
    """Download and load model from Google Drive."""
    gdown.download(url, output, quiet=False)
    return joblib.load(output)

model = load_model()

# 🔹 Streamlit UI Setup
st.set_page_config(page_title="Crop Yield Prediction", layout="centered")
st.markdown("<h1 style='text-align: center; color: green;'>🌱 Crop Yield Prediction App</h1>", unsafe_allow_html=True)

# 🔹 User Inputs
st.markdown("#### 📊 Enter Farming Data:")

rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0.0, max_value=5000.0, value=100.0, step=0.1, help="Amount of rainfall in millimeters.")
temperature = st.number_input("🌡️ Temperature (°C)", min_value=-10.0, max_value=50.0, value=27.0, step=0.1, help="Average temperature in Celsius.")
fertilizer_use = st.radio("🧪 Fertilizer Used?", ["Yes", "No"])
irrigation_use = st.radio("🚰 Irrigation Used?", ["Yes", "No"])
days_to_harvest = st.number_input("⏳ Days to Harvest", min_value=30, max_value=365, value=120, step=1, help="Number of days until harvest.")

# Convert categorical inputs to numerical
fertilizer_use = 1 if fertilizer_use == "Yes" else 0
irrigation_use = 1 if irrigation_use == "Yes" else 0

# 🔹 Prediction Logic
if st.button("🌾 Predict Yield"):
    features = np.array([[rainfall, temperature, fertilizer_use, irrigation_use, days_to_harvest]])
    prediction = model.predict(features)[0]

    st.success(f"📈 Estimated Crop Yield: **{prediction:.2f} tons/ha**")

    # 🔹 Visualization (User Input vs Prediction)
    st.markdown("### 📊 Visualization: Impact of Your Inputs")
    
    # Creating a bar chart
    fig, ax = plt.subplots()
    categories = ["Rainfall", "Temperature", "Fertilizer", "Irrigation", "Days to Harvest"]
    values = [rainfall, temperature, fertilizer_use * 100, irrigation_use * 100, days_to_harvest]

    ax.barh(categories, values, color=["blue", "red", "green", "brown", "orange"])
    ax.set_xlabel("Value")
    ax.set_title("Input Values Relative to Prediction")

    st.pyplot(fig)
