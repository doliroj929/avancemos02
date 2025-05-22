from datos import guardar_datos

def buscar_usuario(datos, nombre_usuario):
    for usuario in datos:
        if usuario.get("nombre_usuario") == nombre_usuario:
            return usuario
    return None

def iniciar_sesion(datos):
    nombre = input("Usuario: ").strip()
    contrasena = input("Contraseña: ").strip()

    usuario = buscar_usuario(datos, nombre)
    if usuario and usuario.get("contrasena") == contrasena:
        print(f"Bienvenido, {nombre}!")
        return nombre
    else:
        print("No coincide usuario o contraseña.")
        return None

def registrar_servicio(datos, nombre_usuario):
    usuario = buscar_usuario(datos, nombre_usuario)
    if usuario is None:
        print("Usuario no encontrado.")
        return

    titulo = input("Título del servicio: ").strip()
    descripcion = input("Descripción del servicio: ").strip()

    nuevo_servicio = {
        "titulo": titulo,
        "descripcion": descripcion
    }

    usuario.setdefault("servicios", []).append(nuevo_servicio)
    guardar_datos(datos)
    print("¡Servicio publicado correctamente!")

def solicitar_servicio(datos, nombre_usuario):
    usuario_solicitante = buscar_usuario(datos, nombre_usuario)
    if usuario_solicitante is None:
        print("Usuario no encontrado.")
        return

    print("\nIntroduce el nombre del servicio que quieres solicitar:")
    servicio_ingresado = input().strip()

    solicitud = {
        "servicio solicitado": servicio_ingresado,
        "solicitado por": nombre_usuario
    }

    # Añadir la solicitud a la lista de solicitudes del usuario
    usuario_solicitante.setdefault("servicios_solicitados", []).append(solicitud)
    
    from datos import guardar_datos
    guardar_datos(datos)

    print(f"✅ Has solicitado el servicio '{servicio_ingresado}' correctamente.")


def ver_servicios_publicados(datos, nombre_usuario):
    usuario = buscar_usuario(datos, nombre_usuario)
    if not usuario or not usuario.get("servicios"):
        print("No tienes servicios publicados.")
        return

    print("\nTus servicios publicados:")
    for s in usuario["servicios"]:
        nombre = s.get("titulo") or "Nombre no disponible"
        descripcion = s.get("descripcion", "Descripción no disponible")
        print(f"- {nombre}: {descripcion}")

def ver_servicios_solicitados(datos, nombre_usuario):
    usuario = buscar_usuario(datos, nombre_usuario)
    if not usuario or not usuario.get("servicios_solicitados"):
        print("No tienes servicios solicitados.")
        return

    print("\nTus servicios solicitados:")
    for idx, s in enumerate(usuario["servicios_solicitados"], 1):
        servicio = s.get("servicio solicitado", s.get("titulo", "Servicio sin nombre"))
        solicitante = s.get("solicitado por", nombre_usuario)
        print(f"{idx}. servicio solicitado : {servicio}")
        print(f"   solicitado por : {solicitante}\n")

        
        
def ver_servicios_publicados_global(datos):
    print("\n--- Servicios publicados por todos los usuarios ---")
    servicios_publicados = []
    for usuario in datos:
        for servicio in usuario.get("servicios", []):
            servicios_publicados.append((usuario["nombre_usuario"], servicio))

    if not servicios_publicados:
        print("No hay servicios publicados aún.")
        return

    for idx, (usuario, servicio) in enumerate(servicios_publicados, 1):
        titulo = servicio.get("titulo", "Sin título")
        descripcion = servicio.get("descripcion", "Sin descripción")
        print(f"{idx}. {titulo} - {descripcion} (Publicado por: {usuario})")

def ver_servicios_solicitados_global(datos):
    todas_solicitudes = []
    for usuario in datos:
        solicitudes = usuario.get("servicios_solicitados", [])
        for solicitud in solicitudes:
            todas_solicitudes.append({
                "servicio solicitado": solicitud.get("servicio solicitado", "Sin nombre"),
                "solicitado por": solicitud.get("solicitado por", usuario.get("nombre_usuario", "Desconocido"))
            })

    if not todas_solicitudes:
        print("No hay servicios solicitados por ningún usuario.")
        return

    print("\n--- Servicios solicitados por todos los usuarios ---")
    for idx, s in enumerate(todas_solicitudes, 1):
        print(f"{idx}. servicio solicitado : {s['servicio solicitado']}")
        print(f"   solicitado por : {s['solicitado por']}\n")

