import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

@st.cache_resource
def load_generator():
    model_name = "IIC/bert-base-spanish-wwm-cased-finetuned-romantic"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return pipeline('text-generation', model=model, tokenizer=tokenizer)

ACCESS_CODE = "1234"

EXPRESIONES = [
    "tu sonrisa ilumina mis días",
    "tu mirada me hace soñar",
    "cada instante contigo es un regalo",
    "eres mi inspiración constante",
    "mi corazón late al ritmo de tu voz",
    "en tus ojos encuentro mi hogar",
    "tu amor es mi mayor fortaleza",
    "contigo el tiempo pierde sentido",
    "eres la melodía de mi alma",
    "tus abrazos son mi refugio"
]

user_code = st.text_input("Ingrese el código de acceso", type="password")

if user_code == ACCESS_CODE:
    st.success("¡Bienvenida mi amor!")
    
    if st.button("Generar mensaje especial"):
        prompt = f"Escribe un mensaje romántico coherente de 10 palabras máximo usando estos conceptos: {', '.join(EXPRESIONES)}. El mensaje debe ser:"
        
        try:
            with st.spinner("Creando algo único para ti..."):
                generator = load_generator()
                result = generator(
                    prompt,
                    max_length=30,
                    do_sample=True,
                    temperature=0.5,  # Reducido para más coherencia
                    top_p=0.9,
                    repetition_penalty=1.3,
                    num_return_sequences=1,
                    pad_token_id=generator.tokenizer.eos_token_id
                )
            
            full_text = result[0]['generated_text']
            # Extraer solo la parte nueva del mensaje
            final_message = full_text.split(prompt)[-1].strip()
            
            # Limpieza y formateo
            final_message = final_message.split(".")[0].replace('"', '').replace("'", '')
            words = final_message.split()[:10]
            final_message = ' '.join(words).capitalize()
            
            st.markdown("### 💌 Mensaje especial:")
            st.success(f"✨ {final_message} ✨")
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
else:
    if user_code:
        st.error("Código incorrecto, prueba con '1234'")
