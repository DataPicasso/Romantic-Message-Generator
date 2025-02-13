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

if user_code == ACCESS_CODE:
    st.success("¡Bienvenido!")
    
    # Instanciamos el pipeline de generación de texto una sola vez
    generator = pipeline('text-generation', model='datificate/gpt2-small-spanish')
    
    if st.button("Generar mensaje"):
        # Combina las expresiones en una cadena
        expresiones_str = ", ".join(EXPRESIONES)
        
        # Crea el prompt para que el modelo genere solo el mensaje final
        prompt = (
            "Genera un mensaje romántico, corto y único para expresar cuánto amo a mi pareja. "
            f"Expresiones de inspiración: {expresiones_str}. Mensaje:"
        )
        
        # Genera el mensaje con parámetros ajustables
        resultado = generator(prompt, max_length=60, do_sample=True, temperature=0.8)
        mensaje = resultado[0]['generated_text']
        
        # Extrae la parte del mensaje que sigue a "Mensaje:"
        if "Mensaje:" in mensaje:
            mensaje = mensaje.split("Mensaje:", 1)[1].strip()
        
        st.markdown("### Tu mensaje romántico:")
        st.write(mensaje)
else:
    if user_code:
        st.error("Código de acceso incorrecto.")
