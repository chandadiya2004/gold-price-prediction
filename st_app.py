import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('gold_price_prediction_model.pkl', 'rb'))

# App title and description
st.title("Gold Price Prediction App")
st.markdown("""
This app uses a trained **Random Forest Regressor** to predict the **Gold Price (GLD)** based on other financial indicators like SPX, Oil, Silver, and USD.
""")

# Input form for features
st.header("Enter the Financial Indicators:")

spx = st.number_input("SPX (S&P 500 Index)", value=1300.0, step=0.1)
oil = st.number_input("Oil Price", value=90.0, step=0.1)
silver = st.number_input("Silver Price", value=20.0, step=0.1)
usd = st.number_input("USD Index", value=90.0, step=0.1)

# Predict button
if st.button("Predict Gold Price"):
    input_data = np.array([[spx, oil, silver, usd]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Gold Price (GLD): ${prediction[0]:.2f}")

# Footer
st.markdown("---")
st.markdown("**Developed by Diya Chanda**")