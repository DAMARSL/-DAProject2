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
col1, col_mid, col2 = st.columns([1, 0.02, 2])

# === SOL KISIM: Kullanıcı Girdileri ===
with col1:
    st.header("Customer Churn Prediction")

    internet_service = st.selectbox("What is Internet Service?", ["No", "DSL", "Fiber optic"], index=2)
    payment_method = st.selectbox("What is Payment Method?", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"], index=0)
    monthly_charges = st.number_input("Enter Monthly Charges", min_value=0, max_value=200, value=70)
    tech_support = st.radio("Do you get Technical Support?", ["Yes", "No", "No internet service"], index=2)
    device_protection = st.radio("Have you Device Protection?", ["Yes", "No", "No internet service"], index=2)
    streaming_tv = st.radio("Have you Streaming TV?", ["Yes", "No", "No internet service"], index=2)
    online_backup = st.radio("Do you have Online Backup?", ["Yes", "No", "No internet service"], index=2)
    online_security = st.radio("Do you have Online Security?", ["Yes", "No", "No internet service"], index=2)
    streaming_movies = st.radio("Have you Streaming Movies?", ["Yes", "No", "No internet service"], index=2)
    dependents = st.radio("Do you have Dependents?", ["Yes", "No"], index=0)
    contract = st.selectbox("Please chose your Contract scope.", ["Month-to-month", "One year", "Two year"], index=2)
    tenure_months = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=10)

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

    user_df = pd.DataFrame([user_data])

    # Modeli yükle
    with open('random_forest_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    prediction = model.predict(user_df)

    # Tahmin sonucu
    if prediction[0] == 0:
        st.subheader("Customer will NOT churn 🙂")
    else:
        st.subheader(" ⚠️ Customer will churn 😟")

# === SAĞ KISIM: Tahmin ve Dashboard ===
with col2:
    st.header("About Dataset")
    st.markdown("---")
    st.markdown("""The Telco Customer Churn dataset contains information about a fictional telecommunications company’s customers. It is commonly used for building predictive models that aim to identify customers who are at risk of churning — that is, canceling their subscription.
     
The dataset includes:

Demographic details such as gender, senior citizen status, dependents, and marital status.

Service-related features, including whether the customer subscribes to services like internet, online security, tech support, device protection, and streaming (TV/movies).

Contract and billing information, such as contract type (monthly or yearly), payment method, monthly charges, and tenure (how long the customer has been with the company).

The target variable: Churn — indicating whether the customer has left the company or not.""")
    st.markdown("---")
    st.subheader("Source Analysis with EDA")
    power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=da7aa0de-ff6f-428e-b4ae-8e3defef0dd5&autoAuth=true&ctid=e4dddef5-d743-42fa-99da-83120e7bf32e"
    components.iframe(power_bi_url, width=900, height=450)
