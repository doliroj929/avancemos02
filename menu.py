# menu.py (fragmento)

from servicios import servicios_publicados
from datos import cargar_datos, guardar_datos
from registro import registrarse
from usuario import iniciar_sesion, registrar_servicio, solicitar_servicio, ver_servicios_solicitados

from servicios import servicios_publicados, servicios_solicitados_global
# ... resto de imports

def menu_principal():
    datos = cargar_datos()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Servicios publicados")
        print("4. Ver servicios solicitados")  # Esta opción muestra solicitudes globales
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

