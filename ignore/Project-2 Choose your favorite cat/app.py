import numpy as np
import requests
import streamlit as st

ENDPOINT = "https://cataas.com/cat"

with st.sidebar:
    st.header("Configuration")
    with st.form(key="grid_reset"):
        n_photos = st.slider("Number of cat photos:", 4, 128, 16)
        n_cols = st.number_input("Number of columns", 2, 8, 4)
        st.form_submit_button(label="Reset images and layout")
    with st.beta_expander("About this app"):
        st.markdown("It's about cats :cat:!")
    st.caption("Source: https://cataas.com/#/")

st.title("Choose your favorite cat :cat:")
st.caption(
    "You can display the image in full size by hovering it and clicking the double arrow"
)

cat_images = [
    requests.get(f"{ENDPOINT}?width=1200&height=1200").content for i in range(n_photos)
]
n_rows = 1 + len(cat_images) // int(n_cols)
rows = [st.beta_container for _ in range(n_rows)]
cols_per_row = [st.beta_columns(n_cols) for _ in range(len(rows))]
cols = [column for row in cols_per_row for column in row]

for image_index, cat_image in enumerate(cat_images):
    cols[image_index].image(cat_image)