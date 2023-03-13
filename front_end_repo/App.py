import streamlit as st
from streamlit.components.v1 import iframe

import numpy as np
import pandas as pd

# background image
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
# title
st.set_page_config(layout="wide", page_title="University Prediction")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    pass
with col2:
    pass
    st.image("https://em-content.zobj.net/thumbs/240/apple/325/graduation-cap_1f393.png")
with col3:
    pass
with col4:
    pass
with col5:
    pass
st.title("Can you get to a top-tier University?")
st.subheader("")
st.subheader("")

st.markdown(
    """<style>
div[class*="stNumberInput"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 22px;
}
    </style>
    """, unsafe_allow_html=True)
st.markdown(
    """<style>
div[class*="stSelectbox"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 22px;
}
    </style>
    """, unsafe_allow_html=True)

# grade_10
col1, col2 = st.columns(2)
with col1:
    pass
    grade_10 = st.number_input("Add your 10th grade performance (%)", min_value=0.0, max_value=100.0, step=0.01, format="%.2f")
with col2:
    pass

# grade_12
col1, col2 = st.columns(2)
with col1:
    pass
    grade_12 = st.number_input("Add your 12th grade performance (%)", min_value=0.0, max_value=100.0, step=0.01, format="%.2f")
with col2:
    pass

# graduation_score
col1, col2 = st.columns(2)
with col1:
    pass
    graduation_score = st.number_input("Add your graduation performance (%)", min_value=0.0, max_value=100.0, step=0.01, format="%.2f")
with col2:
    pass

# gender
col1, col2 = st.columns(2)
with col1:
    pass
    gender = st.selectbox(
    "Choose your gender",
    ["","Female", "Male"], format_func=lambda x: 'Select an option' if x == '' else x,
    index=0,
)
if gender == "":
    col1, col2 = st.columns(2)
    with col1:
        pass
        st.error("No option is selected")
    with col2:
        pass
with col2:
    pass

# graduation_type
col1, col2 = st.columns(2)
with col1:
    pass
    graduation_type = st.selectbox(
    "Choose your graduation type",
    ["","Non-Engineer", "Engineer"], format_func=lambda x: 'Select an option' if x == '' else x,
    index=0,
)
if graduation_type == "":
    col1, col2 = st.columns(2)
    with col1:
        pass
        st.error("No option is selected")
    with col2:
        pass
with col2:
    pass

# work_ex
col1, col2 = st.columns(2)
with col1:
    pass
    work_ex = st.number_input("Add your work experience (months)", min_value=0.0, max_value=100.0, step=0.01, format="%.2f")
with col2:
    pass

# seat_category
col1, col2 = st.columns(2)
with col1:
    pass
    seat_category = st.selectbox(
    "Choose your category",
    ["","General", "EWS", "NC_OBC", "SC", "ST"], format_func=lambda x: 'Select an option' if x == '' else x,
    index=0,
)
if seat_category == "":
    col1, col2 = st.columns(2)
    with col1:
        pass
        st.error("No option is selected")
    with col2:
        pass
with col2:
    pass

# cat_score
col1, col2 = st.columns(2)
with col1:
    pass
    cat_score = st.number_input("Add your CAT score (0-100)", min_value=0.0, max_value=100.0, step=0.01, format="%.2f")
with col2:
    pass

# submit
submit = st.button("Submit ✅")
if submit:
    st.subheader("Congratulations! Your results are ready")
add_bg_from_url()
