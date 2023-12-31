import streamlit as st
from utils.pypdf_parsing import *
from utils.nougat_parsing import *
import time

def pdf_parsing():
    with st.form("login", clear_on_submit=True):
        pdf_url = st.text_input('PDF File URL', '', placeholder = 'Paste the URL here.')

        option = st.selectbox(
            'Which python library would you like to choose for pdf parsing?',
            ('PyPDF', 'Nougat'))

        api_address = st.text_input('API URL (If using Nougat)', '', placeholder = 'Connect to API for GPU computation')

        is_submit = st.form_submit_button("Submit", type="primary")
        if is_submit:
            st.write(f'You selected {pdf_url} file and {option} library for pdf parsing')
            st.divider()
            # Start time
            start_time = time.time()
            # local_filename = download_pdf_from_url(pdf_url, 'data/filefromweb.pdf')
            pdf_in_memory = fetch_pdf_from_url(pdf_url)
            if option == 'Nougat':
                pdf_content = parse_pdf_with_nougat(pdf_url, api_address)

            elif option == 'PyPDF':
                pdf_content, number_of_pages = parse_pdf_with_pypdf(pdf_in_memory)
                st.write(f"Number of pages processed: *{number_of_pages}*")
            summary = text_summarize(pdf_content)
            # End time
            end_time = time.time()
            # Calculate elapsed time in seconds
            elapsed_time = end_time - start_time
            st.write(f"Processing time: *{elapsed_time:.2f} seconds*")
            st.write("*Below is the summarized file content:*")
            st.write(summary)
            st.divider()
            st.write("*Below is the parsed file content:*")
            st.write(pdf_content)
            
                

