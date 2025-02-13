import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Generador de Amor", page_icon="💖")
ACCESS_CODE = "1234"

# CSS centralizado para la app
st.markdown("""
<style>
.stApp {
    background-color: #FFFFFF !important;
}
p, h1, h2, h3, h4, h5, h6 {
    color: #333333 !important;
}
.footer {
    text-align: center;
    padding: 15px;
    color: #E91E63;
    font-family: cursive;
}
</style>
""", unsafe_allow_html=True)

PLANTILLAS = [
    # Plantillas originales mejoradas
    "Para mi {term}: {message}",
    "{term}, {message}",
    "¡{term}! {message}",
    "Mi amada {term}, {message}",
    "Querida {term}: {message}",
    "En este día, {term}, {message}",
    "Desde que te conocí, {term}, {message}",
    "Cada mañana al despertar, {term}, {message}",
    "{message}, mi preciosa {term}",
    "{message}, porque eres mi {term}",
    "En el susurro del viento, {term}, {message}",
    "{term}, mi amor eterno: {message}",
    "Bajo las estrellas, {term}, {message}",
    "En cada latido, {term}, {message}",
    "{message}... eso eres tú, {term}",
    "¿Sabías, {term}, que {message}?",
    "En mi mente y corazón, {term}, {message}",
    "Juro por ti, {term}, que {message}",
    "Hoy quiero decirte, {term}: {message}",
    "Entre millones, {term}, {message}",
    "En cada amanecer, {term}, {message}",
    "Prometo solemnemente, {term}, {message}",
    "En la quietud de la noche, {term}, {message}",
    "Eres, {term}, {message}",
    "Nunca olvides, {term}, que {message}",
    "A través del tiempo, {term}, {message}",
    "En cada respiro, {term}, {message}",
    "Te confieso, {term}: {message}",
    "En tu mirada encuentro, {term}, {message}",
    "Desde lo más profundo, {term}, {message}",
    "En cada paso, {term}, {message}",
    "Hoy y siempre, {term}, {message}",
    "Con toda mi alma, {term}, {message}",
    "En nuestro universo, {term}, {message}",
    "Bajo la lluvia y el sol, {term}, {message}",
    "En cada estación, {term}, {message}",
    "Aunque el mundo gire, {term}, {message}",
    "En cada suspiro, {term}, {message}",
    "En tus manos, {term}, {message}",
    "Más allá de todo, {term}, {message}",
    "En cada desafío, {term}, {message}",
    "A tu lado, {term}, {message}",
    "En cada risa, {term}, {message}",
    "En la melodía de tu voz, {term}, {message}",
    "A través de las distancias, {term}, {message}",
    "En cada logro, {term}, {message}",
    "En la dulzura de tu ser, {term}, {message}",
    "Ante el universo, {term}, {message}",
    "En cada meta alcanzada, {term}, {message}",
    "En la calma y la tormenta, {term}, {message}",
    "En cada palabra tuya, {term}, {message}",
    "En el eco de tu risa, {term}, {message}",
    "En cada aventura, {term}, {message}",
    "En la magia de nuestro amor, {term}, {message}",
    "En cada secreto compartido, {term}, {message}",
    "En la complicidad de nuestras miradas, {term}, {message}",
    "En cada promesa cumplida, {term}, {message}",
    "En la ternura de tus gestos, {term}, {message}",
    "En cada desafío superado, {term}, {message}",
    "En la sinfonía de nuestro amor, {term}, {message}"
]

