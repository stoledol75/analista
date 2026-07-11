import streamlit as st

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA Y ESTILOS
# ==========================================
st.set_page_config(
    page_title="DataLab Tecmilenio - DataMentor",
    page_icon="🚀",
    layout="centered"
)

# Estilos personalizados para emular el ecosistema Tecmilenio
st.markdown("""
    <style>
    .main-title { font-size: 32px; font-weight: bold; color: #1E3A8A; text-align: center; }
    .subtitle { font-size: 18px; color: #4B5563; text-align: center; margin-bottom: 30px; }
    .badge { background-color: #D1FAE5; color: #065F46; padding: 4px 10px; border-radius: 8px; font-weight: bold; }
    .stButton>button { background-color: #1E3A8A; color: white; border-radius: 8px; width: 100%; }
    </style>
""", unsafe_index=True)

# ==========================================
# ESTADO DE LA SESIÓN (Control del progreso)
# ==========================================
if 'fase' not in st.session_state:
    st.session_state.fase = 0  # 0: Selección de caso, 1: Fase 1, 2: Fase 2...
if 'puntos' not in st.session_state:
    st.session_state.puntos = 0
if 'caso_elegido' not in st.session_state:
    st.session_state.caso_elegido = None

# ==========================================
# COMPONENTES INTERACTIVOS / VISTAS
# ==========================================

st.markdown("<div class='main-title'>🚀 DataLab Tecmilenio</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>¡Bienvenido al laboratorio del futuro! Conviértete en Analista de Datos Junior.</div>", unsafe_allow_html=True)

# Barra de progreso de gamificación
st.sidebar.header("📊 Tu Perfil de Analista")
st.sidebar.metric(label="Puntuación de Pensamiento Crítico 🧠", value=f"{st.session_state.puntos} PTS")
if st.session_state.fase > 0:
    st.sidebar.success(f"Caso Activo: {st.session_state.caso_elegido}")
    if st.sidebar.button("🔄 Reiniciar Laboratorio"):
        st.session_state.fase = 0
        st.session_state.puntos = 0
        st.rerun()

# ------------------------------------------
# VISTA 0: SELECCIÓN DEL RETO
# ------------------------------------------
if st.session_state.fase == 0:
    st.markdown("### 📂 Selecciona tu Caso de Estudio de Negocio")
    st.info("💡 Lee las opciones y selecciona el reto que más te apasione para iniciar tu consultoría.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🎮 Caso 1")
        st.markdown("**Gaming & Streaming**\n\nAnaliza tendencias de Twitch/YouTube para romper récords de audiencia.")
        if st.button("Elegir Gaming"):
            st.session_state.caso_elegido = "Gaming & Streaming"
            st.session_state.fase = 1
            st.rerun()
            
    with col2:
        st.subheader("👟 Caso 2")
        st.markdown("**E-Commerce de Moda**\n\nOptimiza el inventario y detecta tendencias en tenis urbanos.")
        if st.button("Elegir E-Commerce"):
            st.session_state.caso_elegido = "E-Commerce de Moda"
            st.session_state.fase = 1
            st.rerun()

    with col3:
        st.subheader("🎵 Caso 3")
        st.markdown("**Spotify Insights**\n\nAnaliza métricas de audio y predice el próximo éxito del verano.")
        if st.button("Elegir Spotify"):
            st.session_state.caso_elegido = "Spotify Insights"
            st.session_state.fase = 1
            st.rerun()

