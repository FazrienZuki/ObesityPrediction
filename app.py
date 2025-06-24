import streamlit as st
import pandas as pd
import joblib

model = joblib.load("obesitymodel.pkl")

st.title("Obesity Level Predictor")
st.markdown("Predict obesity level based on your physical and lifestyle attributes.")

# User input form
with st.form("prediction_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.slider("Age", 10, 100, 25)
    height = st.number_input("Height (in cm)", min_value=100, max_value=200, value=170)
    weight = st.number_input("Weight (in kg)", min_value=20.0, max_value=200.0, value=70.0)
    family_history = st.selectbox("Family History with Overweight", ["yes", "no"])
    favc = st.selectbox("Frequent consumption of high caloric food (FAVC)", ["yes", "no"])
    fcvc = st.slider("Frequency of vegetable consumption (1-3)", 1, 3, 2)
    ncp = st.slider("Number of main meals (1-4)", 1, 4, 3)
    caec = st.selectbox("Consumption of food between meals (CAEC)", ["no", "Sometimes", "Frequently", "Always"])
    smoke = st.selectbox("Do you smoke?", ["yes", "no"])
    ch2o = st.slider("Daily water intake (CH2O)", 0, 5, 2)
    scc = st.selectbox("Do you monitor your calories?", ["yes", "no"])
    faf = st.slider("Physical activity frequency (FAF)", 0, 3, 1)
    alcohol = st.selectbox("Do you consume alcohol?", ["no", "Sometimes", "Frequently", "Always"])
    tue = st.slider("Time using technology devices (TUE)", 0, 3, 1)
    mtrans = st.selectbox("Transportation used", ["Automobile", "Motorbike", "Bike", "Public_Transportation", "Walking"])

    submit = st.form_submit_button("Predict")

if submit:
    # Prepare input DataFrame
    input_data = pd.DataFrame({
        "Gender": [gender],
        "Age": [age],
        "Height": [height],
        "Weight": [weight],
        "Family History with Overweight": [family_history],
        "Frequent consumption of high caloric food": [favc],
        "Frequency of consumption of vegetables": [fcvc],
        "Number of main meals": [ncp],
        "Consumption of food between meals": [caec],
        "Smoke": [smoke],
        "Consumption of water daily": [ch2o],
        "Calories consumption monitoring": [scc],
        "Physical activity frequency": [faf],
        "Consumption of alcohol": [alcohol],
        "Time using technology devices": [tue],
        "Transportation used": [mtrans]
    })

    # Predict
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Obesity Level: **{prediction}**")
