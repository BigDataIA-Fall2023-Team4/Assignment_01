import streamlit as st
from pages.pdf_parsing import pdf_parsing
from pages.architecture import diagram

def home():
    import streamlit as st

    st.title("DAMG 7245 - Assignment 01")
    st.sidebar.success("Select from the dropdown above☝")


page_names_to_funcs = {
    "Home": home,
    "PDF Parser": pdf_parsing,
    "Architecture": diagram
}

demo_name = st.sidebar.selectbox("Choose an option", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()