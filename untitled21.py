import streamlit as st
import pandas as pd
import pickle
import streamlit.components.v1 as components

st.set_page_config(layout="wide")  # Sayfayı geniş modda başlat

# Başlık ve görsel
st.markdown("""
    <style>
    h1 {
        color: #6c575d;
        text-align: center;
    }
    </style>
    <h1>Telco Customer Churn Prediction</h1>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center;">
        <img src="https://www.cleartouch.in/wp-content/uploads/2022/11/Customer-Churn.png" width="80%" />
    </div>
""", unsafe_allow_html=True)

# Sayfa iki sütuna bölünüyor
col1, col2 = st.columns([1, 2])  # Sol daha dar, sağ daha geniş

# === SOL KISIM: Kullanıcı Girdileri ===
with col1:
    st.header("Customer Info")

    internet_service = st.selectbox("Internet Service", ["No", "DSL", "Fiber optic"], index=2)
    payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"], index=0)
    monthly_charges = st.number_input("Monthly Charges", min_value=0, max_value=200, value=70)
    tech_support = st.radio("Tech Support", ["Yes", "No", "No internet service"], index=2)
    device_protection = st.radio("Device Protection", ["Yes", "No", "No internet service"], index=2)
    streaming_tv = st.radio("Streaming TV", ["Yes", "No", "No internet service"], index=2)
    online_backup = st.radio("Online Backup", ["Yes", "No", "No internet service"], index=2)
    online_security = st.radio("Online Security", ["Yes", "No", "No internet service"], index=2_
