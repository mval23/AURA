import json

def cargar_recursos():
    with open("data/recursos.json", "r", encoding="utf-8") as f:
        return json.load(f)

def recomendar_recursos(titulo: str) -> list:
    recursos = cargar_recursos()
    titulo = titulo.lower()
    sugerencias = []

    for recurso in recursos:
        if any(palabra in titulo for palabra in recurso["titulo"].lower().split()):
            sugerencias.append(recurso)

    return sugerencias
