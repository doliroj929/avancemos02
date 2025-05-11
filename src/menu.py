import json
from src.registro import registrarsefrom src.usuario import iniciar_sesion
from src.servicios import servicios_publicados, publicar_servicio
from src.chatbot import chatbot_recomendador

# Menú Principal
def menu_principal():
    datos = cargar_datos()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Servicios publicados")
        print("4. Ver servicios solicitados")
        print("5. Volver atrás")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            registrarse(datos)
        elif opcion == '2':
            iniciar_sesion(datos)
        elif opcion == '3':
            servicios_publicados(datos)
        elif opcion == '4':
            print("Ver servicios solicitados - Pendiente de implementación.")
        elif opcion == '5':
            print("Volver atrás.")
        elif opcion == '6':
            guardar_datos(datos)
            break

# Función para cargar los datos
def cargar_datos():
    try:
        with open('data/usuarios.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"usuarios": []}

# Función para guardar los datos..
def guardar_datos(datos):
    with open('data/usuarios.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)
