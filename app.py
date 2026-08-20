import streamlit as st
from PIL import Image

st.title("HOLA! mi nombre es Maleja")

image = Image.open ('cat.jpg')
st.image(image, caption='Interfaces multimodales y un gatito')

texto=st.text_input('buenas buenas','awawawawawa')
st.write('el texto escrito es ', texto)
