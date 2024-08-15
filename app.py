import streamlit as st
from PIL import Image
image = Image.open('Taylor.png')
texto= st.text_input('Escribe algo', 'Este es mi texto')

st.image(image, caption='Taylor Swift')

st.title("Amo a Taylor Swift")
st.header("Top 10 personas obsesionadas con Taylor Swift")
st.write("1. Yo, Manuela Hoyos Jimènez.")
st.write('El texto escrito es' , texto)
