from registro import registrarse
from datos import guardar_datos, cargar_datos
from usuario import (
    iniciar_sesion,
    registrar_servicio,
    solicitar_servicio,
    ver_servicios_publicados,
    ver_servicios_solicitados_global,
    ver_servicios_publicados_global
)
from chatbot import chatbot_que_puedo_ofrecer

def menu_principal():
    datos = cargar_datos()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Ver servicios publicados")
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
            ver_servicios_publicados_global(datos)
            input("\nPresiona Enter para volver al menú principal.")
        elif opcion == '4':
            ver_servicios_solicitados_global(datos)
            input("\nPresiona Enter para volver al menú principal.")
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
        print("1. Ver servicios publicados")
        print("2. Publicar servicio")
        print("3. Solicitar servicio")
        print("4. ¿Qué puedo ofrecer?")
        print("5. Ver servicios publicados (global)")
        print("6. Ver servicios solicitados (global)")
        print("7. Volver atrás")
        print("8. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            ver_servicios_publicados(datos, nombre_usuario)
            input("\nPresiona Enter para volver al menú de usuario.")
        elif opcion == '2':
            registrar_servicio(datos, nombre_usuario)
        elif opcion == '3':
            solicitar_servicio(datos, nombre_usuario)
        elif opcion == '4':
            chatbot_que_puedo_ofrecer()
        elif opcion == '5':
            ver_servicios_publicados_global(datos)
            input("\nPresiona Enter para volver al menú de usuario.")
        elif opcion == '6':
            ver_servicios_solicitados_global(datos)
            input("\nPresiona Enter para volver al menú de usuario.")
        elif opcion == '7':
            print("Volviendo atrás...")
            break
        elif opcion == '8':
            print("Cerrando sesión...")
            exit()
        else:
            print("Opción no válida. Intenta de nuevo.")
