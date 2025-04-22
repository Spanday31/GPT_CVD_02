import streamlit as st
from datetime import datetime
import json
import pandas as pd
import matplotlib.pyplot as plt

# ✅ Correct imports without dots for Streamlit Cloud
from calculations import (
    calculate_smart_risk, calculate_ldl_effect, validate_drug_classes,
    calculate_ldl_reduction, generate_recommendations
)
from constants import LDL_THERAPIES
from pdf_generator import create_pdf_report
from utils import load_logo

# ======================
# Streamlit Page Config
# ======================
st.set_page_config(page_title="PRIME CVD Risk Calculator", layout="wide", page_icon="❤️")

# ======================
# HEADER
# ======================
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown("""
    <div style='background:linear-gradient(135deg,#3b82f6,#2563eb);padding:1rem;border-radius:10px;'>
        <h1 style='color:white;margin:0;'>PRIME CVD Risk Calculator</h1>
        <p style='color:#e0f2fe;margin:0;'>Secondary Prevention After Myocardial Infarction</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    load_logo()

# ======================
# SIDEBAR: PATIENT INPUTS
# ======================
st.sidebar.title("Patient Demographics")
age = st.sidebar.number_input("Age (years)", min_value=30, max_value=100, value=65)
sex = st.sidebar.radio("Sex", ["Male", "Female"], horizontal=True)
diabetes = st.sidebar.checkbox("Diabetes mellitus")
smoker = st.sidebar.checkbox("Current smoker")

st.sidebar.title("Vascular Disease")
cad = st.sidebar.checkbox("Coronary artery disease (CAD)")
stroke = st.sidebar.checkbox("Cerebrovascular disease (Stroke/TIA)")
pad = st.sidebar.checkbox("Peripheral artery disease (PAD)")
vasc_count = sum([cad, stroke, pad])

st.sidebar.title("Biomarkers")
total_chol = st.sidebar.number_input("Total Cholesterol (mmol/L)", 2.0, 10.0, 5.0, 0.1)
hdl = st.sidebar.number_input("HDL-C (mmol/L)", 0.5, 3.0, 1.0, 0.1)
ldl = st.sidebar.number_input("LDL-C (mmol/L)", 0.5, 6.0, 3.5, 0.1)
sbp = st.sidebar.number_input("SBP (mmHg)", 90, 220, 140)
egfr = st.sidebar.slider("eGFR (mL/min/1.73m²)", 15, 120, 80)
crp = st.sidebar.number_input("hs-CRP (mg/L)", 0.1, 20.0, 2.0, 0.1)

if ldl < hdl:
    st.sidebar.error("LDL-C cannot be lower than HDL-C!")

# ======================
# RISK CALCULATION
# ======================
baseline_risk = calculate_smart_risk(age, sex, sbp, total_chol, hdl, smoker, diabetes, egfr, crp, vasc_count)
if baseline_risk:
    st.success(f"Baseline 10-Year Risk: {baseline_risk}%")
else:
    st.warning("Please complete all patient data to calculate risk.")
