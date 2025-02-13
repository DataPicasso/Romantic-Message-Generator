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
        # Prompt simplificado y enfocado en la tarea
        prompt = (
            "Escribe un mensaje romántico, coherente, original y completo para expresar todo mi amor incondicional a mi pareja. "
            "Utiliza como inspiración, sin repetirlas literalmente, las siguientes ideas: " + expresiones_str +
            ". El mensaje debe terminar de forma natural."
        )
        
        try:
            with st.spinner("Cargando modelo y generando mensaje..."):
                generator = load_generator()
                resultado = generator(
                    prompt,
                    max_length=250,
                    do_sample=True,
                    temperature=0.7,
                    top_p=0.95,
                    repetition_penalty=1.2
                )
            mensaje = resultado[0]['generated_text']
            
            st.markdown("### Mensaje:")
            st.write(mensaje)
        except Exception as e:
            st.error(f"Error al generar el mensaje: {e}")
else:
    if user_code:
        st.error("Código de acceso incorrecto.")
