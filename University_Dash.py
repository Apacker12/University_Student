#import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st

# Loading the data
student_df = pd.read_excel("university_student_dashboard_data.xls")

# Adding the title
st.title(" :bar_chart: University Student Trend Analysis")
