#import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st

# Loading the data
student_df = pd.read_excel("university_student_dashboard_data.xls")

# Adding the title
st.title(" :bar_chart: University Student Trend Analysis")

#To change the required columns to a integar data type
student_df['Applications'] = student_df['Applications'].astype(int)
student_df['Admitted'] = student_df['Admitted'].astype(int)
student_df['Enrolled'] = student_df['Enrolled'].astype(int)
student_df['Science Enrolled'] = student_df['Science Enrolled'].astype(int)
student_df['Engineering Enrolled'] = student_df['Engineering Enrolled'].astype(int)
student_df['Business Enrolled'] = student_df['Business Enrolled'].astype(int)
student_df['Arts Enrolled'] = student_df['Arts Enrolled'].astype(int)

# Adding KPIs
st.metric("Total Applications", {student_df['Applications'].sum()})
st.metric("Total Admissions", {student_df['Admitted'].sum()})
st.metric("Total Enrollments", {student_df['Enrolled'].sum()})
st.metric("Total Science Enrollees", {student_df['Science Enrolled'].sum()})
st.metric("Total Engineering Enrollees", {student_df['Engineering Enrolled'].sum()})
st.metric("Total Business Enrollees", {student_df['Business Enrolled'].sum()})
st.metric("Total Arts Enrollees", {student_df['Arts Enrolled'].sum()})
