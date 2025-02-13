import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

@st.cache_resource
def load_generator():
    model_name = "DeepESP/gpt2-spanish"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return pipeline('text-generation', model=model, tokenizer=tokenizer)

ACCESS_CODE = "1234"

EXPRESIONES = [
    "tu sonrisa ilumina mis días",
    "tu mirada me hace soñar",
    "cada instante a tu lado es un regalo",
    "eres mi inspiración",
    "mi corazón late por ti",
    "eres la luz de mis ojos",
    "te amo con toda mi alma",
    "eres mi razón de ser",
    "contigo el tiempo se detiene",
    "tu amor es mi fortaleza"
]

user_code = st.text_input("Ingrese el código de acceso", type="password")

if user_code == ACCESS_CODE:
    st.success("¡Bienvenida princesa!")
    
    if st.button("Generar mensaje"):
        prompt = (
            "Escribe un mensaje romántico y emotivo de máximo 10 palabras usando estas ideas: " 
            + ", ".join(EXPRESIONES) + ". Mensaje:"
        )
        
        try:
            with st.spinner("Generando mensaje..."):
                generator = load_generator()
                result = generator(
                    prompt,
                    max_new_tokens=30,
                    do_sample=True,
                    temperature=0.9,
                    top_k=50,
                    top_p=0.95,
                    repetition_penalty=1.5,
                    num_return_sequences=1
                )
            generated_text = result[0]['generated_text']
            # Extract only the new generated part
            final_message = generated_text.replace(prompt, "").strip().split(".")[0]
            # Ensure max 10 words
            final_message = " ".join(final_message.split()[:10])
            st.markdown("### Tu mensaje especial:")
            st.success(f"💖 {final_message} 💖")
        except Exception as e:
            st.error(f"Error al generar el mensaje: {e}")
else:
    if user_code:
        st.error("Código de acceso incorrecto.")
