import streamlit as st
import requests 
from streamlit_lottie import st_lottie

#Función para animación
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding3 = load_lottieurl("https://lottie.host/7747eead-cd4a-478e-abe8-ff18afde1471/E9Pj1q0BKf.json") 

#st_lottie(lottie_coding3, height = 100, key= "coding4")

st.title("Contacto")


st_lottie(lottie_coding3, height = 100, key= "coding3")
st.write(r"Si estais interesados en mi perfil, podéis contactar conmigo en Linkedin.")
st.write("[Linkedin >](https://www.linkedin.com/in/adri%C3%A1n-s%C3%A1nchez-garc%C3%ADa-822676114/)")


"""
left_column3,center_column3,right_column3 = st.columns(3)
with left_column3:
    st_lottie(lottie_coding3, height = 100, key= "coding3")
with left_column3:
    st.write(r"Si estais interesados en mi perfil, podéis contactar conmigo en Linkedin.")
    st.write("[Linkedin >](https://www.linkedin.com/in/adri%C3%A1n-s%C3%A1nchez-garc%C3%ADa-822676114/)")

"""