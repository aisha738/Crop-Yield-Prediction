import pickle
import numpy as np

# Load Model
with open("crop_yield_pred.pkl", "rb") as f:
    model = pickle.load(f)

# Mappings for categorical values
crop_mapping = {"Barley": 0, "Cotton": 1, "Rice": 3, "Soyabean": 4, "Wheat": 5}
soil_type_mapping = {"Sandy": 4, "Clay": 1, "Loam": 2, "Silt": 5, "Peaty": 3, "Chalky": 6}
weather_mapping = {"Cloudy": 0, "Rainy": 1, "Sunny": 2}
region_mapping = {"West": 3, "South": 2, "North": 1, "East": 4}

# User Input
region = input("Enter Region (West, South, North, East): ").strip()
soil_type = input("Enter Soil Type (Sandy, Clay, Loam, Silt, Peaty, Chalky): ").strip()
crop = input("Enter Crop Type (Barley, Cotton, Rice, Soyabean, Wheat): ").strip()
rainfall = float(input("Enter Rainfall (mm): "))
temperature = float(input("Enter Temperature (°C): "))
fertilizer_used = input("Was Fertilizer Used? (yes/no): ").strip().lower() == "yes"
irrigation_used = input("Was Irrigation Used? (yes/no): ").strip().lower() == "yes"
weather_condition = input("Enter Weather Condition (Cloudy, Rainy, Sunny): ").strip()
days_to_harvest = int(input("Enter Days to Harvest: "))

# Convert categorical inputs to numerical values
region = region_mapping.get(region, -1)
soil_type = soil_type_mapping.get(soil_type, -1)
crop = crop_mapping.get(crop, -1)
weather_condition = weather_mapping.get(weather_condition, -1)
fertilizer_used = int(fertilizer_used)
irrigation_used = int(irrigation_used)

# Ensure valid input
if -1 in [region, soil_type, crop, weather_condition]:
    print("🚨 Error: Invalid input detected. Please enter correct values.")
else:
    # Prepare features for prediction
    features = np.array([[region, soil_type, crop, rainfall, temperature, fertilizer_used, irrigation_used, weather_condition, days_to_harvest]])

    try:
        # Predict yield
        prediction = model.predict(features)
        print(f"\n🌾 Estimated Crop Yield: {prediction[0]:.2f} tons/ha")
    except Exception as e:
        print(f"🚨 Prediction Error: {str(e)}")
