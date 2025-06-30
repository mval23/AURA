import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.image("assets/logo.png", width=100)
        st.title("Menú")
        st.page_link("app.py", label="🏠 Inicio")
        st.page_link("app.py?page=calendar", label="📅 Calendario")
        st.page_link("app.py?page=tasks", label="📝 Tareas")
        st.page_link("app.py?page=chat", label="💬 Chat con AURA")
        st.page_link("app.py?page=recommendations", label="🎯 Recomendaciones")
