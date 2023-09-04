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
st.sidebar.success("Select a page above")




with st.container():
    st.subheader("¡Hola! Bienvenido a mi portfolio de analista de datos :wave:")
    st.header("Sobre mí...")
    left_column2, right_column2 = st.columns(2)
    with left_column2:
         st_lottie(lottie_coding2, height = 300, key= "coding2")
    with right_column2:
        st.write(r"Mi nombre es Adrián Sánchez. Me encuentro en plena transición en el mercado laboral. Yo estudié ADE Después de años trabajando en departamentos de finanzas/contabilidad, donde aparte de tareas contables/administrativas, he creado difertes proyectos para automatizar ciertos procesos en el departamento, actualmente estoy buscando una posición 100%  como analista de datos. Este canal se centra en la creawción de tutoriales y yutoriales para programadores e ingenieros.")
        st.write("[Más información >](https://youtube.com)") # aquí redireccionar a mi CV.
       

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Mi objetivo")
        st.write(
            """
            He creado esta web como portfolio con el objetivo de compartir mis diferentes proyectos para mostrar mi conocimiento en python, en las librerías de análisis de datos y por último en streamlit. 
        """
        )
        st.write("[Linkedin >](https://www.linkedin.com/in/adri%C3%A1n-s%C3%A1nchez-garc%C3%ADa-822676114/)")
    with right_column:
        st_lottie(lottie_coding, height = 300, key= "coding")





