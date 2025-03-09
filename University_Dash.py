import pandas as pd
import numpy as np
import streamlit as st

# Adding the title
st.title(" :bar_chart: University Student Trend Analysis")

# Loading the data
student_df = pd.read_excel("university_student_dashboard_data.xls")


# Adding KPIs
st.metric("Total Applications", f"${student_df['Applications'].sum():,.2f}")
st.metric("Total Admissions", f"${student_df['Admitted'].sum():,.2f}")
st.metric("Total Enrollments", f"${student_df['Enrolled'].sum():,.2f}")
st.metric("Total Science Enrollees", {student_df['Science Enrolled'].sum()})
st.metric("Total Engineering Enrollees", {student_df['Engineering Enrolled'].sum()})
st.metric("Total Business Enrollees", {student_df['Business Enrolled'].sum()})
st.metric("Total Arts Enrollees", {student_df['Arts Enrolled'].sum()})

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
