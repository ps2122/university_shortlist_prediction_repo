import streamlit as st
from streamlit.components.v1 import iframe

import numpy as np
import pandas as pd

def add_bg_from_url():

    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-photo/teacher-s-day-elements-composition_23-2149044935.jpg?w=1800&t=st=1678489990~exp=1678490590~hmac=764aafe42f10341fbd6603849f1e692103b8bd19110621562c155d1c3b0dda29");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

st.set_page_config(layout="wide", page_title="University Prediction")
st.title("Can you get to a top-tier University 🎓?")
st.subheader("Check it now")
#st.markdown('<div style="text-align: center;">Check it now</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    pass
    grade_10 = st.text_input("Add your 10th grade performance (%)")
with col2:
    pass

col1, col2 = st.columns(2)
with col1:
    pass
    grade_12 = st.text_input("Add your 12th grade performance (%)")
with col2:
    pass

col1, col2 = st.columns(2)
with col1:
    pass
    graduation_score = st.text_input("Add your graduation performance (%)")
with col2:
    pass

col1, col2 = st.columns(2)
with col1:
    pass
    gender = st.selectbox(
    "Choose your gender",
    ["","Female", "Male"],
    index=0,
)
with col2:
    pass

col1, col2 = st.columns(2)
with col1:
    pass
    graduation_type = st.selectbox(
    "Choose your graduation type",
    ["","Engineer", "Non-Engineer"],
    index=0,
)
with col2:
    pass

col1, col2 = st.columns(2)
with col1:
    pass
    work_ex = st.text_input("Add your work experience (months)")
with col2:
    pass

col1, col2 = st.columns(2)
with col1:
    pass
    seat_category = st.selectbox(
    "Choose your category",
    ["","General", "EWS", "NC_OBC", "SC", "ST"],
    index=0,
)
with col2:
    pass

col1, col2 = st.columns(2)
with col1:
    pass
    cat_score = st.text_input("Add your CAT score (0-100)")
with col2:
    pass

submit = st.button('Submit ✅')
if submit:
    st.subheader("Congratulations! Your results are ready")
add_bg_from_url()
