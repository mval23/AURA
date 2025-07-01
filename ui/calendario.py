import streamlit as st
from streamlit_calendar import calendar
from utils.io import cargar_eventos

def mostrar():
    st.title("Calendario semanal")

    eventos = cargar_eventos()

    calendar(
        events=eventos,
        options={
            "initialView": "timeGridWeek",
            "slotMinTime": "00:00:00",
            "slotMaxTime": "24:00:00",
            "allDaySlot": False,
            "locale": "es",
            "nowIndicator": True
        }
    )
