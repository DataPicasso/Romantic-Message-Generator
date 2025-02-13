import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_generator():
    return pipeline('text-generation', model='PahaII/ZeroGen-flickr10k-romantic')

ACCESS_CODE = "1234"

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
        delimiter = "\n### Mensaje Final:"
        prompt = (
            "Genera UNICAMENTE un mensaje de amor para mi pareja, "
            "con máximo 10 palabras, sin ningún encabezado, instrucción o comentario. "
            "Inspírate en estas ideas (sin repetirlas literalmente): " + ideas_str +
            "." + delimiter
        )
        
        try:
            with st.spinner("Generando mensaje..."):
                generator = load_generator()
                result = generator(
                    prompt,
                    max_length=100,
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
            # Limitar la salida a 10 palabras
            final_message = " ".join(final_message.split()[:10])
            st.markdown("### Mensaje:")
            st.write(final_message)
        except Exception as e:
            st.error(f"Error al generar el mensaje: {e}")
else:
    if user_code:
        st.error("Código de acceso incorrecto.")
