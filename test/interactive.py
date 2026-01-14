import streamlit as st
import os

# --- CONFIGURATION ---
# Replace 'nobuaki-mzmt' and 'testapp_share' if you ever change your repo name
GITHUB_USER = "nobuaki-mzmt"
REPO_NAME = "testapp_share"
FOLDER = "test"

st.set_page_config(layout="wide", page_title="Tandem Model Sensitivity Explorer")

st.title("Parameter Trend Explorer")

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

# Construct the URL for the raw file on GitHub
# Format: https://raw.githubusercontent.com/USER/REPO/main/FOLDER/FILE
raw_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/{FOLDER}/{filename}"

# --- DISPLAY ---
st.subheader(f"Current Selection: `{filename}`")

# Create two columns: one for a direct link and one for the viewer
col1, col2 = st.columns([1, 4])

with col1:
    st.write("If the viewer doesn't load:")
    st.markdown(f"[🔗 Open PDF in New Tab]({raw_url})")
    st.info("Note: Chrome/Edge may block embedded PDFs. If it's blank, try Firefox or click the link above.")

with col2:
    # Use an iframe to point to the raw GitHub URL
    # We use a Google Drive PDF viewer wrapper which is much more compatible with browsers
    pdf_viewer_url = f"https://docs.google.com/viewer?url={raw_url}&embedded=true"
    
    st.markdown(
        f'<iframe src="{pdf_viewer_url}" width="100%" height="800px" style="border: none;"></iframe>',
        unsafe_allow_html=True
    )