import pdftotext
import streamlit as st

from utils.text_to_json import text_to_json

def pdf_json_resume():
    st.title("Convert your PDF to JSON Resume")
    file_pdfresume = st.file_uploader("Upload a PDF Resume", type=["pdf"])
    if file_pdfresume is not None:
        try:
            with file_pdfresume:
                with st.empty():
                    with st.spinner("Converting pdf to json resume..."):
                        pdf = pdftotext.PDF(file_pdfresume)
                        resume_text = "\n\n".join(pdf)
                        json_text = text_to_json(resume_text)
                        st.write(json_text)
                        st.success("PDF to JSON conversion complete!")
        except Exception as e:
            st.error(f"Error: {e}")