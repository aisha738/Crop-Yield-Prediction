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
    <h1 style='text-align: center; color: #4CAF50; font-size: 6
