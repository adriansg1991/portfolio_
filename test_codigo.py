"""
with st.container():
    st.subheader("¡Hola! Bienvenido a mi portfolio de analista de datos :wave:")
    st.header("Sobre mí...")
    left_column2, right_column2 = st.columns(2)
    with left_column2:
         st_lottie(lottie_coding2, height = 300, key= "coding2")
    with right_column2:
        st.write(r"¡Hola! 👋 Soy Adrián, un apasionado de los datos en plena transición de una carrera en finanzas y contabilidad hacia el emocionante mundo de la analítica de datos. 📊💼 Mi viaje en el mundo de los números me ha brindado una sólida base en el análisis financiero, pero mi verdadera pasión siempre ha sido desentrañar historias ocultas en los datos y transformarlos en información valiosa. 💡En mi porfolio de proyectos de análisis de datos en Streamlit, te invito a explorar el fruto de mi entusiasmo y dedicación por este campo en constante evolución. 🚀 Desde visualizaciones interactivas que hacen que los datos cobren vida hasta aplicaciones que simplifican el proceso de toma de decisiones, estoy emocionado de compartir mi viaje de aprendizaje y descubrimiento contigo. 📈🤓¡Acompáñame en este emocionante viaje de transformación de números en conocimiento y descubre cómo mi pasión por los datos puede aportar valor a tu próximo proyecto! 🔍📊",justify='center')
        st.write("[Más información >](https://youtube.com)") # aquí redireccionar a mi CV.
 """


# Función para traducir texto a inglés
def traducir_a_ingles(texto):
    translator = Translator()
    traduccion = translator.translate(texto, src='es', dest='en')
    return traduccion.text

 # Define el contenido de tu aplicación en español
contenido_espanol = {
    "titulo": "Adrián Sánchez García",
    "parrafo_1": "Experiencia en Educación, Investigación y Administración con casi veinte años de experiencia en un entorno orientado a los datos y una pasión por proporcionar ideas basadas en modelado predictivo.",
    # Agrega aquí el resto del contenido en español...
}

# Traduce el contenido a inglés
contenido_ingles = {clave: traducir_a_ingles(valor) for clave, valor in contenido_espanol.items()}

# Título de la aplicación
st.title(contenido_espanol["titulo"])

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Resumen', unsafe_allow_html=True)
st.info(contenido_ingles["parrafo_1"])
# Agrega aquí el resto del contenido en inglés...

# Botón para activar la traducción
if st.button("Traducir a Inglés"):
    # Cambia el contenido de la aplicación a inglés
    st.title(contenido_ingles["titulo"])
    st.info(contenido_ingles["parrafo_1"])
    # Agrega aquí el resto del contenido en inglés...





