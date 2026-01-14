import streamlit as st
import os
import base64

# --- CONFIGURATION ---
BASE_PATH = r"C:\Users\nobua\OneDrive - Auburn University\paper_and_projects\tandem\tandem_model\output\test"

st.set_page_config(layout="wide", page_title="Tandem Model Sensitivity Explorer")

st.title("📊 Parameter Trend Explorer")

# Helper function to display PDF
def display_pdf(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.error(f"File not found: {os.path.basename(file_path)}")

# --- SIDEBAR SLIDERS ---
st.sidebar.header("Model Parameters")
options = [0.10, 0.30, 0.50, 0.70, 0.90]

a = st.sidebar.select_slider("Parameter **a**", options=options, value=0.10)
d = st.sidebar.select_slider("Parameter **d**", options=options, value=0.10)
l = st.sidebar.select_slider("Parameter **l**", options=options, value=0.10)
m = st.sidebar.select_slider("Parameter **m**", options=options, value=0.10)
g = st.sidebar.select_slider("Parameter **g**", options=options, value=0.10)

# --- FILE PATH CONSTRUCTION ---
filename = f"a{a:.2f}_d{d:.2f}_l{l:.2f}_m{m:.2f}_g{g:.2f}.pdf"
full_path = os.path.join(BASE_PATH, filename)

# --- DISPLAY ---
st.subheader(f"Current Selection: `{filename}`")
display_pdf(full_path)