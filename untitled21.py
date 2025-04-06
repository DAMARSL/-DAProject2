# -*- coding: utf-8 -*-
"""Untitled22.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q2j8yMH4nEGDNenGCOFthZjjClPZhJvZ
"""


import streamlit as st
import pandas as pd
import pickle

# Başlık
st.title("Telecom Churn Prediction")

# Resim ekleme
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://www.cleartouch.in/wp-content/uploads/2022/11/Customer-Churn.png" width="80%" />
    </div>
    """, unsafe_allow_html=True)


# Kullanıcıdan veri almak için widget'lar

# Categorical features
internet_service = st.selectbox(
    "Internet Service", ["No", "DSL", "Fiber optic"], index=2
)

payment_method = st.selectbox(
    "Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"], index=0
)

# Numerical features
monthly_charges = st.number_input("Monthly Charges", min_value=0, max_value=200, value=70)


tech_support = st.radio(
    "Tech Support", ["Yes", "No", "No internet service"], index=2
)

device_protection = st.radio(
    "Device Protection", ["Yes", "No", "No internet service"], index=2
)

streaming_tv = st.radio(
    "Streaming TV", ["Yes", "No", "No internet service"], index=2
)

online_backup = st.radio(
    "Online Backup", ["Yes", "No", "No internet service"], index=2
)

online_security = st.radio(
    "Online Security", ["Yes", "No", "No internet service"], index=2
)

streaming_movies = st.radio(
    "Streaming Movies", ["Yes", "No", "No internet service"], index=2
)

dependents = st.radio("Dependents", ["Yes", "No"], index=0)

contract = st.selectbox(
    "Contract", ["Month-to-month", "One year", "Two year"], index=2
)

tenure_months = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=10)

# Kullanıcıdan alınan verileri bir DataFrame'e dönüştürme
user_data = {
    "Internet Service_Fiber optic": 1 if internet_service == "Fiber optic" else 0,
    "Payment Method_Electronic check": 1 if payment_method == "Electronic check" else 0,
    "Monthly Charges": monthly_charges,
    "Tech Support_No internet service": 1 if tech_support == "No internet service" else 0,
    "Device Protection_No internet service": 1 if device_protection == "No internet service" else 0,
    "Internet Service_No": 1 if internet_service == "No" else 0,
    "Streaming TV_No internet service": 1 if streaming_tv == "No internet service" else 0,
    "Online Backup_No internet service": 1 if online_backup == "No internet service" else 0,
    "Online Security_No internet service": 1 if online_security == "No internet service" else 0,
    "Streaming Movies_No internet service": 1 if streaming_movies == "No internet service" else 0,
    "Dependents_Yes": 1 if dependents == "Yes" else 0,
    "Contract_Two year": 1 if contract == "Two year" else 0,
    "Tenure Months": tenure_months
}

# Verileri DataFrame'e dönüştürme
user_df = pd.DataFrame([user_data])

# Modeli yükleme
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Tahmin yapma
prediction = model.predict(user_df)

# Tahminin sonucu
if prediction[0] == 0:
    st.subheader("Customer will NOT churn:)")
else:
    st.subheader("Customer will churn:(")

import streamlit as st

