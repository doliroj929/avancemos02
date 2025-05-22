import json
import os

RUTA_ARCHIVO = "data/usuarios.json"

def cargar_datos():
    if not os.path.exists(RUTA_ARCHIVO):
        return []  # Lista vacía si no existe archivo

    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
        try:
            datos = json.load(archivo)
            # Comprobamos que sea una lista
            if isinstance(datos, list):
                return datos
            else:
                print("Error: datos corruptos, se esperaba lista.")
                return []
        except json.JSONDecodeError:
            print("Error: archivo JSON corrupto o vacío.")
            return []

def guardar_datos(datos):
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
