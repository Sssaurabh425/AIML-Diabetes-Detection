import streamlit as st
import pickle
import numpy as np

diabetes = pickle.load(open("diabetes_model.sav", 'rb'))
scaler = pickle.load(open("scaler.sav", 'rb'))


st.title('Diabetes Detection')
preg = st.number_input("Enter the No. Of Pregnancies",value=1)
glu = st.number_input("Enter the Glucose Level",value=89)
bp = st.number_input("Enter the Blood Pressure Level",value=66)
skin = st.number_input("Enter the Skin Thickness",value=23)
insulin = st.number_input("Enter the Insulin Level",value=94)
bmi = st.number_input("Enter the BMI",value=28.1)
dpf = st.number_input("Enter the DPF",value=0.167)
age = st.number_input("Enter the Age",value=23)


if st.button('Predict'):
    input_data = (preg,glu,bp,skin,insulin,bmi,dpf,age)
    
    # Changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for an instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    # standardize the input data
    std_data = scaler.transform(input_data_reshaped)
    prediction = diabetes.predict(std_data)
    if(prediction[0]==1):
        st.header("The Person is Diabetic")
    else:
        st.header("The Person is Non Diabetic")
