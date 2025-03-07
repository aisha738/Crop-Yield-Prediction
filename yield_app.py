import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt

# Load Model
model = pickle.load(open('crop_yield_pred.pkl', 'rb'))

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

col1, col2 = st.columns(2)

with col1:
    rainfall = st.number_input('🌧️ Rainfall (mm)', value=100.00, step=0.1, help="Amount of rainfall in millimeters")
    temperature = st.number_input('🌡️ Temperature (°C)', value=27.00, step=0.1, help="Average temperature in degrees Celsius")
    days_to_harvest = st.number_input('📅 Days to Harvest', value=100, step=1, help="Number of days before harvest")

with col2:
    fertilizer_used = st.radio('🧪 Fertilizer Used?', ('Yes', 'No'), help="Select whether fertilizer was applied")
    irrigation_used = st.radio('🚰 Irrigation Used?', ('Yes', 'No'), help="Select whether irrigation was applied")

# Convert categorical inputs
fertilizer_used = 1 if fertilizer_used == "Yes" else 0
irrigation_used = 1 if irrigation_used == "Yes" else 0

# 🚜 Predict Button
if st.button('🚜 Predict Yield'):
    features = np.array([[rainfall, temperature, fertilizer_used, irrigation_used, days_to_harvest]])
    prediction = model.predict(features)
    st.success(f'🌾 Estimated Yield: {prediction[0]:.2f} tons/ha')

    # Example average yield (Adjust based on real dataset)
    average_yield = 4.65  

    # 📊 Visualization 1: Predicted vs. Average Yield
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(["Predicted Yield", "Average Yield"], [prediction[0], average_yield], color=["#4CAF50", "#FFC107"])
    ax.set_ylabel("Yield (tons/ha)")
    ax.set_title("Predicted vs. Average Yield")

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.2f}", ha="center", va="bottom")

    st.pyplot(fig)

    # 📊 Visualization 2: User Input Breakdown
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    user_inputs = [rainfall, temperature, days_to_harvest, fertilizer_used, irrigation_used]
    input_labels = ["Rainfall (mm)", "Temperature (°C)", "Days to Harvest", "Fertilizer Used", "Irrigation Used"]
    
    bars2 = ax2.barh(input_labels, user_inputs, color=["#4CAF50", "#8B4513", "#2196F3", "#FFC107", "#FF5722"])
    ax2.set_xlabel("User Input Value")
    ax2.set_title("Your Inputs Breakdown")

    for bar in bars2:
        ax2.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f"{bar.get_width():.2f}", va="center")

    st.pyplot(fig2)

# 🔗 Footer
st.markdown('<p class="footer">Developed with ❤️ for smart agriculture</p>', unsafe_allow_html=True)
