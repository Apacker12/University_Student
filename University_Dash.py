#import required libraries/packages
import pandas as pd
import numpy as np
import streamlit as st

# Loading the data
student_df = pd.read_excel("university_student_dashboard_data.xls")

# Adding the title
st.title(" :bar_chart: University Student Trend Analysis")

# To calculate average satisfaction & retention rate
average_satisfaction = student_df['Student Satisfaction (%)'].mean()
average_retention = student_df['Retention Rate (%)'].mean()

# Adding KPIs
col1,col2, col3=st.columns(3)
with col1:
  st.metric("Total Applications", f"{student_df['Applications'].sum():,.0f}")
  st.metric("Total Science Enrollees", f"{student_df['Science Enrolled'].sum():,.0f}")
  st.metric("Total Arts Enrollees", f"{student_df['Arts Enrolled'].sum():,.0f}")
with col2:
  st.metric("Total Admissions", f"{student_df['Admitted'].sum():,.0f}")
  st.metric("Total Engineering Enrollees", f"{student_df['Engineering Enrolled'].sum():,.0f}")
  st.metric("Average Satisfaction", f"{average_satisfaction:.2f}%")
with col3:
  st.metric("Total Enrollments", f"{student_df['Enrolled'].sum():,.0f}")
  st.metric("Total Business Enrollees", f"{student_df['Business Enrolled'].sum():,.0f}")
  st.metric("Average Rentention", f"{average_retention:.2f}%")

# Adding a new column with the text "08" for any Term of "Fall" and "01" for any Term of "Spring"
student_df['Month'] = student_df['Term'].apply(lambda x: '08' if x == 'Fall' else ('01' if x == 'Spring' else ''))

# Concatenating the Month and Term columns with an "/01/" in between the two
student_df['Term_Date'] = student_df['Month'] + '/01/' + student_df['Year'].astype(str)

# Changing the Term_Date column to a date type
student_df['Term_Date'] = pd.to_datetime(student_df['Term_Date'])

# Removing "Enrolled" from the column header
student_df = student_df.rename(columns={'Engineering Enrolled': 'Engineering', 'Business Enrolled': 'Business', 'Arts Enrolled': 'Arts', 'Science Enrolled': 'Science'})

st.sidebar.header("Choose your filter: ")

# Creating a filter for the Year
year = st.sidebar.multiselect("Select the Year", student_df["Year"].unique())
if not year:
    student_df2 = student_df.copy()
else:
    student_df2 = student_df[student_df["Year"].isin(year)]

# Creating a filter for the Term
term = st.sidebar.multiselect("Select the Term", student_df2["Term"].unique())
if not term:
    student_df3 = student_df2.copy()
else:
    student_df3 = student_df2[student_df2["Term"].isin(term)]

# Data Table
st.subheader("University Student Data")
st.dataframe(student_df3)
