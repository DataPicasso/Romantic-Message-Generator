import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_generator():
    return pipeline('text-generation', model='datificate/gpt2-small-spanish')

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
        # Delimitador para separar prompt de salida
        delimiter = "\nMensaje final:"
        # Prompt enfocado: NO incluir referencias a libros, textos, noticias u otros contenidos literarios
        prompt = (
            "Escribe un mensaje romántico, personal, coherente y original para expresar todo mi amor incondicional a mi pareja. "
            "No incluyas ninguna referencia a libros, textos, noticias u otra información externa. "
            "Inspírate en las siguientes ideas sin repetirlas literalmente: " + expresiones_str +
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
            # Extrae solo el mensaje generado después del delimitador
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
