import streamlit as st
from services.google_auth import login, get_user_email
from ui.sidebar import render_sidebar

st.set_page_config(page_title="AURA", layout="wide")

st.title("🎓 AURA – Asistente Universitario con Recomendaciones y Autonomía")

# Autenticación
if "token" not in st.session_state:
    login()
else:
    email = get_user_email()
    st.success(f"Sesión iniciada como: {email}")

    # UI principal
    render_sidebar()

    st.subheader("Bienvenido a tu espacio inteligente 🧠")
    st.write("Aquí verás tus tareas, calendario, y recomendaciones personalizadas.")
