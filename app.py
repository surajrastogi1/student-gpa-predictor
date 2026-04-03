import streamlit as st
import pandas as pd
import numpy as np
import joblib

# --- LOAD ASSETS ---
# Loading the model and scaler you exported in cell [27] of your notebook
model = joblib.load('knn_model.pkl')
scaler = joblib.load('scaler.pkl')

st.set_page_config(page_title="GPA Predictor", page_icon="🎓")

st.title("🎓 Student GPA Predictor")
st.write("Enter the student's details in the sidebar to predict their GPA.")

# --- SIDEBAR INPUTS ---
st.sidebar.header("Student Metrics")

def get_user_input():
    age = st.sidebar.slider("Age", 15, 18, 17)
    gender = st.sidebar.selectbox("Gender", [0, 1], format_func=lambda x: "Male" if x==1 else "Female")
    ethnicity = st.sidebar.selectbox("Ethnicity", [0, 1, 2, 3], help="0: Caucasian, 1: African Am, 2: Asian, 3: Other")
    parental_ed = st.sidebar.selectbox("Parental Education", [0, 1, 2, 3, 4], help="0: None, 4: Higher")
    study_time = st.sidebar.slider("Weekly Study Time (hrs)", 0.0, 40.0, 15.0)
    absences = st.sidebar.slider("Absences", 0, 30, 5)
    tutoring = st.sidebar.radio("Tutoring", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    parental_support = st.sidebar.slider("Parental Support Level", 0, 4, 2)
    extracurricular = st.sidebar.radio("Extracurriculars", [0, 1])
    sports = st.sidebar.radio("Sports", [0, 1])
    music = st.sidebar.radio("Music", [0, 1])
    volunteering = st.sidebar.radio("Volunteering", [0, 1])
    grade_class = st.sidebar.selectbox("Grade Class", [0.0, 1.0, 2.0, 3.0, 4.0])

    features = {
        'Age': age, 'Gender': gender, 'Ethnicity': ethnicity,
        'ParentalEducation': parental_ed, 'StudyTimeWeekly': study_time,
        'Absences': absences, 'Tutoring': tutoring, 'ParentalSupport': parental_support,
        'Extracurricular': extracurricular, 'Sports': sports, 'Music': music,
        'Volunteering': volunteering, 'GradeClass': grade_class
    }
    return pd.DataFrame(features, index=[0])

df_input = get_user_input()

# --- PREDICTION ---
st.subheader("Student Profile Summary")
st.write(df_input)

if st.button("Predict GPA"):
    # 1. Scale the input using the loaded scaler
    scaled_data = scaler.transform(df_input)
    
    # 2. Make prediction
    prediction = model.predict(scaled_data)
    
    # 3. Output result
    st.success(f"### Predicted GPA: {prediction[0]:.2f}")
    
    # Visual Feedback
    if prediction[0] >= 3.0:
        st.balloons()