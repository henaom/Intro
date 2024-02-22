import streamlit as st 
from PIL import Image

st.title(" Bienvenido moooorchi")
         
st.header("En este espacio vamos a crear solo cosas lindas")
st.write("Estas preparado para soñar?")
image=Image.open("morchis1.jpeg")

st.image(image, caption="Lo que vamos a soñar")

text = st.text_input("Escribe algo, "Este es mi texto")
st.write("El texto escrito es", texto)

st.subheander("Ahora usemos 2 columbas")

col1, col2 = st.columnas(2)


