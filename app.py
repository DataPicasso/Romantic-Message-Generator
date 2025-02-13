import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

@st.cache_resource
def load_generator():
    model_name = "DeepESP/gpt2-spanish"  # Modelo de generación en español
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return pipeline('text-generation', model=model, tokenizer=tokenizer)

ACCESS_CODE = "1234"

EXPRESIONES = [
    "tu sonrisa ilumina mi mundo",
    "tu mirada despierta mi alma",
    "contigo el tiempo se detiene",
    "eres mi paz y mi aventura",
    "tu amor es mi fortaleza",
    "en tus brazos encuentro hogar",
    "cada latido te pertenece",
    "nuestro amor es mi poema",
    "eres mi sueño hecho realidad",
    "juntos escribimos nuestra eternidad"
]

user_code = st.text_input("Ingrese el código de acceso", type="password")

if user_code == ACCESS_CODE:
    st.success("¡Bienvenida al corazón digital!")
    
    if st.button("Generar declaración de amor"):
        prompt = f"Escribe un mensaje romántico en español de máximo 10 palabras usando: {', '.join(EXPRESIONES)}. Mensaje:"
        
        try:
            with st.spinner("Creando magia amorosa..."):
                generator = load_generator()
                result = generator(
                    prompt,
                    max_new_tokens=25,
                    do_sample=True,
                    temperature=0.85,
                    top_k=45,
                    top_p=0.92,
                    repetition_penalty=1.25,
                    num_return_sequences=1
                )
            
            raw_text = result[0]['generated_text']
            # Extraer solo el mensaje nuevo
            final_message = raw_text.split("Mensaje:")[-1].strip()
            # Limpieza y formateo
            final_message = final_message.split(".")[0].split("!")[0]
            final_message = " ".join(final_message.split()[:10]).capitalize()
            
            st.markdown("### 💝 Tu Mensaje Especial")
            st.success(f"\"{final_message}\"")
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
else:
    if user_code:
        st.error("Código incorrecto, el secreto es 1234")
