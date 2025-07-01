import streamlit as st
from utils.io import cargar_tareas, guardar_tareas

def mostrar():
    st.title("Lista de tareas")

    tareas = cargar_tareas()

    nueva_tarea = st.text_input("Nueva tarea")
    if st.button("Agregar tarea") and nueva_tarea:
        tareas.append({"titulo": nueva_tarea, "completado": False})
        guardar_tareas(tareas)
        st.rerun()


    st.subheader("Tareas:")
    for i, tarea in enumerate(tareas):
        tareas[i]["completado"] = st.checkbox(
            tarea["titulo"],
            value=tarea["completado"],
            key=f"tarea_{i}"
        )

    # Guardar cambios al marcar/desmarcar
    guardar_tareas(tareas)
