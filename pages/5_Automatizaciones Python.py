import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


st.title("Automatizaciones Dpto. Financiero/contable")
#st.sidebar.success("Select a page above")


with st.container():
    #st.subheader("¡Hola! Bienvenido a mi portfolio de analista de datos :wave:")
    #st.header("Sobre mí...")
    st.write("""💼 Gracias a trabajar en diferentes empresas en el departamento financiero/contable, me he dado cuenta de que muchas tareas que se realizan de manera manual se pueden automatizar y no se hacen por mero desconocimiento.
Este es el principal motivo por el cual empecé a programar con Python.

💡 Gracias a conocer el gran potencial de Python en el mundo de los datos y mi conocimiento en ello, siempre intento cambiar este tipo de procesos manuales automátizandolos.

📊 Por ejemplo, en el CRM (web) de mi última empresa, se introducían manualmente todos los datos en las fichas de proveedores/clientes, productos, y demás información relevante. Del mismo modo, al momento de generar informes a partir de la base de datos del CRM, todas estas tareas eran realizadas de manera manual.

🕒 Todas estas tareas son perfectamente automatizables, lo que permitiría ahorrar una cantidad considerable de tiempo, especialmente dado que se llevan a cabo de manera rutinaria, ya sea a diario o mensualmente.


""")
   
with st.container():
    st.write("---")
    st.header(":blue[**Automatización 1**]", divider='rainbow')
    st.subheader("**1. Informe de productos mensual**")
    st.write(
            """
            En esta empresa, además de la producción dental, también comercializa sus propios productos. Estos productos tienen varios años en el mercado, e incluso algunos son novedades. Por lo tanto, es esencial monitorear sus ventas entre los diversos laboratorios.

Por este motivo, era imperativo generar un informe el primer día de cada mes que incluyera un listado de todos los laboratorios junto con sus ventas.

Además, estas ventas están relacionadas con acuerdos previos con los expropietarios de los laboratorios adquiridos por el grupo. Por lo tanto, era fundamental disponer de esta información a principios de cada mes.

"""

    
        )
    st.subheader("1.1 ¿Cómo se hacia este informe manualmente?")
    st.write("""Un ejemplo ilustrativo de la complejidad es la venta de productos, que no solo se destina a clientes finales, sino también a otros laboratorios dentro del grupo. Para evitar duplicación de ventas, se debe restar estos importes. Además de esta particularidad, existen numerosos casos que requieren una transformación de los datos, lo que impide que el informe se genere directamente desde el CRM.
""")
    st.subheader("1.2 ¿Cómo automatizar este proceso?")
    st.write("Para que el script funcione y genere las ventas mensuales por laboratorio, solo es necesario proporcionar las fechas de inicio y final para extraer la información del CRM. El script se encargará de procesar los datos y calcular las ventas de manera automática, lo que simplificará en gran medida la generación de informes.")
    st.write("")
    st.subheader("1.3 Librerías utilizadas")

    st.write("""Para poder automatizar este informe, he utilizado las siguientes librerías:

> **Selenium**: Para automatizar las acciones en la parte web. Esta librería simula el uso del ratón y el teclado en el navegador.
Abre Chrome e inserta la URL del CRM.
Se dirige a la pestaña que le indico
Introduce la fecha inicial y final para generar un Excel con la información para poder generar el informe final.
Finalmente, descargo el fichero.
             
> **Pandas**/**Numpy**: Utilizo estas librerías para trabajar con los datos descargados del CRM. Resto, agrupo por Labs. En definitiva, realizo todas las operaciones que haría de forma manual en un Excel.


A continuación, podéis ver un video donde se puede ver el proceso automatizado:
""")
    
    st.video("https://www.youtube.com/watch?v=3EREhkUDS0c")



