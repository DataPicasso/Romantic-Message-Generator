import streamlit as st
from transformers import pipeline

# Función para cargar y cachear el pipeline de generación
@st.cache_resource
def load_generator():
    return pipeline('text-generation', model='datificate/gpt2-small-spanish')

# Define el código de acceso
ACCESS_CODE = "1234"

# Expresiones predefinidas para inspirar el mensaje romántico
EXPRESIONES = [
    "tu sonrisa ilumina mis días",
    "tu mirada me hace soñar",
    "cada instante a tu lado es un regalo",
    "eres mi inspiración",
    "mi corazón late por ti",
    "eres la luz de mis ojos",
    "Te amo con mi vida",
    "Te adoro",
    "Te amodoro, en un inodoro",
    "Eres mi bebita",
    "Eres mi princesita"
]

# Solicita al usuario el código de acceso (tipo password)
user_code = st.text_input("Ingrese el código de acceso", type="password")

if user_code == ACCESS_CODE:
    st.success("¡Bienvenida princesa!")
    
    if st.button("Generar mensaje"):
        # Combina las expresiones en una cadena
        expresiones_str = ", ".join(EXPRESIONES)
        
        # Crea el prompt para que el modelo genere solo el mensaje final
        prompt = (
            "Genera un mensaje romántico, corto y único para expresar cuánto amo a mi pareja. "
            f"Expresiones de inspiración: {expresiones_str}. Mensaje:"
        )
        
        try:
            with st.spinner("Cargando modelo y generando mensaje..."):
                generator = load_generator()
                resultado = generator(
                    prompt,
                    max_length=100,  # Incrementa la longitud máxima permitida
                    do_sample=True,
                    temperature=0.8,
                    top_p=0.9  # Opcional, para controlar la diversidad
                )
            mensaje = resultado[0]['generated_text']
            
            # Extrae solo la parte del mensaje que sigue a "Mensaje:"
            if "Mensaje:" in mensaje:
                mensaje = mensaje.split("Mensaje:", 1)[1].strip()
            
            st.markdown("### Mensaje:")
            st.write(mensaje)
        except Exception as e:
            st.error(f"Error al generar el mensaje: {e}")
else:
    if user_code:
        st.error("Código de acceso incorrecto.")
