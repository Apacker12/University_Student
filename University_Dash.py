#import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st

# Loading the data
student_df = pd.read_excel("university_student_dashboard_data.xls")

# Adding the title
st.title(" :bar_chart: University Student Trend Analysis")

# Adding KPIs
st.metric("Total Applications", f"${student_df['Applications'].sum():,.2f}")
st.metric("Total Admissions", f"${student_df['Admitted'].sum():,.2f}")
st.metric("Total Enrollments", f"${student_df['Enrolled'].sum():,.2f}")
st.metric("Total Science Enrollees", {student_df['Science Enrolled'].sum()})
st.metric("Total Engineering Enrollees", {student_df['Engineering Enrolled'].sum()})
st.metric("Total Business Enrollees", {student_df['Business Enrolled'].sum()})
st.metric("Total Arts Enrollees", {student_df['Arts Enrolled'].sum()})
