import streamlit as st
from PIL import Image


def diagram():
    image = Image.open('diagrams/architecture.png')
    st.image(image, caption='Architecture Diagram')