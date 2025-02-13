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
        
        # Nuevo prompt con instrucciones detalladas para generar un mensaje completo y coherente
        prompt = (
            "Crea un mensaje romántico, coherente y original, dirigido a mi pareja, que exprese mi amor incondicional. "
            "Utiliza como inspiración las siguientes ideas sin repetirlas literalmente: "
            f"{expresiones_str}. "
            "Escribe un mensaje completo que tenga sentido y termine de forma natural."
        )
        
        try:
            with st.spinner("Cargando modelo y generando mensaje..."):
                generator = load_generator()
                resultado = generator(
                    prompt,
                    max_length=250,  # Permite más tokens para completar la idea
                    do_sample=True,
                    temperature=0.7,  # Temperatura ligeramente baja para mayor coherencia
                    top_p=0.95        # Aumenta la diversidad sin perder cohesión
                )
            mensaje = resultado[0]['generated_text']
            st.markdown("### Mensaje:")
            st.write(mensaje)
        except Exception as e:
            st.error(f"Error al generar el mensaje: {e}")
else:
    if user_code:
        st.error("Código de acceso incorrecto.")