# ------------------------------------------
# VISTA 1: FASE 1 - ENTENDER EL PROBLEMA
# ------------------------------------------
elif st.session_state.fase == 1:
    st.markdown(f"### 🎯 Fase 1: Entender el Problema | Caso: {st.session_state.caso_elegido}")
    
    # Dataset simulado interactivo
    st.write("Aquí tienes la base de datos preliminar extraída del cliente:")
    
    if st.session_state.caso_elegido == "Gaming & Streaming":
        data = {
            "Categoría": ["Minecraft", "Valorant", "Just Chatting"],
            "Audiencia Promedio": [1200, 2500, 3800],
            "Horas Transmitidas": [10, 4, 2],
            "Interacción del Chat": ["Media", "Alta", "Baja"]
        }
        st.table(data)
        
        st.markdown("🤔 **El Reto:** Si el streamer busca **alta interacción con el chat** y **maximizar espectadores por hora**, ¿cuál es la mejor opción?")
        opciones = ["Selecciona una opción...", "Minecraft", "Valorant", "Just Chatting"]
        respuesta = st.selectbox("¿Cuál es tu diagnóstico preliminar?", opciones)
        
        # Botones de auxilio solicitados por la metodología
        col_p, col_e = st.columns(2)
        with col_p:
            if st.button("❓ Solicitar /pista"):
                st.warning("Pista: Divide la Audiencia Promedio entre las Horas Transmitidas para ver el rendimiento real por hora y revisa la columna de interacción.")
        with col_e:
            if st.button("💡 Solicitar /explicame"):
                st.info("Explicación: Imagina que abres una tienda. No es lo mismo vender 10 productos en 10 horas, que vender 9 productos en sólo 1 hora. ¡El tiempo invertido importa!")

        if respuesta == "Valorant":
            st.success("🎉 ¡Excelente análisis! Valorant tiene la interacción más alta y genera 625 espectadores por hora de transmisión (más eficiente que Minecraft).")
            if st.button("Avanzar a Fase 2 ➡️"):
                st.session_state.puntos += 10
                st.session_state.fase = 2
                st.rerun()
        elif respuesta != "Selecciona una opción...":
            st.error("Buen intento, pero analiza con cuidado la relación de espectadores por hora y el nivel del chat. ¡Inténtalo de nuevo!")

# ------------------------------------------
# VISTA 2: FASE 2 - EL ALGORITMO
# ------------------------------------------
elif st.session_state.fase == 2:
    st.markdown("### 🧠 Fase 2: Diseñar el Algoritmo (Lógica)")
    st.write("¡Fase 1 completada! +10 en Pensamiento Crítico 🧠")
    
    st.markdown("Ahora debes estructurar la lógica para automatizar este análisis. Ordena los pasos lógicos del programa:")
    
    paso1 = st.checkbox("1. Recibir datos de Audiencia, Horas e Interacción (Input)")
    paso2 = st.checkbox("2. Calcular la métrica: Audiencia / Horas (Proceso)")
    paso3 = st.checkbox("3. Mostrar en pantalla el juego recomendado (Output)")
    
    if paso1 and paso2 and paso3:
        st.success("¡Algoritmo estructurado perfectamente! Input ➡️ Proceso ➡️ Output.")
        if st.button("Avanzar a la Fase de Código (Fase 3) ➡️"):
            st.session_state.puntos += 15
            st.session_state.fase = 3
            st.rerun()

# ------------------------------------------
# VISTA 3: FASE 3 Y 4 - CÓDIGO E IMPACTO
# ------------------------------------------
elif st.session_state.fase == 3:
    st.markdown("### 💻 Fase 3 y 4: Código Limpio e Impacto")
    st.write("¡Lógica aprobada! +15 puntos en Diseño Algorítmico 💻")
    
    st.write("Completa la línea de código en Python para calcular el rendimiento por hora:")
    
    codigo_plantilla = """
audiencia = 2500
horas = 4
# ¿Qué operador matemático completa la fórmula?
espectadores_por_hora = audiencia ___ horas 
    """
    st.code(codigo_plantilla, language="python")
    
    operador = st.text_input("Escribe el operador matemático correcto (ej: +, -, *, /):")
    
    if operador == "/":
        st.success("¡Código Limpio y Correcto! El operador `/` realiza la división en Python.")
        
        st.markdown("---")
        st.markdown("### 📊 Fase 4: Reporte de Impacto")
        reporte = st.text_area("Como Analista de Datos Junior, escribe una breve conclusión para el streamer cliente:")
        
        if st.button("🚀 Enviar Reporte Final"):
            st.session_state.puntos += 25
            st.balloons()
            st.success(f"🏆 ¡Reto Completado con éxito! Has acumulado un total de {st.session_state.puntos} puntos de Bienestar e Innovación en el DataLab.")
            if st.button("Terminar y volver al inicio"):
                st.session_state.fase = 0
                st.session_state.puntos = 0
                st.rerun()
    elif operador != "":
        st.error("¡Ups! Ese operador no calculará los espectadores promedio por hora. Recuerda cómo se calcula una tasa promedio.")