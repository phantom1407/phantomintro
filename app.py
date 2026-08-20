import streamlit as st
from PIL import Image

st.title("HOLA! mi nombre es Maleja")

image = Image.open ('cat.jpg')
st.image(image, caption='Interfaces multimodales y un gatito')

texto=st.text_input('buenas buenas','awawawawawa')
st.write('el texto escrito es ', texto)

st.subheader('ahora dos columnas:')
col1, col2=st.columns(2)
with col1:
  st.write('las interfaces multimodales mejoran la exp de usuario')
  resp=st.checkbox('sisas')
  if resp:
    st.write('niceee')

with col2:
  modo=st.radio('que modalidad es la principal en esta interfaz?', ('visual', 'auditiva', 'tactil'))
  if modo== 'visual':
    st.write('la vista es fundamental en esta interfaz')
  if modo== 'auditiva':
    st.write('la audición no es fundamental en esta interfaz')
  if modo== 'tactil':
    st.write('el sentir no es fundamental en esta interfaz')

st.subheader('esto es un botón, presionalo')
if st.button('presioname :)'):
  st.write("gracias por presionar jiji')
           else:
  st.write('no has presionado aún')
