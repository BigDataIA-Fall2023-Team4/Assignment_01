import streamlit as st
from PIL import Image


def diagram():
    image = Image.open('pdf_parser/pages/architecture.png')
    st.image(image, caption='Architecture Diagram')