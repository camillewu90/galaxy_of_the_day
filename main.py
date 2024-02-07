import streamlit as st
from download_image import download_info


# Download image of the day
title, image_url, explanation = download_info()
print(title)
print(image_url)
print(explanation)

# Make the website
st.header(title)
st.image(image_url)
st.write(explanation)