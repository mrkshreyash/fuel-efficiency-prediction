# import pickle

from logging import exception
import time
from tkinter import E
from typing import Container
from urllib import request
import numpy as np
import pickle
import streamlit as st
import os
from sklearn.preprocessing import StandardScaler
import tensorflow
import requests
from streamlit_lottie import st_lottie

st.set_page_config("Fuel Efficiency Prediction", ":tada:", layout="wide")



sc = StandardScaler()

# _----------------------------------------------------------------



# _----------------------------------------------------------------


def Prediction(values):
    path = "models/"

    scaler_path = os.path.join(os.path.dirname(
        "models/"),
        'scaler.pkl')

    sc = None
    with open(scaler_path, 'rb') as f:
        sc = pickle.load(f)

    values = sc.transform(values)

    model = tensorflow.keras.models.load_model(
        "models/model.h5")

    return model.predict(values)

def main():




    # ---- Greet & Project Info
    with st.container():

        st.title("Welcome to Fuel Efficiency Prediction".upper(), ":tada:")
        st.write("---")

        col1, col2 = st.columns([2,1])

        with col1:
            


            st.subheader("This project is for to predict the efficiency of a car using their features.")
            st.markdown("""
                \n\n **How to Calculate efficiency???**
                """)

        

            st.write("##")

            st.text("""\n\n\n
                It's very easy. You have to just fill below information

                about your car. And you will get the resulting output of

                a car that how much a car can travel distance 

                in  Miles per Gallon or Kilo-Meter per Litre.
            """)

        with col2:
            try:            
                #LottieFiles sets here

                def load_lottieurl(url):
                    r = requests.get(url)
                    if r.status_code != 200:
                        return None

                    return r.json()

                lottie_car = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_a3emlnqk.json") # LottieFiles URL
                st_lottie(lottie_car, height=300, key='Moving Car')
            except Exception as e:
                st.write("Check Your Internet Connection...")

        st.write("---")

    # ---- Get Input from users
    with st.container():
        Cylinder = st.number_input("Cylinder")

        displacement = st.number_input("Displacement")

        horsepower = st.number_input("HorsePower")

        weight = st.number_input("Weight")

        acceleration = st.number_input("Acceleration")

        model_year = st.number_input("Model Year")

        origin = st.number_input("Origin")

        prediction = Prediction([[Cylinder, displacement, horsepower, weight, acceleration, model_year, origin]])

        st.write("---")
        try:
            if st.button("Submit & Predict"):

                st.write("---")

                with st.spinner('Wait for it...'):
                    time.sleep(1.5)

                st.subheader("The Prediction is : ")
                st.write(" You car can go  ")
                st.write( float(prediction), " MPG")
                st.write("or")
                st.write(float(prediction*0.425) ," KML")
                st.balloons()

        except Exception as e:
            st.write("Error : " , e)

        
    with st.container():

        st.write("---")

        if st.button("Show Credits."):

            st.write("""

                This project is creted by     

                     Shreyash Avinash Kamble                  
                  
            """)

if __name__ == '__main__':
    main()
