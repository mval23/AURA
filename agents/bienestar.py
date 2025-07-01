from datetime import datetime, timedelta

def analizar_bienestar(tareas: list, eventos: list) -> list[str]:
    advertencias = []

    eventos_por_dia = {}
    for e in eventos:
        if "inicio" not in e:
            continue
        try:
            inicio = datetime.fromisoformat(e["inicio"])
        except ValueError:
            continue

        dia = inicio.date()
        eventos_por_dia.setdefault(dia, []).append(inicio)

    for dia, inicios in eventos_por_dia.items():
        inicios.sort()
        bloques = 1
        for i in range(1, len(inicios)):
            if (inicios[i] - inicios[i-1]) < timedelta(hours=1):
                bloques += 1
            else:
                bloques = 1
            if bloques > 3:
                advertencias.append(f"El {dia} tienes más de 3 sesiones seguidas sin descanso.")
                break

        if len(inicios) >= 5:
            advertencias.append(f"El {dia} podrías estar saturado. Considera tomar pausas.")

    hoy = datetime.now().date()
    for t in tareas:
        if not t.get("completado", False) and "fecha_entrega" in t:
            try:
                entrega = datetime.fromisoformat(t["fecha_entrega"]).date()
            except ValueError:
                continue

            if entrega <= hoy + timedelta(days=2):
                relacionada = any(
                    "inicio" in e and entrega == datetime.fromisoformat(e["inicio"]).date()
                    and "Estudio" in e.get("titulo", "")
                    for e in eventos
                )
                if not relacionada:
                    advertencias.append(f"La tarea '{t['titulo']}' es urgente y no tiene sesión de estudio asignada.")

    return advertencias
