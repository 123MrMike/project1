import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Cars EDA")
st.write("In this project we will import the vehicles_us.csv and performa simple EDA")

df=pd.read_csv(r'C:\\Users\Michael\project1\vehicles_us.csv')
clean_df=df.dropna().reset_index(drop=True)

st.subheader("Let's look at the dataset")

ck = st.checkbox("Without Nulls", value = False)
if ck == True:
    st.write(clean_df)
else:
    st.write(df)

st.write(px.histogram(clean_df, x='paint_color', title='Color Distribution'))

st.write(px.histogram(clean_df, x='price', title='Price Distribution'))

st.write(px.scatter(clean_df, x='price', y='model_year', title='Price correlation'))

st.write(boxplot=px.box(clean_df, x='price', title='Price IQR'))
