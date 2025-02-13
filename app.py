import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_generator():
    # Usamos mrm8488/spanish-gpt2, que es un modelo público en español
    return pipeline('text-generation', model='mrm8488/spanish-gpt2')

ACCESS_CODE = "1234"

# Ideas de inspiración para el mensaje romántico
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

user_code = st.text_input("Ingrese el código de acceso", type="password")

if user_code == ACCESS_CODE:
    st.success("¡Bienvenida princesa!")
    
    if st.button("Generar mensaje"):
        ideas_str = ", ".join(EXPRESIONES)
        # Definimos un delimitador para extraer únicamente el mensaje final
        delimiter = "\nMensaje final:"
        # Prompt muy enfocado, con instrucciones explícitas para evitar cualquier referencia externa
        prompt = (
            "Escribe un mensaje de amor apasionado, personal y totalmente centrado en expresar mis sentimientos de amor y admiración hacia mi pareja. "
            "El mensaje debe estar escrito en un tono emotivo y poético, sin incluir ningún tipo de referencia a otros temas (como economía, política, tecnología, libros o noticias). "
            "Inspírate en estas ideas sin repetirlas literalmente: " + ideas_str + "."
            + delimiter
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
