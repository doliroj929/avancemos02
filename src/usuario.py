import json
from src.menu import menu_usuario

# Función para iniciar sesión
def iniciar_sesion(datos):
    print("\n--- Iniciar sesión ---")
    nombre_usuario = input("Nombre de usuario: ")

    # Buscar el usuario
    usuario = next((usuario for usuario in datos["usuarios"] if usuario["nombre_usuario"] == nombre_usuario), None)
    
    if usuario:
        print(f"¡Hola, {usuario['nombre_usuario']}!")
        menu_usuario(usuario, datos)
    else:
        print("Usuario no encontrado.")