MENSAJES_BASE = [
    # Mensajes originales
    "cada momento a tu lado es un regalo",
    "mi mundo brilla con tu presencia",
    "eres la razón de mi felicidad",
    "tu amor ilumina mi camino",
    "nada se compara a tu sonrisa",
    "tu esencia transforma mi realidad",
    "en tus abrazos encuentro mi hogar",
    "tu fuerza es mi inspiración diaria",
    "contigo hasta lo ordinario es extraordinario",
    "tu sabiduría guía mis decisiones",
    "tus sueños son mis motivaciones",
    "en tu corazón encontré mi paz",
    "tu valentía me enseña a volar",
    "cada detalle tuyo me fascina",
    "tu ternura cura mis heridas",
    "tu pasión enciende mi alma",
    "tu honestidad construye nuestra confianza",
    "tu generosidad no conoce límites",
    "tu mirada transmite mil verdades",
    "tu compromiso fortalece nuestro amor",
    "tu risa es mi melodía favorita",
    "tu inteligencia me estimula constantemente",
    "tu perseverancia es admirable",
    "tu creatividad sorprende mi mundo",
    "tu compañía es mi mejor regalo",
    "tu sensibilidad embellece la vida",
    "tu elegancia trasciende lo físico",
    "tu humor alegra mis días grises",
    "tu compasión toca mi corazón",
    "tu dedicación inspira mi crecimiento",
    "tu misterio me mantiene cautivado",
    "tu espontaneidad divierte mi ser",
    "tu calma equilibra mi existencia",
    "tu intuición nunca falla",
    "tu entrega hace todo posible",
    "tu romanticismo aviva la llama",
    "tu autenticidad es refrescante",
    "tu complicidad hace todo mejor",
    "tu apoyo es mi columna vertebral",
    "tu ambición complementa la mía",
    "tu paciencia enseña tolerancia",
    "tu energía contagia positividad",
    "tu cuidado nutre mi espíritu",
    "tu complicidad crea magia",
    "tu determinación rompe barreras",
    "tu vulnerabilidad nos acerca",
    "tu confianza me fortalece",
    "tu crecimiento personal me enorgullece",
    "tu forma de amar me transforma",
    "tu resiliencia es inspiradora",
    "tu compañerismo construye equipo",
    "tu romanticismo mantiene viva la pasión",
    "tu capacidad de perdonar ennoblece",
    "tu sonrisa cura cualquier mal día",
    "tu forma de ver la vida enseña",
    "tu compromiso supera obstáculos",
    "tu presencia equilibra mi universo",
    "tu amor trasciende lo terrenal"
]

TERMINOS_CARIÑO = ["bebita", "princesa", "reina", "amada", "vida", "inspiración", "destino"]

def generar_mensaje_coherente():
    plantilla = random.choice(PLANTILLAS)
    term = random.choice(TERMINOS_CARIÑO)
    message = random.choice(MENSAJES_BASE)
    
    # Ajustes gramaticales avanzados
    if "¿Sabías" in plantilla:
        message = message[0].lower() + message[1:]
    if plantilla.startswith("¡"):
        message = message.capitalize()
    if "..." in plantilla:
        term = term.capitalize()
    
    # Generar mensaje final
    mensaje = plantilla.format(term=term, message=message.capitalize())
    
    # Limpieza y formato final
    palabras = mensaje.split()[:14]
    mensaje_final = ' '.join(palabras)
    
    # Asegurar signos de puntuación
    if not any(mensaje_final.endswith(c) for c in [".", "!", "?", "..."]):
        mensaje_final += "."
    
    return mensaje_final

# Interfaz mejorada
st.set_page_config(page_title="Generador de Amor", page_icon="💖")

user_code = st.text_input("Ingrese el código de acceso", type="password")

if user_code == ACCESS_CODE:
    st.success("🌟 ¡Bienvenida princesa! 🌟")
    
    with st.expander("✨ Configuración Especial"):
        col1, col2 = st.columns(2)
        with col1:
            tema = st.selectbox("Tema del mensaje:", ["Romántico", "Apasionado", "Poético", "Gracias", "Promesas"])
        with col2:
            intensidad = st.slider("Intensidad romántica:", 1, 5, 3)
    
    if st.button("🎇 Generar Mensaje Único"):
        with st.spinner("Creando magia amorosa..."):
            for _ in range(3):
                mensaje = generar_mensaje_coherente()
              # Busca esta sección en el código:
                if len(mensaje.split()) >= 6 and any(term in mensaje.lower() for term in TERMINOS_CARIÑO):
                    st.balloons()  # <---- ESTA LÍNEA CAMBIAR
                    # Por esto:
                    st.markdown(f"""
                    <div style='background:#FFFFFF;padding:25px;border-radius:15px;margin:20px 0;border: 2px solid #FF0076;box-shadow: 0 4px 8px rgba(233,30,99,0.1);'>
                        <h3 style='text-align:center;margin-bottom:20px;color:#B4004E;'>💌 Mensaje Especial 💌</h3>
                        <p style='font-size:20px;line-height:1.6;text-align:center;font-family:Helvetica;color:#E91E63;'>{mensaje}</p>
                    </div>
                    """)
                    st.download_button("📥 Descargar Mensaje", mensaje, file_name="mensaje_amor.txt")
                    break
                    
            else:
                st.error("⚠️ ¡Necesito más de tu energía amorosa! Intenta nuevamente")

else:
    if user_code:
        st.error("🔒 Código incorrecto, mi amor")

# Sección de footer personalizado
st.markdown("---")
st.markdown("""

<div class="footer">
    ✨ Sistema creado con el corazón por tu bebito ✨<br>
    💝 Cada mensaje contiene parte de mi corazón 💝
</div>
""", unsafe_allow_html=True)
