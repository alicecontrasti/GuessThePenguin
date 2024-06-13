import streamlit as st
import pandas as pd
#import xlsxwriter
import seaborn as sns
import matplotlib.pyplot as plt

###### CSS BACKGROUND #######################
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2014/08/27/12/58/emperor-penguins-429128_1280.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

import joblib

model_pipe = joblib.load('penguinspipe.pkl')

st.title("Let's Play: Guess the Species!")

island = st.selectbox("Select your favourite island", 
                       ["Torgersen","Biscoe","Dream"])

bill_length = st.slider("Insert your Penguin's Bill Length (use mm)",25,65,40)
bill_depth = st.slider("Insert your Penguin's Bill Depth (use mm)",8,30,20)
flipper_length = st.slider("Insert your Penguin's Flipper Length (use mm)",150,250,200)
body_mass = st.slider("Insert your Penguin's Body Mass (use g)",2000,7000,4200)


sex = st.radio("Select the gender of your lovely Penguin", ["Male", "Female"])

data = {
        "island": [island],
        "bill_length_mm": [bill_length],
        "bill_depth_mm": [bill_depth],
        "flipper_length_mm":[flipper_length],
        "body_mass_g": [body_mass],
        "sex": [sex],
        }

input_df = pd.DataFrame(data)

if st.button("Prediction"):
    res = model_pipe.predict(input_df).astype(int)[0]

    classes = {0:'Adelie',
           1:'Gentoo',
           2:'Chinstrap',
           }

    y_pred = classes[res]

    st.success(f'Your Penguin belongs to the species: {y_pred}')

st.toast("Aren't they cute?!", icon='😍')
st.snow()
