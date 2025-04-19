# === SAĞ KISIM: Tahmin ve Dashboard ===
with col2:
    st.header("Prediction Result & Dashboard")

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

    # === Tahmin sonucunu hemen giriş alanlarının altına göster ===
    with st.container():
        if prediction[0] == 0:
            st.success("Customer will NOT churn 🙂")
        else:
            st.warning("⚠️ Customer will churn 😟")

    st.markdown("---")

    # === Kısa açıklama ekle ===
    st.subheader("About the Telco Dataset")
    st.markdown("""
    The **Telco Customer Churn** dataset contains information about customers of a fictional telecom company.
    It includes service usage, account details, and demographic data.  
    The primary goal is to predict whether a customer is likely to **churn** (leave the service).
    """)

    # === Power BI Dashboard ===
    st.subheader("Source Analysis with EDA")
    power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=da7aa0de-ff6f-428e-b4ae-8e3defef0dd5&autoAuth=true&ctid=e4dddef5-d743-42fa-99da-83120e7bf32e&navContentPaneEnabled=false&filterPaneEnabled=false"
    components.iframe(power_bi_url, width=800, height=400)
