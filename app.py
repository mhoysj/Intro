import streamlit as st
from PIL import Image
image = Image.open('Taylor.png')


st.image(image, caption='Taylor Swift')

st.title("Amo a Taylor Swift")
st.header("Top 10 personas obsesionadas con Taylor Swift")
st.write("1. Yo, Manuela Hoyos Jimènez.")
texto= st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es' , texto)

st.subheader('Ahora usemos 2 columnas')
col1, col2 = st.columns(2)

with col1:
  st.subheader('esta es la primera columna') 
st.write('El mejor album de Taylor swift es Evermore')
resp = st.checkbox('Estoy de acuerdo')
if resp: 
  st.write('Correcto!')

with col2:
  st.subheader('Esta es la segunda columna')
  modo=st.radio('Que modalidad es la principal de tu interfaz', ('visual', 'auditiva', 'táctil'))
  if modo == 'visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'auditiva':
    st.write('la audición es fundamental para tu interfaz')
  if modo == 'táctil': 
    st.write('el tacto es fundamental para tu interfaz') 

st. subheader('uso de botones')
if st.button('Presiona el botón'): 
  st.write('Gracias por presionar')
