import streamlit as st
from PIL import Image


def diagram():
    image = Image.open("profile_validate/pages/architecture_diagram_part2.png")
    st.image(image, caption="Architecture Diagram", width=700)