with st.container():
    st.write("---")
    st.header(":blue[**Automatización 2**]", divider='rainbow')
    st.subheader("**Carga masiva de facturas de venta SAP**")
    st.write(
            """
            Dado mi rol en el departamento financiero, tuve la oportunidad de identificar procesos que podían ser automatizados mediante Python y sus librerías. Uno de estos procesos críticos era la automatización de la carga masiva de facturas en SAP Business One. Esta tarea requería la preparación de un archivo Excel siguiendo un formato específico, en el cual era necesario detallar línea por línea cada factura que debía ser contabilizada.

Cada vez que el equipo contable quería llevar a cabo una carga masiva de facturas en SAP, se veían en la necesidad de extraer la información de las facturas desde el sistema CRM de la empresa y luego trabajar con los datos obtenidos en Excel. Debían adaptar meticulosamente estos datos al formato exigido por SAP para, finalmente, cargarlos en el sistema.

Fue entonces cuandos surgió la idea de desarrollar un programa que funcionara como un conversor. La esencia de este programa residía en su capacidad para cargar automáticamente el archivo proveniente del CRM y, al hacer clic en "convertir", generar un archivo Excel preparado para su carga en SAP.


"""

    
        )
    st.subheader('Librerías utilizadas')
    st.write("""

En el proceso de automatizar la carga de facturas en SAP Business One, he usado las siguientes librerías:

> **Pandas/Numpy**: . Estas bibliotecas permitieron leer los excels extráidos desde el CRM, la manipulación de los datos de manera eficiente y la transformación de los mismos hasta lograr el formato requerido por SAP.

> **Tkinter**: Para facilitar el trabajo del equipo contable, creé una interfaz gráfica de usuario (GUI) utilizando Tkinter. Esta interfaz incluía varios botones que simplificaban la carga del archivo y su conversión al formato adecuado.

> **OpenpyXL**: Una vez obtuve la información deseada, empleé la librería OpenpyXL para dar formato al archivo Excel resultante. Esto incluyó la creación de una tabla, el agrupamiento de celdas y otros ajustes necesarios para asegurarme de que los datos estuvieran listos para ser cargados en SAP.

> **Auto-py-to-exe**: Para hacer que el programa fuera aún más accesible, utilicé Auto-py-to-exe, una herramienta que permitió compilar el código en un ejecutable (.exe). Esto simplificó el proceso de ejecución del programa sin la necesidad de instalar Python o las bibliotecas correspondientes en las computadoras de los contables.

 Mediante este programa se logró simplificar significativamente el proceso de carga de facturas en SAP Business One, mejorando la eficiencia y la precisión del equipo contable.             
             """)
    
    st.write("""A continuación, mostraré diversas imágenes que representan el proceso, incluyendo el archivo Excel original extraído del CRM, el resultado final destinado a la carga en SAP y el programa que diseñé para realizar la conversión.
""")
    st.write("")
    st.markdown('\n*Excel "en bruto/sin transformar". Extraído desde el CRM.*\n') #añadir subrayado
    
    image =Image.open('image_01.jpg')
    st.image(image)
    st.write("")
    st.markdown('*Excel con formato SAP*') 
    
    image2=Image.open("image_02.jpg")
    st.image(image2)

    st.write("")
    st.markdown('*Video: Funcionamiento del programa*')
    st.video("https://www.youtube.com/watch?v=UUBhiQdTuu0")

    st.write("")
    st.write("")
    st.write("""
Como se ha podido observar en el video, el programa transforma el formato de manera automática para que se ajuste a los requisitos de SAP. El usuario solo tendrá que cargar el archivo Excel procedente del CRM, seleccionar la sociedad en la que desea llevar a cabo la contabilización y, finalmente, hacer clic en el botón de conversión. La elección de la sociedad es de vital importancia, ya que en algunas sociedades requieren la contabilización de centros de coste. De esta manera, cuando sea necesario, se especificará el centro de coste en el archivo final.""")


with st.container():
    st.write("---")
    st.header(":blue[**Automatización 3**]", divider='rainbow')
    st.subheader("**Proceso automático de introducción de datos en el CRM**")
    st.write(
            """
            Como mencioné al principio del artículo, la introducción manual de datos en el CRM era la norma.
Sin embargo, es factible automatizar este proceso utilizando Python. Podemos crear un script que, a partir de un archivo .CSV o Excel, complete los campos en una página web.
Por ejemplo, consideremos el escenario clásico de registrar el número de proveedor/cliente en SAP. En el CRM de la empresa, existe un campo para introducir el número de interlocutor SAP.
En SAP, es posible obtener un listado con el CIF y el número de interlocutor.
El script accederá a la ficha del interlocutor a través del CIF y completará el número de interlocutor.
En resumen, el script leerá línea por línea (mediante un bucle) el archivo y llenará los números de interlocutor que se indican. Este enfoque puede ser aplicado a otros casos similares.
Es importante destacar que esta automatización puede ahorrar tiempo y reducir errores al introducir datos en el CRM de la empresa.

"""  
        )
    
    st.write("")
    st.markdown('\n*Ejemplo: Carga datos al CRM (web) a través de un .csv*') 
    
    code= """# Corus
        import csv
        import time
        from selenium import webdriver

        # read CSV
        with open ('corus_test.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            web = webdriver.Chrome(r'C:\chromedriver_win32\chromedriver.exe')
            web.get('https://www.coruslink.com/mylab/clinics/7355/edit#contact')
            time.sleep(1)

            #Identificación
            email_ident = 'adrian.sanchez@xxxxxx.com'
            email = web.find_element_by_xpath('//*[@id="user_email"]')
            email.send_keys(email_ident)
            password_ident= 'XXXXXXX'
            password = web.find_element_by_xpath('//*[@id="user_password"]')
            password.send_keys(password_ident)
            Submit_ident = web.find_element_by_xpath('//*[@id="new_user"]/div[4]/input')
            Submit_ident.click()
            time.sleep(1)
            
            # Pestaña: Contact data
            click_contact_data = web.find_element_by_xpath('/html/body/div/main/div[2]/div[2]/div[2]/div/form/ul/li[2]/a')
            click_contact_data.click()

            
            
            Mobile = web.find_element_by_xpath('//*[@id="clinic_mobile_phone"]') # añadir xpath de supercliente
            Mobile.send_keys(line[0])
            Submit = web.find_element_by_xpath('//*[@id="edit_clinic_7355"]/div[2]/input')
            Submit.click()
            web.close()
            ) """
    st.code(code)


    
    st.write("""En el proceso descrito, se lleva a cabo la automatización de la carga de datos en el CRM a través de un archivo CSV. Aquí se presenta una breve descripción:

1. Se lee el archivo CSV que contiene los datos a cargar en el CRM.
2. Utilizando la biblioteca Selenium, se realiza la automatización del navegador web:
    - Se inicia sesión en la página web con las credenciales proporcionadas.
    - Se navega hasta la sección específica donde se desean introducir los datos, en este caso, los números de teléfono de diferentes proveedores.
3. Se coloca todo en un bucle para que el proceso se repita línea por línea del archivo CSV, insertando los datos en el campo especificado en la página web.
4. Hay que mencionar la necesidad de usar la función .sleep para pausar la ejecución del código durante unos segundos, lo que permite que los elementos en la página web se carguen correctamente y que el código continúe funcionando de manera efectiva.
Es importante ajustar los tiempos de pausa (sleep) de acuerdo a la velocidad de carga de la página y la interacción con los elementos web para asegurar un funcionamiento adecuado.""")