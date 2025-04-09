# 🌟 Gold Price Prediction using Machine Learning

This project uses a **Random Forest Regressor** to predict the **Gold Price (GLD)** based on other financial indicators such as SPX (S&P 500), Oil Price, Silver Price, and USD Index. The model has been deployed as an interactive web app using **Streamlit**.

---

## 📊 Overview

Gold price is influenced by various economic indicators. This project aims to build a **machine learning model** that can accurately predict the gold price by analyzing these features.

**Tech Stack:**
- Python
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn (Random Forest)
- Streamlit (for web deployment)
- Streamlit Cloud (for hosting)

---

## 📁 Project Structure

.
├── st_app.py                      # Streamlit web app
├── gld_price_data.csv          # Dataset used
├── gold_price_prediction_model.pkl  # Trained ML model
├── requirements.txt            # Dependencies for the project
└── README.md                   # Project documentation (this file)



---

## 🚀 Live Demo

🔗 [Click here to view the deployed Streamlit App](https://gold-price-prediction-diya.streamlit.app/)  
> _(Replace the above link with your actual Streamlit Cloud app link)_

---

## 📌 Features

- 📈 Visualizes correlation between gold price and financial indicators
- 🔍 Trains a Random Forest model on historical data
- 🧠 Makes predictions based on user input
- 🌐 Deploys the model with an interactive UI using Streamlit

---

## 📥 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/gold-price-prediction.git
   cd gold-price-prediction
