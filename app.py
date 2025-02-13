import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer

@st.cache_resource
def load_model():
    model_id = "Qwen/Qwen2.5-7B-Instruct"
    # Cargamos el tokenizador y modelo con trust_remote_code=True
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
    return model, tokenizer

def generate_text(prompt, max_new_tokens=250, temperature=0.7, top_p=0.95, repetition_penalty=1.2):
    model, tokenizer = load_model()
    # Codifica el prompt
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    # Genera la respuesta
    output = model.generate(
        input_ids,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=temperature,
        top_p=top_p,
        repetition_penalty=repetition_penalty
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)

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
            "Genera un mensaje de amor, romántico, personal, coherente y emotivo para expresar mi amor incondicional a mi pareja. "
            "No incluyas ninguna referencia externa. Utiliza como inspiración estas ideas sin repetirlas textualmente: " +
            ideas_str + "." + delimiter
        )
        
        try:
            with st.spinner("Generando mensaje..."):
                generated_text = generate_text(prompt)
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
