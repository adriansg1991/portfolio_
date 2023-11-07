#%%writefile app.py

import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(
    page_title="Projects - A. Sánchez",
    page_icon="📊"
)

  #Función para animación
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/87acffc7-0328-40e5-a46a-97afbda66ea6/SVnIWBl5vG.json")                          
lottie_coding2 = load_lottieurl("https://lottie.host/081aae07-c20f-44e6-be71-6b0186fc349a/DrfTRExNaq.json")  


st.title("Presentación")
#st.sidebar.success("Select a page above")


with st.container():
    st.subheader("¡Hola! Bienvenido a mi portfolio de analista de datos :wave:")
    st.header("Sobre mí...")
    st.write("""¡Hola! 👋 Soy Adrián Sánchez, un apasionado de los datos en plena transición de una carrera en finanzas y contabilidad hacia el emocionante mundo de la analítica de datos.
             \n📊💼 Mi viaje en el mundo de los números me ha brindado una sólida base en el análisis financiero, pero mi verdadera pasión siempre ha sido desentrañar historias ocultas en los datos y transformarlos en información valiosa. 
             \nEn mi porfolio de proyectos de análisis de datos en Streamlit, te invito a explorar el fruto de mi entusiasmo y dedicación por este campo en constante evolución. 
             \n🚀 Desde visualizaciones interactivas que hacen que los datos cobren vida hasta aplicaciones que simplifican el proceso de toma de decisiones, estoy emocionado de compartir mi viaje de aprendizaje y descubrimiento contigo. 
             \n📈🤓¡Acompáñame en este emocionante viaje de transformación de números en conocimiento y descubre cómo mi pasión por los datos puede aportar valor a tu próximo proyecto! 🔍📊""")
    st.write("[Linkedin >](https://www.linkedin.com/in/adri%C3%A1n-s%C3%A1nchez-garc%C3%ADa-822676114/)") # aquí redireccionar a mi CV.      

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Mi objetivo")
        st.write(
            """
            He creado esta web como portfolio con el objetivo de compartir mis diferentes proyectos para mostrar mi conocimiento en python, en las librerías de análisis de datos y, por último, en streamlit. 
        """
        )
        st.write("[Medium >](https://medium.com/@adriansg1991)")
    with right_column:
        st_lottie(lottie_coding, height = 300, key= "coding")





