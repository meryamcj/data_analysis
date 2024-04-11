from operator import index
import streamlit as st
import plotly.express as px
from ydata_profiling import ProfileReport
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os 

if os.path.exists('./dataset.csv'): 
    df = pd.read_csv('dataset.csv', index_col=None)

with st.sidebar: 
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("Proyecto Aplicado")
    choice = st.radio("Navigation", ["Details"])
    st.info("This project application explore our data.")

if choice == "Upload":
    st.title("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset")
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

if choice == "Details": 
    st.title("Exploratory Data Analysis for Punrecpsic")
    df.to_csv('dataset.csv', index=None)
    st.dataframe(df)
    #profile_df = df.profile_report()ProfileReport(df, title='Pandas Profiling Report')
    profile_df = ProfileReport(df, title='Pandas Profiling Report')
    st_profile_report(profile_df)
