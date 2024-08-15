import streamlit as st
from PIL import Image

image = Image.open('Taylor')
st.image(image, caption='Taylor Swift')

st.title("Amo a Taylor Swift")
st.header("Top 10 personas obesesionadas con Taylor Swift")
st.write("1. Yo, Manuela Hoyos Jimènez.")
