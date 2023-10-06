import streamlit as st
from PIL import Image


def diagram():
    image = Image.open("profile_validate/pages/part2_architecture.png")
    st.image(image, caption="Architecture Diagram", width=700)
