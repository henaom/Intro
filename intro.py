import streamlit as st 
from PIL import Image

st.title(" Bienvenido moooorchi")
         
st.header("En este espacio vamos a crear solo cosas lindas")
st.write("Estas preparado para soñar?")
image=Image.open("morchis1.jpeg")

st.image(image, caption="Lo que vamos a soñar")

text = st.text_input("Escribe algo", "Este es mi texto")
st.write("El texto escrito es", text)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
         st.subheader("Esta es la primera columna")
         st.write("Las interfaces multimodales mejoran la experiencia de usuario")
         resp = st.checkbox ("Estoy de acuerdo")
         if resp:
                  st.write("Correcto !")
                  
with col2:
         st.subheader("Esta es la segunda columna")
         modo = st.radio("Que Modalidad es la principal en tu interfaz", ("Visual", "Auditiva", "Tácti"))
         if modo == "Visual":
                  st.write("La vista es fundamental para tu interfaz")
         if modo == "Auditiva":
                  st.write("La audicion es fundamental para tu interfaz")
         if modo == "Tácti" :
                  st.write("El tacto es fundamental para tu inferfaz")
                  
                  
         
                         

