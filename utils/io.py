import json
from pathlib import Path

DATA_DIR = Path("data")

def cargar_json(nombre_archivo):
    ruta = DATA_DIR / nombre_archivo
    if ruta.exists():
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_json(nombre_archivo, datos):
    ruta = DATA_DIR / nombre_archivo
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)

# Accesos rápidos
def cargar_tareas():
    return cargar_json("tareas.json")

def guardar_tareas(tareas):
    guardar_json("tareas.json", tareas)

def cargar_eventos():
    return cargar_json("calendario.json")

def guardar_eventos(eventos):
    guardar_json("calendario.json", eventos)
