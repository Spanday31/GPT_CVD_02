import math
import streamlit as st

@st.cache_data
def calculate_smart_risk(age, sex, sbp, total_chol, hdl, smoker, diabetes, egfr, crp, vasc_count):
    return 10.0