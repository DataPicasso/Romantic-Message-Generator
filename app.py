import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_generator():
    # Usamos la tarea text2text-generation para Qwen2.5 y se habilita trust_remote_code
    return pipeline('text2text-generation', model='Qwen/Qwen2.5-7B-Instruct', trust_remote_code=True)

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
        delimiter = "\nMensaje final:"
        prompt = (
            "Genera un mensaje de amor, romántico, personal, coherente y emotivo dirigido a mi pareja. "
            "No incluyas ninguna referencia externa. "
            "Inspírate en las siguientes ideas sin repetirlas literalmente: " 
            + ideas_str + "." + delimiter
        )
        
        try:
            with st.spinner("Generando mensaje..."):
                generator = load_generator()
                result = generator(
                    prompt,
                    max_new_tokens=250,
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
