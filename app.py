import base64
import os
import sys
import time
import streamlit as st
import pdfplumber
import tempfile
import openai
from dotenv import load_dotenv
import pdftotext
import re
from streamlit_chat import message
#end of libs
# files
from utils.chat_ui import render_chat_ui
from scenes.pdf_json_resume import pdf_json_resume

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


# def pdf_to_text(file_path):
#     with pdfplumber.open(file_path) as pdf:
#         text = "\n".join([page.extract_text() for page in pdf.pages])
#     return text


# sidebar
st.sidebar.title("AI Tools")
# Using object notation


# Using "with" notation
with st.sidebar:
    add_radio = st.radio("PDF tools", ("Question PDF", "PDF to Text", "PDF to JSON Resume"))
# add links to the sidebar


if add_radio == "Question PDF":
    st.title("Chat with your PDF")
    file_pdfchat = st.file_uploader("Upload a PDF file", type=["pdf"])
    if file_pdfchat is not None:
        try:
            # with file_pdfchat:
                # with st.spinner("Converting PDF to text..."):
            '''
            RENDER PDF
            '''
            # base64_pdf = base64.b64encode(file_pdfchat.read()).decode('utf-8')
            # pdf_display = ( f'<embed src="data:application/pdf;base64,{base64_pdf}" ' 'width="800" height="1000" type="application/pdf"></embed>' )
            # st.markdown(pdf_display, unsafe_allow_html=True)
            with st.spinner("Processing PDF..."):
                pdf = pdftotext.PDF(file_pdfchat)
                extracted_text = "\n\n".join(pdf)
                render_chat_ui(extracted_text)
                # st.success("PDF to Text conversion complete!")
                # st.write(extracted_text)
                st.write("Now you can chat with your PDF")
               
        except Exception as e:
            #print line number and file name
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_tb.tb_lineno, os.path.split(exc_tb.tb_frame.f_code.co_filename)[1])
            st.error(f"Error: {e}")
    
if add_radio == "PDF to JSON Resume":
    pdf_json_resume()

def pdf_to_text():
    st.title("Convert your PDF to Text")
    file_pdf = st.file_uploader("Upload a PDF File", type=["pdf"])
    if file_pdf is not None:
        try:
            with file_pdf:
                with st.spinner("Converting pdf to text..."):
                    pdf = pdftotext.PDF(file_pdf)
                    resume_text = "\n\n".join(pdf)
                    st.subheader("Resume Text")
                    st.markdown(resume_text)
                    st.success("PDF to text conversion complete!")
        except Exception as e:
            st.error(f"Error: {e}")
              
if add_radio == "PDF to Text":
    pdf_to_text()