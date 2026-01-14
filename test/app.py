import streamlit as st
import os
import base64

# Use relative path for stlite compatibility
BASE_PATH = "output_pdfs" 

st.title("📊 Tandem Model Explorer (Serverless)")

# ... (rest of your slider logic remains the same) ...

filename = f"a{a:.2f}_d{d:.2f}_l{l:.2f}_m{m:.2f}_g{g:.2f}.pdf"
full_path = os.path.join(BASE_PATH, filename)

if os.path.exists(full_path):
    with open(full_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)
else:
    st.warning(f"File {filename} not found in the bundle.")