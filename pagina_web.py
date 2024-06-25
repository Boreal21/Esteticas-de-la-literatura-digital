# En primer lugar, debes ejecutar el siguiente comando en la terminal de tu computadora:
# python -m venv .venv
# Este comando crea un entorno virtual en la carpeta .venv de tu proyecto.

# En segundo lugar, debes instalar las librerías necesarias en tu entorno virtual con el siguiente comando:
# El siguiente código sirve para instalar Streamlit en tu computadora desde el terminal y hacer un primer programa en Streamlit.
# pip install Streamlit

# Adicional, este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# streamlit hello

# En tercer lugar, este comando sirve para ejecutar un script de Python en Streamlit.
# OJO: Debes antes tener instalado Streamlit en tu computadora y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

# Añadir un select box al sidebar para la selección de la pestaña de la página principal
pagina_principal = sidebar.selectbox("Selecciona una pestaña:", ("Sábado 22 de junio, 2024", "Álbum de chicos"))

# Lógica para mostrar contenido basado en la selección de la pestaña
if pagina_principal == "Sábado 22 de junio, 2024":
    # La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>La voz de Lara</h1>", unsafe_allow_html=True)
    # <h1 style='text-align: center;'>Aquí pon el título</h1>: Esto es una cadena de código HTML. 
    # La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
    # el atributo style se utiliza para agregar estilos CSS. 
    # En este caso, el texto está alineado al centro (text-align: center;). 
    # El texto dentro de las etiquetas <h1> ("Aquí pon el título") es el contenido del encabezado.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

    # Agregamos un subtítulo
    st.markdown("<h2 style='text-align: center;'>De alto perfil</h2>", unsafe_allow_html=True)

    # Creamos dos columnas separadas para el video y el texto
    col1, col2 = st.columns([3, 2])
    # La función st.columns crea columnas en la interfaz de usuario de Streamlit.
    # El argumento de la función es una lista de números que representan el ancho relativo de cada columna.
    # En este caso, la primera columna tiene un ancho relativo de 3 y la segunda columna tiene un ancho relativo de 0.5.
    # Esto significa que la primera columna es 6 veces más ancha que la segunda columna.
    # La suma de los números en la lista debe ser 12, que es el ancho total de la página.
    # En este caso, la primera columna ocupa 3/12 del ancho total y la segunda columna ocupa 0.5/12 del ancho total.

    # En la primera columna colocamos un texto?
    texto = """

    Miel burbujeando a punto de quermarse,
    ¿quién es Lara? sino un fuerte regusto a canela
    en rezago del manjarblanco.
    ¿Quién es Lara? Una café con leche
    que va de vaca a cabra,
    de cabra a oveja.
    Que mama ubre y no se blanquea
    ¿Dónde está la voz de Lara?
    ¿Dónde es que vibra?
    ¿Dónde se oye?
    Mi amor, Lara soy yo
    Y aquí empieza mi canto
    """
    # Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.


    # Mostramos el texto
    col1.markdown(f"<div style='text-align: centre; font-size: 15px;'>{texto}", unsafe_allow_html=True)

    # En la segunda columna colocamos un video
    col2.video("Clip_cara.mp4")

    # Agregamos un subtítulo
    st.markdown("<h2 style='text-align: justify;'>Sábado 22 de junio, 2024</h2>", unsafe_allow_html=True)

    # Agregar un video
    st.video("videopoema.mp4")

elif pagina_principal == "Álbum de chicos":

    st.markdown("<h1 style='text-align: center;'>La voz de Lara</h1>", unsafe_allow_html=True)

    # Agregamos un subtítulo
    st.markdown("<h2 style='text-align: center;'>Álbum de chicos</h2>", unsafe_allow_html=True)


    # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)

    # En la primera columna colocamos la imagen
    col1.image("foto_2.jpg", caption='Unos te eligen porque te pareces a su ex', width=300)
    col2.image("foto_!.jpg", caption='Otros te engañan, golpean e insultan porque se te ve que has sido infiel', width=300)

    col3, col4 = st.columns(2)
    col4.image("foto_3.jpg", caption='Hay quienes no ven pecado en salir con niñas, porque tú no eres su mujer', width=300)
   
    texto2 = """
    Y los que sigan ...
    """
    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 30px;'><em>{texto2}</em></div>", unsafe_allow_html=True)    



