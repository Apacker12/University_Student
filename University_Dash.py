# To import libraries and packages
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# Loading the data
student_df = pd.read_excel("university_student_dashboard_data.xls")

# To add a title
st.title(" :bar_chart: University Student Trend Analysis")

# Adding a new column with the text "08" for any Term of "Fall" and "01" for any Term of "Spring"
student_df['Month'] = student_df['Term'].apply(lambda x: '08' if x == 'Fall' else ('01' if x == 'Spring' else ''))

# Concatenating the Month and Term columns with an "/01/" in between the two
student_df['Term_Date'] = student_df['Month'] + '/01/' + student_df['Year'].astype(str)

# To change the Term_Date column to a date type
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

# Calculating metrics using the filtered data
average_satisfaction = student_df3['Student Satisfaction (%)'].mean()
average_retention = student_df3['Retention Rate (%)'].mean()
admission_rate = (student_df3['Admitted'] / student_df3['Applications']) * 100
average_admission_rate = admission_rate.mean()

# To add the first plot's KPIs
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Science Enrollees", f"{student_df3['Science'].sum():,.0f}")
with col2:
    st.metric("Total Engineering Enrollees", f"{student_df3['Engineering'].sum():,.0f}")
with col3:
    st.metric("Total Business Enrollees", f"{student_df3['Business'].sum():,.0f}")
with col4:
    st.metric("Total Arts Enrollees", f"{student_df3['Arts'].sum():,.0f}")

# Creating a line plot for the type of Enrollees over time
fig1 = plt.figure(figsize=(12, 8))
plt.plot(student_df3['Term_Date'], student_df3['Science'], label='Science Enrollees', color='blue')
plt.plot(student_df3['Term_Date'], student_df3['Engineering'], label='Engineering Enrollees', color='green')
plt.plot(student_df3['Term_Date'], student_df3['Business'], label='Business Enrollees', color='red')
plt.plot(student_df3['Term_Date'], student_df3['Arts'], label='Arts Enrollees', color='purple')
plt.title('Enrollees Over Time by Category')
plt.xlabel('Date')
plt.ylabel('Number of Enrollees')
plt.legend()
st.pyplot(fig1)

# To add the second plot's KPIs
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Average Admission Rate", f"{average_admission_rate:.2f}%")
with col2:
    st.metric("Average Satisfaction", f"{average_satisfaction:.2f}%")
with col3:
    st.metric("Average Retention", f"{average_retention:.2f}%")

# Creating a line plot for the retention, satisfaction, and admission rates over time
fig2 = plt.figure(figsize=(12, 8))
plt.plot(student_df3['Term_Date'], student_df3['Retention Rate (%)'], label='Retention Rate', color='magenta')
plt.plot(student_df3['Term_Date'], student_df3['Student Satisfaction (%)'], label='Satisfaction', color='orange')
plt.plot(student_df3['Term_Date'], admission_rate, label='Admission Rate', color='cyan')
plt.title('Retention Rate, Satisfaction, and Admission Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Rate')
plt.legend()
st.pyplot(fig2)

# To add the third plot's KPIs
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Enrollments", f"{student_df3['Enrolled'].sum():,.0f}")
with col2:
    st.metric("Total Applications", f"{student_df3['Applications'].sum():,.0f}")
with col3:
    st.metric("Total Admissions", f"{student_df3['Admitted'].sum():,.0f}")

# Creating a line plot for the Applications, Admitted, and Enrolled
fig3 = plt.figure(figsize=(12, 8))
plt.plot(student_df3['Term_Date'], student_df3['Applications'], label='Applications', color='teal')
plt.plot(student_df3['Term_Date'], student_df3['Admitted'], label='Admitted', color='navy')
plt.plot(student_df3['Term_Date'], student_df3['Enrolled'], label='Enrolled', color='maroon')
plt.title('Applications, Admitted, and Enrolled Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Students')
plt.legend()
st.pyplot(fig3)

# Creating a data table
st.subheader("University Student Data")
st.dataframe(student_df3)
