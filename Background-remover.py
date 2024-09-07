import streamlit as st
from rembg import remove
from PIL import Image
import numpy as np
import io

st.title("Simple Background remover :lower_left_paintbrush:")

if 'processed_image' not in st.session_state:
    st.session_state.processed_image = None

image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png", "webp"])

col1, col2 = st.columns(2)

if image:
    img = Image.open(image)
    col1.header("Original")
    col1.image(img)

    output = remove(img)
    img_byte_arr = io.BytesIO()
    output.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    col2.header("Background Removed")
    col2.image(output)

    st.session_state.processed_image = img_byte_arr

if st.session_state.processed_image is not None:
    st.download_button(
        label="Download Background Removed Image",
        data=st.session_state.processed_image,
        file_name="bg-removed.png",
        mime="image/png"
    )