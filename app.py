import streamlit as st
import random

ACCESS_CODE = "1234"

EXPRESIONES = [
    # Términos cariñosos (30% de probabilidad)
    "Mi preciosa bebita",
    "Princesa de mi corazón",
    "Amada mía",
    "Mi niña bonita",
    "Reina de mi alma",
    
    # Tus 102 mensajes (agregados y adaptados)
    "Eres mi razón de ser, bebita",
    "Eres mi razón de ser",  
    "Mi mundo es mejor desde que estás en él",  
    "Te amo más de lo que las palabras pueden expresar",  
    "Eres mi sol en los días nublados",  
    "No puedo imaginar mi vida sin ti",  
    "Cada momento a tu lado es un regalo",  
    "Gracias por ser mi todo",  
    "Eres mi hogar, mi paz y mi felicidad",  
    "No dejo de enamorarme de ti cada día",  
    "Contigo, todo tiene sentido",  
    "Mi corazón siempre late por ti",  
    "Me haces sentir la persona más afortunada del mundo",  
    "Eres mi sueño hecho realidad",  
    "Contigo, todo es más brillante",  
    "Eres mi amor eterno",  
    "Te elijo hoy y siempre",  
    "Mi vida está llena de amor gracias a ti",  
    "Eres mi mayor bendición",  
    "Cada día me enamoras más",  
    "Tu sonrisa ilumina mi alma",  
    "Eres mi refugio y mi fortaleza",  
    "No puedo dejar de pensar en ti",  
    "Eres mi mejor decisión",  
    "Mi amor por ti no tiene límites",  
    "Cada instante contigo es mágico",  
    "Me haces sentir vivo",  
    "Eres mi persona favorita en el mundo",  
    "Contigo aprendí lo que es el verdadero amor",  
    "Eres mi mejor amigo y mi amor eterno",  
    "No hay nadie como tú en este mundo",  
    "Mi felicidad está a tu lado",  
    "Tu amor es mi mayor tesoro",  
    "Te amo con todo mi corazón",  
    "Eres mi historia favorita",  
    "Mi amor por ti crece cada día más",  
    "Eres mi inspiración y mi alegría",  
    "Eres el motivo de mi sonrisa cada mañana",  
    "Te amo por ser exactamente quien eres",  
    "Mi corazón te pertenece por completo",  
    "No hay un día en que no piense en ti",  
    "Tu amor me llena de paz y felicidad",  
    "Eres la luz de mi vida",  
    "Estoy agradecido por cada momento contigo",  
    "Eres mi todo, mi siempre y mi para siempre",  
    "Eres mi mayor alegría y mi más grande amor",  
    "Nunca me cansaré de decirte cuánto te amo",  
    "Mi corazón late al ritmo de tu amor",  
    "Eres mi mejor capítulo",  
    "Contigo, todo es perfecto",  
    "Eres mi alma gemela",  
    "Mi amor por ti es infinito",  
    "Eres la melodía de mi corazón",  
    "Tu amor me hace invencible",  
    "Eres la razón de mis suspiros",  
    "No hay nada que no haría por ti",  
    "Eres mi mayor bendición en esta vida",  
    "Mi felicidad es verte feliz",  
    "Tu amor me da fuerzas para todo",  
    "Eres el amor de mi vida",  
    "Tu presencia hace que todo sea mejor",  
    "Eres mi mayor motivo para sonreír",  
    "Cada día a tu lado es una aventura increíble",  
    "Mi amor por ti es eterno",  
    "Me haces sentir amado y especial",  
    "Eres mi felicidad hecha persona",  
    "Cada abrazo tuyo me llena de paz",  
    "Tu amor me completa",  
    "Contigo, soy la mejor versión de mí mismo/a",  
    "Mi corazón es tuyo para siempre",  
    "Eres el mejor regalo que la vida me dio",  
    "Mi amor por ti nunca se desvanecerá",  
    "Contigo, la vida es más dulce",  
    "Tu amor es mi mayor fortaleza",  
    "Eres mi presente, mi futuro y mi siempre",  
    "Tu sonrisa ilumina mi mundo",  
    "Cada beso tuyo me llena de vida",  
    "Eres la razón por la que creo en el amor",  
    "Contigo quiero compartirlo todo",  
    "Tu amor es el motor de mi vida",  
    "Eres la pieza que faltaba en mi vida",  
    "Mi corazón se acelera cada vez que te veo",  
    "Eres mi razón para soñar en grande",  
    "Cada día agradezco tenerte en mi vida",  
    "Eres el poema más hermoso que he conocido",  
    "Te amo como jamás imaginé amar a alguien",  
    "Tu amor hace que todo valga la pena",  
    "Eres mi refugio y mi lugar seguro",  
    "Contigo, el mundo es un lugar mejor",  
    "Mi corazón es tuyo, ahora y siempre",  
    "Eres la razón de mis mejores días",  
    "Mi amor por ti es inquebrantable",  
    "Eres mi más dulce fantasía hecha realidad",  
    "Cada caricia tuya llena mi alma",  
    "Eres el centro de mi universo",  
    "Tu amor me hace sentir invencible",  
    "Eres la respuesta a todas mis oraciones",  
    "Contigo quiero envejecer",  
    "Eres mi siempre y mi para siempre",  
    "No hay lugar en el mundo donde prefiera estar que contigo",  
    "Te amo más allá de las estrellas y hasta el infinito".  

    
    # Estructuras base para combinar
    "Mi {term} {verb} {complemento}",
    "{term}, {message}",
    "Para mi {term}: {message}"
]

TERMINOS_CARIÑO = ["bebita", "princesa", "amada", "reina", "vida"]
VERBOS = ["iluminas", "embelleces", "completas", "transformas", "enalteces"]
COMPLEMENTOS = ["mi existir", "cada día", "mi universo", "mi alma", "este amor"]

def generar_mensaje():
    base = random.choice(EXPRESIONES)
    
    if "{term}" in base:
        term = random.choice(TERMINOS_CARIÑO)
        verb = random.choice(VERBOS)
        comp = random.choice(COMPLEMENTOS)
        return base.format(term=term, verb=verb, complemento=comp)
    
    # 70% de probabilidad de añadir término cariñoso
    if random.random() < 0.7:  
        term = random.choice([" mi " + random.choice(TERMINOS_CARIÑO), ", " + random.choice(TERMINOS_CARIÑO)])
        insert_pos = random.randint(0, len(base.split()))
        words = base.split()
        words.insert(insert_pos, term)
        return " ".join(words[:12])  # Limitar a 12 palabras máximo
    
    return base

user_code = st.text_input("Ingrese el código de acceso", type="password")

if user_code == ACCESS_CODE:
    st.success("¡Generador de Amor para Mi Princesa!")
    
    if st.button("Crear Mensaje"):
        for _ in range(3):
            mensaje = generar_mensaje()
            palabras = mensaje.split()[:10]
            final = " ".join(palabras).capitalize()
            
            # Verificar calidad
            if any(term in final.lower() for term in TERMINOS_CARIÑO) and len(palabras) >=5:
                st.markdown(f"### 💖 Para Mi Bebita:\n> *{final}*")
                break
        else:
            st.error("El universo del amor necesita recargarse - ¡Intenta de nuevo!")
else:
    if user_code:
        st.error("Código incorrecto, mi princesa")
