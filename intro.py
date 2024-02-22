import streamlit as st 
from PIL import Image

st.title(" Bienvenido moooorchi")
         
st.header("En este espacio vamos a crear solo cosas lindas")
st.write("Estas preparado para soñar?")
image=Image.open("morchis1.jpeg")

st.image(image, caption="Interfaces Multimodales")

