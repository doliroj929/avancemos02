# usuario.py

from datos import cargar_datos
from datos import guardar_datos


def iniciar_sesion(datos):
    print("\n--- Iniciar sesión ---")
    nombre_usuario = input("Nombre de usuario: ")
    clave_ingreso = input("Clave de ingreso: ")

    usuario = next((u for u in datos["usuarios"] if u["nombre_usuario"] == nombre_usuario), None)

    if usuario:
        if usuario["clave_ingreso"] == clave_ingreso:
            print(f"¡Bienvenido, {nombre_usuario}!")
            return nombre_usuario
        else:
            print("Clave incorrecta.")
    else:
        print("Usuario no encontrado. Regístrate primero.")
    return None

#registar servicio 

def registrar_servicio(datos, nombre_usuario):
    usuario = next((u for u in datos["usuarios"] if u["nombre_usuario"] == nombre_usuario), None)
    if usuario is None:
        print("Usuario no encontrado.")
        return

    nombre_servicio = input("Introduce el nombre del servicio: ").strip()
    descripcion = input("Introduce la descripción del servicio: ").strip()

    if "servicios_publicados" not in usuario:
        usuario["servicios_publicados"] = []

    ids = [s.get("id", 0) for s in usuario["servicios_publicados"]]
    nuevo_id = max(ids) + 1 if ids else 1

    nuevo_servicio = {
        "id": nuevo_id,
        "nombre_servicio": nombre_servicio,
        "descripcion": descripcion
    }

    usuario["servicios_publicados"].append(nuevo_servicio)
    from datos import guardar_datos
    guardar_datos(datos)
    print(f"Servicio '{nombre_servicio}' registrado correctamente.")


def ver_servicios_publicados(datos, nombre_usuario):
    usuario = next((u for u in datos["usuarios"] if u["nombre_usuario"] == nombre_usuario), None)
    if not usuario or not usuario.get("servicios_publicados"):
        print("No tienes servicios publicados.")
        return

    print("\nTus servicios publicados:")
    for s in usuario["servicios_publicados"]:
        nombre = s.get("nombre_servicio") or s.get("categoria") or "Nombre no disponible"
        descripcion = s.get("descripcion", "Descripción no disponible")
        print(f"- {nombre}: {descripcion}")

def ver_servicios_solicitados(datos, nombre_usuario):
    usuario = next((u for u in datos["usuarios"] if u["nombre_usuario"] == nombre_usuario), None)
    if not usuario or not usuario.get("servicios_solicitados"):
        print("No tienes servicios solicitados.")
        return

    print("\nTus servicios solicitados:")
    for s in usuario["servicios_solicitados"]:
        nombre = s.get("nombre_servicio") or s.get("categoria") or "Nombre no disponible"
        descripcion = s.get("descripcion", "Descripción no disponible")
        print(f"- {nombre}: {descripcion}")



def solicitar_servicio(datos, nombre_usuario):
    usuario = next((u for u in datos["usuarios"] if u["nombre_usuario"] == nombre_usuario), None)
    if usuario is None:
        print("Usuario no encontrado.")
        return

    print("Introduce el nombre del servicio que quieres solicitar:")
    nombre_servicio = input().strip()
    descripcion = input("Descripción del servicio solicitado: ").strip()

    if "servicios_solicitados" not in usuario:
        usuario["servicios_solicitados"] = []

    nuevo_id = 1
    if usuario["servicios_solicitados"]:
        nuevo_id = max(s["id"] for s in usuario["servicios_solicitados"]) + 1

    nueva_solicitud = {
        "id": nuevo_id,
        "nombre_servicio": nombre_servicio,
        "descripcion": descripcion
    }

    usuario["servicios_solicitados"].append(nueva_solicitud)
    guardar_datos(datos)
    print(f"Has solicitado el servicio '{nombre_servicio}' correctamente.")
    
    