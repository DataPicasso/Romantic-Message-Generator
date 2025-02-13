import streamlit as st
from transformers import pipeline

# Función para cargar y cachear el pipeline de generación usando un modelo afinado en mensajes de amor
@st.cache_resource
def load_generator():
    # Usa el modelo preentrenado enfocado en mensajes románticos (sustituye por el nombre real)
    return pipeline('text-generation', model='lmesquita/spanish-love-messages')

ACCESS_CODE = "1234"

# Ideas de inspiración para el mensaje (puedes ajustar estas ideas según tus necesidades)
EXPRESIONES = [
    "tu sonrisa ilumina mis días",
    "tu mirada me hace soñar",
    "cada instante a tu lado es un regalo",
    "eres mi inspiración",
    "mi corazón late por ti",
    "eres la luz de mis ojos",
    "Te amo con mi vida",
    "Te adoro",
    "Eres mi bebita",
    "Eres mi princesita"
]

user_code = st.text_input("Ingrese el código de acceso", type="password")

if user_code == ACCESS_CODE:
    st.success("¡Bienvenida princesa!")
    
    if st.button("Generar mensaje"):
        ideas_str = ", ".join(EXPRESIONES)
        # Definimos un delimitador único para separar el prompt de la salida
        delimiter = "\nMensaje final:"
        # Prompt enfocado únicamente en generar un mensaje de amor, sin información extra
        prompt = (
            "Escribe un mensaje de amor, romántico, personal, y emotivo dirigido a mi pareja. "
            "Utiliza como inspiración las siguientes ideas sin repetirlas textualmente: " + ideas_str +
            "." + delimiter
        )
        
        try:
            with st.spinner("Generando mensaje..."):
                generator = load_generator()
                result = generator(
                    prompt,
                    max_length=250,
                    do_sample=True,
                    temperature=0.7,
                    top_p=0.95,
                    repetition_penalty=1.2
                )
            generated_text = result[0]['generated_text']
            # Extrae solo la parte generada después del delimitador
            if delimiter in generated_text:
                final_message = generated_text.split(delimiter, 1)[1].strip()
            else:
                final_message = generated_text.strip()
            st.markdown("### Mensaje:")
            st.write(final_message)
        except Exception as e:
            st.error(f"Error al generar el mensaje: {e}")
else:
    if user_code:
        st.error("Código de acceso incorrecto.")
