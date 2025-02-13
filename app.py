import streamlit as st
from transformers import pipeline

# Define el código de acceso (puedes cambiarlo según tus preferencias)
ACCESS_CODE = "1234"

# Expresiones predefinidas para inspirar el mensaje romántico
EXPRESIONES = [
    "tu sonrisa ilumina mis días",
    "tu mirada me hace soñar",
    "cada instante a tu lado es un regalo",
    "eres mi inspiración",
    "mi corazón late por ti"
]

# Solicita al usuario el código de acceso (se muestra como contraseña)
user_code = st.text_input("Ingrese el código de acceso", type="password")

# Verifica el código ingresado
if user_code == ACCESS_CODE:
    st.success("¡Bienvenido!")
    
    # Botón para generar el mensaje
    if st.button("Generar mensaje"):
        # Combina las expresiones en una sola cadena
        expresiones_str = ", ".join(EXPRESIONES)
        
        # Crea el prompt combinando las expresiones predefinidas
        prompt = (
            f"Utilizando las siguientes expresiones: {expresiones_str}\n"
            "Genera un mensaje romántico, corto y único para expresar cuánto amo a mi pareja:"
        )
        
        # Crea el pipeline de generación de texto con un modelo en español
        generator = pipeline('text-generation', model='datificate/gpt2-small-spanish')
        
        # Genera el mensaje; puedes ajustar parámetros como max_length y temperature
        resultado = generator(prompt, max_length=60, do_sample=True, temperature=0.8)
        mensaje = resultado[0]['generated_text']
        
        st.markdown("### Tu mensaje romántico:")
        st.write(mensaje)
else:
    if user_code:  # Si el usuario ya ingresó algo y es incorrecto
        st.error("Código de acceso incorrecto.")
