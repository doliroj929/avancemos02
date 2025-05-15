# datos.py

import json
import os

RUTA_ARCHIVO = 'avancemos02/data/usuarios.json'

def asegurar_carpeta():
    carpeta = os.path.dirname(RUTA_ARCHIVO)
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

def cargar_datos():
    try:
        with open(RUTA_ARCHIVO, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("El archivo no existe. Se creará uno nuevo.")
        return {"usuarios": []}
    except json.JSONDecodeError:
        print("Error leyendo el archivo. Se usará estructura vacía.")
        return {"usuarios": []}

def guardar_datos(datos):
    try:
        asegurar_carpeta()
        with open(RUTA_ARCHIVO, 'w') as f:
            json.dump(datos, f, indent=4)
        print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
