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


