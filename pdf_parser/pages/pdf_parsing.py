import streamlit as st
from utils.pypdf_parsing import *
from utils.nougat_parsing import *

def pdf_parsing():
    with st.form("login", clear_on_submit=True):
        pdf_url = st.text_input('PDF File URL', '', placeholder = 'Paste the URL here.')

        option = st.selectbox(
            'Which python library would you like to choose for pdf parsing?',
            ('PyPDF', 'Nougat'))

        api_address = st.text_input('API URL', '', placeholder = 'Connect to API for GPU computation')

        is_submit = st.form_submit_button("Submit", type="primary")
        if is_submit:
            st.write(f'You selected {pdf_url} file and {option} library for pdf parsing')

            if option == 'Nougat':
                st.write('Nougat')
                # api_address = st.text_input('API URL', '', placeholder = 'Connect to API for GPU computation')
                # is_confirm = st.form_submit_button("Confirm URL", type="secondary")
                # if is_confirm:
                local_filename = download_pdf_from_url(pdf_url, 'data/filefromweb.pdf')
                pdf_content = parse_pdf_with_nougat('data/filefromweb.pdf', api_address)

            elif option == 'PyPDF':
                local_filename = download_pdf_from_url(pdf_url, 'data/filefromweb.pdf')
                pdf_content = parse_pdf_with_pypdf(local_filename)

            st.write("*Below is the processed file content:*")
            st.divider()
            st.write(pdf_content)
                

