from agents.planificador import generar_plan
from agents.recomendador import recomendar_recursos
from agents.bienestar import analizar_bienestar

from utils.io import (
    cargar_tareas,
    guardar_tareas,
    cargar_eventos,
    guardar_eventos
)

def procesar_mensaje(mensaje: str) -> str:
    mensaje = mensaje.lower()

    if "planifica" in mensaje or "agenda" in mensaje:
        return _accion_planificar()

    elif "agrega" in mensaje or "añade" in mensaje:
        return _accion_agregar_tarea(mensaje)

    elif "tareas" in mensaje or "pendientes" in mensaje:
        return _accion_listar_tareas()

    elif "hola" in mensaje:
        return "Hola. Soy AURA, tu asistente. Puedes decir: 'Planifica mi semana', 'Agrega tarea', o '¿Qué tareas tengo?'."

    elif "recomiendas" in mensaje or "recurso" in mensaje:
        return _accion_recomendar(mensaje)

    elif any(palabra in mensaje for palabra in ["bienestar", "descanso", "estresado"]):
        return _accion_bienestar()

    return "No entendí tu mensaje. Intenta algo como 'Agrega tarea de mates para el viernes' o 'Planifica mi semana'."

def _accion_planificar():
    tareas = cargar_tareas()
    eventos = cargar_eventos()
    nuevas_sesiones = generar_plan(tareas, eventos)

    if nuevas_sesiones:
        eventos.extend(nuevas_sesiones)
        guardar_eventos(eventos)
        return f"Se han agendado {len(nuevas_sesiones)} sesiones de estudio en el calendario."
    else:
        return "No encontré espacios disponibles para agendar sesiones de estudio."

def _accion_listar_tareas():
    tareas = cargar_tareas()
    pendientes = [t["titulo"] for t in tareas if not t.get("completado", False)]
    if pendientes:
        return "Tienes estas tareas pendientes:\n- " + "\n- ".join(pendientes)
    else:
        return "No tienes tareas pendientes."

def _accion_agregar_tarea(mensaje: str):
    texto = mensaje.replace("agrega", "").replace("añade", "").strip()
    if not texto:
        return "¿Qué tarea quieres agregar?"

    nueva_tarea = {
        "titulo": texto.capitalize(),
        "completado": False,
        "fecha": None  # Este campo puede ser procesado más adelante con NLP
    }

    tareas = cargar_tareas()
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)

    return f"Tarea agregada: {nueva_tarea['titulo']}"

def _accion_recomendar(mensaje: str):
    tema = mensaje.replace("¿qué me recomiendas para", "").replace("?", "").strip()
    if not tema:
        return "¿Para qué tema necesitas recursos?"

    sugerencias = recomendar_recursos(tema)
    if sugerencias:
        respuesta = "Te recomiendo estos recursos:\n"
        for r in sugerencias:
            respuesta += f"- [{r['titulo']}]({r['enlace']}) ({r['tipo']})\n"
        return respuesta
    else:
        return "No encontré recursos específicos para ese tema. ¿Puedes darme más detalles?"

def _accion_bienestar():
    tareas = cargar_tareas()
    eventos = cargar_eventos()
    alertas = analizar_bienestar(tareas, eventos)

    if alertas:
        return "Aquí tienes algunas alertas de bienestar:\n\n" + "\n".join(alertas)
    else:
        return "Todo se ve bien. No detecté sobrecarga ni tareas urgentes sin planificar."
