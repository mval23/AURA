import streamlit as st
from agents.chatbot import procesar_mensaje  # Nuevo: usamos el chatbot modular

def mostrar():
    st.title("Chat AURA")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Mostrar historial
    for mensaje in st.session_state.chat_history:
        with st.chat_message(mensaje["role"]):
            st.markdown(mensaje["content"])

    # Entrada del usuario
    prompt = st.chat_input("Escribe tu mensaje aquí...")

    if prompt:
        # Mostrar mensaje del usuario
        st.chat_message("user").markdown(prompt)
        st.session_state.chat_history.append({"role": "user", "content": prompt})

        # Llamada al agente chatbot
        respuesta = procesar_mensaje(prompt)

        # Mostrar respuesta del sistema
        with st.chat_message("assistant"):
            st.markdown(respuesta)
        st.session_state.chat_history.append({"role": "assistant", "content": respuesta})
