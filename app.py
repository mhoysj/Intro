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
  modo=st.radio('¿Cuál álbum te gusta más?', ('evermore', 'folklore', 'TTPD'))
  if modo == 'evermore':
    st.write('Un álbum súper infravalorado')
  if modo == 'folklore':
    st.write('De sus mejores trabajos, tanto en lírica como producción')
  if modo == 'TTPD': 
    st.write('el más nuevo y más largo hasta ahora, de sus mejores trabajos') 

st. subheader('uso de botones')
if st.button('Presiona el botón'): 
  st.write('Gracias por presionar')
