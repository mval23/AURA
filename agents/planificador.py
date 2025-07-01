from datetime import datetime, timedelta
import pytz

TZ = pytz.timezone("America/Bogota")

def generar_plan(tareas, eventos):
    sesiones_generadas = []
    for tarea in tareas:
        if tarea.get("completado", False):
            continue  # Ignorar tareas ya completadas

        fecha_limite = tarea.get("fecha")  # formato esperado: YYYY-MM-DD
        if not fecha_limite:
            continue

        # Convertir la fecha límite a datetime
        try:
            deadline = TZ.localize(datetime.strptime(fecha_limite, "%Y-%m-%d"))
        except ValueError:
            continue

        # Intentar asignar una sesión el mismo día o días anteriores
        fecha_actual = datetime.now(TZ).replace(hour=8, minute=0, second=0, microsecond=0)
        dia = fecha_actual

        while dia.date() <= deadline.date():
            # Generar sesiones de 1h entre 8:00 y 20:00
            for hora in range(8, 20):
                inicio = dia.replace(hour=hora)
                fin = inicio + timedelta(hours=1)

                if not hay_conflicto(inicio, fin, eventos + sesiones_generadas):
                    nueva_sesion = {
                        "title": f"Estudiar: {tarea['titulo']}",
                        "start": inicio.isoformat(),
                        "end": fin.isoformat()
                    }
                    sesiones_generadas.append(nueva_sesion)
                    break  # Asignar solo una sesión por tarea
            dia += timedelta(days=1)

    return sesiones_generadas

def hay_conflicto(inicio, fin, eventos):
    """Verifica si el nuevo evento se cruza con alguno existente."""
    for evento in eventos:
        ev_inicio = datetime.fromisoformat(evento["start"])
        ev_fin = datetime.fromisoformat(evento["end"])

        # Asegura que todos sean aware con la misma zona horaria
        if ev_inicio.tzinfo is None:
            ev_inicio = TZ.localize(ev_inicio)
        if ev_fin.tzinfo is None:
            ev_fin = TZ.localize(ev_fin)

        if inicio < ev_fin and fin > ev_inicio:
            return True
    return False
