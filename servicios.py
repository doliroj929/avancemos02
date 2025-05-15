# servicios.py

from datos import cargar_datos

def servicios_publicados():
    datos = cargar_datos()
    encontrados = False

    print("\n--- Servicios publicados por todos los usuarios ---")
    for usuario in datos["usuarios"]:
        for s in usuario.get("servicios_publicados", []):
            nombre_servicio = s.get("nombre_servicio") or s.get("categoria") or "Nombre no disponible"
            descripcion = s.get("descripcion", "Descripción no disponible")
            print(f"servio : -{nombre_servicio}-")
            print(f"descripcion : -{descripcion}-")
            print(f"usuario : -{usuario.get('nombre_usuario', 'Desconocido')}-")
            print(f"correo : -{usuario.get('correo', 'Desconocido')}-")
            print("-" * 30)
            encontrados = True

    if not encontrados:
        print("No hay servicios publicados.")

def servicios_solicitados_global():
    datos = cargar_datos()
    encontrados = False

    print("\n--- Servicios solicitados por todos los usuarios ---")
    for usuario in datos["usuarios"]:
        for s in usuario.get("servicios_solicitados", []):
            nombre_servicio = s.get("nombre_servicio") or s.get("categoria") or "Nombre no disponible"
            descripcion = s.get("descripcion", "Descripción no disponible")
            print(f"servicio solicitado : -{nombre_servicio}-")
            print(f"descripcion : -{descripcion}-")
            print(f"usuario solicitante : -{usuario.get('nombre_usuario', 'Desconocido')}-")
            print(f"correo usuario : -{usuario.get('correo', 'Desconocido')}-")
            print("-" * 30)
            encontrados = True

    if not encontrados:
        print("No hay servicios solicitados.")
