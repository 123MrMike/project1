import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Cars EDA")
st.write("In this project we will import the vehicles_us.csv and performa simple EDA")

df=pd.read_csv('vehicles_us.csv')
clean_df=df.dropna().reset_index(drop=True)

st.subheader("Let's look at the dataset")

ck = st.checkbox("Without Nulls", value = False)
if ck == True:
    st.write(clean_df.head())
    st.write(clean_df.isnull().sum())
    st.write(clean_df.info())
else:
    st.write(df.head())
    st.write(df.isnull().sum())
    st.write(df.info())

st.markdown("Ok, so the data seems to be unclean. I'm concerned about the thousands of missing values in **model_year**, **cylinders**, **odometer**, **paint_color**, and **is_4wd**. Out of 51,525 entries, a large fraction of entries are missing in those columns. Eliminate all Nulls by checking the box.")
st.write("Even though we eliminate over 2/3's of our data by excluding all Nulls, I believe 14,852 entries is still plenty of data for a simple EDA. We'll just have to bear in mind that our Statistc population is now much smaller. Now let's visualize our DataFrame.")

st.subheader("EDA")
st.write("Next we'll make a couple of Histograms and scatterplots")

st.write(px.histogram(clean_df, x='paint_color', title='Color Distribution'))
st.write("It looks like people like white cars the most. Black comes in second, followed by silver and blue.")

st.write(px.histogram(clean_df, x='price', title='Price Distribution'))
st.write("The price distribution is heavily skewed to the left, suggesting great outliers in expensive cars.")

st.write(px.scatter(clean_df, x='price', y='model_year', title='Price correlation'))
st.write("Here we've compared the cars price against the model year. Newer cars populate the majority of the data set. There is a positive correlation between new cars and higher prices. We can also point out the extreme outliers that threw off the average disrtibution in the previous Histogram. Some overpriced cars from the late 90's to early 2000's (perhaps vintage collectables) are skewing the entire visual to the far outskirts of 100,000 and greater price range, when in fact the majority of the data is in the 80,000 and lower range.")
st.markdown(" This is were the differences between Averages and Medians come into play. Averages are suscepltible to be skewed by outliers. **Median statistics are more robust**. infact let's throw in an additional visualization to demonstrate.")

st.write(px.box(clean_df, x='price', title='Price IQR'))
st.write("A better Statistical model would be the IQR (Inter Quartile Range), which is the difference between the 1st and 3rd quartile. A quartile is a marker for a quarter of the data points. The Median is the middle data point in our data set, meanwhile IQR marks the range for the middle 50 percent of the data")
st.write("By the way. In the Box plot above, the IQR is the greyed-out area in the box")

st.write("- Q1 marks the first 25 percent of the data points.")
st.write("- Q2 AKA the Median marks the first 50 percent of the data points.")
st.write("- Q3 marks the first 75 percent of the data points.")
st.write("- IQR = Q3-Q1")

st.write("Our Q3 is 22,000. Our Q1 is 7,000. 22,000 - 7,000 = 15,000 is our IQR.")
st.write("Which means the middle 50 percent of the cars in our data set are *actually* around the 15,000 dollar range, with a Median of 13,500. This statistical analysis is a great way to factor out extreme outliers.")