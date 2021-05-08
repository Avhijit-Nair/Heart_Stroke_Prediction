import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

def welcome():
    return 'welcome all'

def prediction(gender, age1, hypertension, heart_disease,married,work_type1,residence,avg_glucose1,bmi1,smoking_stat1):  
    age = [0,0,0,0]
    work_type = [0,0,0,0,0]
    glucose_level = [0,0,0,0]
    bmi = [0,0,0,0]
    smoking = [0,0,0,0]
    if gender=="Male":
    	gender=0
    else:
    	gender=1

    if hypertension=="Yes":
    	hypertension=1
    else:
    	hypertension=0

    if heart_disease=="Yes":
    	heart_disease=1
    else:
    	heart_disease=0

    if married=="Yes":
    	married=1
    else:
    	married=0

    if residence=="Rural":
    	residence=1
    else:
    	residence=0

    if age1>=20 and age1<40:
    	age[0]=1
    elif age1>=40 and age1<60:
    	age[1]=1
    elif age1>=60:
    	age[2]=1
    else:
    	age[3]=1

    if avg_glucose1<77:
    	glucose_level[3]=1
    elif avg_glucose1<91:
    	glucose_level[0]=1
    elif avg_glucose1<114:
    	glucose_level[1]=1
    else:
    	glucose_level[2]=1

    if work_type1=="Govt job":
    	work_type[0]=1
    elif work_type1=="Never worked":
    	work_type[1]=1
    elif work_type1=="Private":
    	work_type[2]=1
    elif work_type1=="Self-employed":
    	work_type[3]=1
    else:
    	work_type[4]=1

    if bmi1<23:
    	bmi[3]=1
    elif bmi1<28:
    	bmi[0]=1
    elif bmi1<33:
    	bmi[1]=1
    else:
    	bmi[2]=1

    if smoking_stat1=="Unknown":
    	smoking[0]=1
    elif smoking_stat1=="Formerly smoked":
    	smoking[1]=1
    elif smoking_stat1=="Never smoked":
    	smoking[2]=1
    else:
    	smoking[3]=1

    prediction = classifier.predict(
        [[gender,hypertension,heart_disease,married,residence,age[0],age[1],age[2],age[3],glucose_level[0],glucose_level[1],glucose_level[2],glucose_level[3],
        work_type[0],work_type[1],work_type[2],work_type[3],work_type[4],bmi[0],bmi[1],bmi[2],bmi[3],smoking[0],smoking[1],smoking[2],smoking[3]]])
    #print(heart_disease)
    return prediction

def main():
	st.title("Heart ❤ Stroke Prediction App")
	html_temp=""
	ans=0
	st.markdown(html_temp,unsafe_allow_html = True)
	get_Gender = st.sidebar.radio("Select your gender",("Male","Female"))
	get_Hypertension = st.sidebar.radio("Do you have hypertension?",("Yes","No"))
	get_heartDisease = st.sidebar.radio("Do you have heart disease?",("Yes","No"))
	get_married = st.sidebar.radio("Have you ever been married?",("Yes","No"))
	get_residence = st.selectbox("Select your residence type",("Rural","Urban"))
	get_age = st.slider("How old are you?",value=25)
	get_workType = st.selectbox("Select the type of work you do.",("Govt job","Never worked","Private","Self-employed","Children"))
	get_bmi = st.slider("How much is your bmi?",min_value=10,max_value=100,value=65)
	get_glucose = st.slider("How much is your glucose level?",min_value=55,max_value=272,value=50)
	get_smoke = st.selectbox("What's your smoking history",("Unknown","Formerly smoked","Never smoked","Smokes"))

	if st.button("Predict"):
		ans=prediction(get_Gender,get_age,get_Hypertension,get_heartDisease,get_married,get_workType,get_residence,get_glucose,get_bmi,get_smoke)[0]
		if ans==0:
			st.success('You have no chance of getting stroke😊')
			st.image('images/happy_heart.jfif')
		else:
			st.success('You are at risk of getting stroke😥')
			st.image('images/damaged_heart.jfif')

if __name__=='__main__':
    main()