import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_generator():
    # Usamos mrm8488/spanish-gpt2, un modelo en español
    return pipeline('text-generation', model='mrm8488/spanish-gpt2')

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
        expresiones_str = ", ".join(EXPRESIONES)
        # Delimitador para separar el mensaje final del prompt
        delimiter = "\n### Mensaje Final:"
        prompt = (
            "Genera UNICAMENTE un mensaje de amor para mi pareja, sin ningún encabezado, instrucción, comentario o explicación. "
            "El mensaje debe ser personal, romántico, emotivo y coherente, expresando mi amor incondicional. "
            "No incluyas ningún otro tipo de información o referencia externa. "
            "Inspírate en estas ideas (sin repetirlas textualmente): " + expresiones_str +
            "." + delimiter
        )
        
        try:
            with st.spinner("Generando mensaje..."):
                generator = load_generator()
                result = generator(
                    prompt,
                    max_length=300,
                    do_sample=True,
                    temperature=0.7,
                    top_p=0.95,
                    repetition_penalty=1.2
                )
            generated_text = result[0]['generated_text']
            # Extrae únicamente el texto que se encuentra después del delimitador
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
