# datos.py

import json
import os

# Función para guardar los datos en el archivo JSON
def guardar_datos(datos):
    try:
        # Asegurarse de que la carpeta 'avancemos02/data' exista
        if not os.path.exists('avancemos02/data'):
            os.makedirs('avancemos02/data')  # Crear la carpeta si no existe

        # Imprimir los datos para verificar que se están guardando
        print("Guardando datos:", datos)

        # Guardar el archivo en la ruta correcta dentro de 'avancemos02/data/'
        with open('avancemos02/data/usuarios.json', 'w') as archivo:
            json.dump(datos, archivo, indent=4)
        print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

# Función para cargar los datos desde el archivo JSON
def cargar_datos():
    try:
        # Cambiar la ruta a 'avancemos02/data/usuarios.json'
        with open('avancemos02/data/usuarios.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("El archivo de usuarios no existe. Se creará uno nuevo.")
        return {"usuarios": []}
    except json.JSONDecodeError:
        print("Error al leer los datos del archivo.")
        return {"usuarios": []}
