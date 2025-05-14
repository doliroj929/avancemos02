# menu.py

import json
from registro import registrarse
from servicios import servicios_publicados, publicar_servicio
from chatbot import chatbot_recomendador
from datos import guardar_datos, cargar_datos
from usuario import registrar_servicio


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
            from usuario import iniciar_sesion  # Importación local dentro de la función
            nombre_usuario = iniciar_sesion(datos)  # Llamamos a la función de iniciar sesión y obtenemos el nombre de usuario
            menu_usuario(datos, nombre_usuario)  # Llamamos al menú de usuario con los datos y el nombre de usuario
        elif opcion == '3':
            servicios_publicados(datos)
        elif opcion == '4':
            print("Ver servicios solicitados - Pendiente de implementación.")
        elif opcion == '5':
            print("Volver atrás.")
        elif opcion == '6':
            guardar_datos(datos)  # Guardamos los datos al salir
            break




# menu.py

def menu_usuario(datos, nombre_usuario):
    print("--- Menú de Usuario ---")
    print("1. Ver perfil")
    print("2. Ver servicios publicados")
    print("3. Ver servicios solicitados")
    print("4. Registrar nuevo servicio")
    print("5. Solicitar un servicio")
    print("6. Cerrar sesión")
    
    seleccion = input("Selecciona una opción: ")
    if seleccion == "1":
        print("Mostrando perfil...")
    elif seleccion == "2":
        # Asegúrate de que tienes la función 'ver_servicios_publicados' correctamente definida
        ver_servicios_publicados(datos, nombre_usuario)  # Ver servicios publicados
    elif seleccion == "3":
        # Asegúrate de que tienes la función 'ver_servicios_solicitados' correctamente definida
        ver_servicios_solicitados(datos, nombre_usuario)  # Ver los servicios solicitados
    elif seleccion == "4":
        registrar_servicio(datos, nombre_usuario)  # Registrar un servicio
    elif seleccion == "5":
        # Asegúrate de que tienes la función 'solicitar_servicio' correctamente definida
        solicitar_servicio(datos, nombre_usuario)  # Solicitar un servicio
    elif seleccion == "6":
        print("Cerrando sesión...")
    else:
        print("Opción no válida.")






