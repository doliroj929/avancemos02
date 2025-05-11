import json
from src.chatbot import chatbot_recomendador

# Función de registro de usuarios
def registrarse(datos):
    print("\n--- Registrarse ---")
    nombre_usuario = input("Nombre de usuario: ")
    provincia = input("Selecciona tu provincia (Almería, Cádiz, Córdoba, Granada, Huelva, Jaén, Málaga, Sevilla): ")
    
    # Validación de provincia
    provincias_validas = ["Almería", "Cádiz", "Córdoba", "Granada", "Huelva", "Jaén", "Málaga", "Sevilla"]
    if provincia not in provincias_validas:
        print("Provincia no válida.")
        return

    tipo_usuario = input("¿Deseas ser 'colaborador' (ofrecer servicios) o 'cliente' (solicitar servicios)? ")

    if tipo_usuario == 'colaborador':
        categoria = chatbot_recomendador()
        descripcion = input("Describe el servicio que quieres ofrecer: ")
        correo = input("Introduce tu correo electrónico: ")

        # Crear nuevo usuario
        nuevo_usuario = {
            "nombre_usuario": nombre_usuario,
            "provincia": provincia,
            "tipo_usuario": tipo_usuario,
            "servicios_publicados": [{
                "categoria": categoria,
                "descripcion": descripcion,
                "correo": correo,
                "provincia": provincia
            }]
        }
        datos["usuarios"].append(nuevo_usuario)
        print(f"¡Te has registrado como colaborador en {provincia}!")
    elif tipo_usuario == 'cliente':
        nuevo_usuario = {
            "nombre_usuario": nombre_usuario,
            "provincia": provincia,
            "tipo_usuario": tipo_usuario,
            "servicios_publicados": []
        }
        datos["usuarios"].append(nuevo_usuario)
        print(f"¡Te has registrado como cliente en {provincia}!")
    else:
        print("Tipo de usuario no válido.")
