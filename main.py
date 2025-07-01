import streamlit as st
from ui import calendario, tareas, chat

# Título general
st.set_page_config(page_title="AURA", layout="wide")
st.title("AURA")

# Definir páginas como funciones
def vista_calendario():
    calendario.mostrar()

def vista_tareas():
    tareas.mostrar()

def vista_chat():
    chat.mostrar()

# Crear objetos de página con íconos
calendario_page = st.Page(vista_calendario, title="Calendario", icon=":material/calendar_today:")
tareas_page = st.Page(vista_tareas, title="Tareas", icon=":material/check_circle:")
chat_page = st.Page(vista_chat, title="Chat AURA", icon=":material/chat:")

# Diccionario de secciones
page_dict = {
    "Asistente": [chat_page],
    "Planificación": [calendario_page, tareas_page],
    
}

# Navegación con menú agrupado
pg = st.navigation(page_dict)
pg.run()
