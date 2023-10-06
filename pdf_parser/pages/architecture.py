import streamlit as st
from PIL import Image


def diagram():
    image = Image.open('architecture.png')
    st.image(image, caption='Architecture Diagram')