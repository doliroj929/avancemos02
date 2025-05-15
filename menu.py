# menu.py

from registro import registrarse
from servicios import servicios_publicados, servicios_solicitados_global
from datos import guardar_datos, cargar_datos
from usuario import (
    iniciar_sesion,
    registrar_servicio,
    solicitar_servicio,
    ver_servicios_publicados,
    ver_servicios_solicitados
)

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
            nombre_usuario = iniciar_sesion(datos)
            if nombre_usuario:
                menu_usuario(datos, nombre_usuario)
        elif opcion == '3':
            servicios_publicados()
        elif opcion == '4':
            servicios_solicitados_global()
        elif opcion == '5':
            print("Volver atrás.")
        elif opcion == '6':
            guardar_datos(datos)
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def menu_usuario(datos, nombre_usuario):
    while True:
        print(f"\n--- Menú de Usuario: {nombre_usuario} ---")
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
            ver_servicios_publicados(datos, nombre_usuario)
        elif seleccion == "3":
            ver_servicios_solicitados(datos, nombre_usuario)
        elif seleccion == "4":
            registrar_servicio(datos, nombre_usuario)
        elif seleccion == "5":
            solicitar_servicio(datos, nombre_usuario)
        elif seleccion == "6":
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
