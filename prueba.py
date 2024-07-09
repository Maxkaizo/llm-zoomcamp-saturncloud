import streamlit as st
import time

# Definir la función que se ejecutará al hacer clic en el botón
def rag_function(input_text):
    # Simular un proceso que toma tiempo
    time.sleep(5)
    return f"Resultado para la entrada: {input_text}"

# Título de la aplicación
st.title("Aplicación Streamlit con Input Box y Botón")

# Cuadro de entrada para el texto
input_text = st.text_input("Ingrese un texto:")

# Botón para ejecutar la función
if st.button("Ask"):
    with st.spinner('Ejecutando función, por favor espere...'):
        result = rag_function(input_text)
        st.success("Función ejecutada exitosamente!")
        st.write(result)
