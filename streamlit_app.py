import streamlit as st
import pandas as pd
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt

# Title
st.title("Sample Decimitry demo")

# File upload
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file:
    # Read Excel file
    df = pd.read_excel(uploaded_file)
    st.write("Preview of uploaded data:", df.head())

    # Placeholder for computation
    result = df.describe()  # Example computation
    plt.figure()
    plt.plot(df['date'], df['att'])
    plt.show()

    # Display result
    #st.write("Computation result (summary statistics):", result)

    # Provide download link to existing PDF
    with open("reports/sample_report.pdf", "rb") as pdf_file:
        st.download_button(
            label="Download Report (PDF)",
            data=pdf_file,
            file_name="reports/sample_report.pdf",
            mime="application/pdf"
        )
