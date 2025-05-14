# usuario.py

# Funciones relacionadas con la gestión de los usuarios

def registrar_usuario(datos, nombre_usuario, provincia, tipo_usuario):
    """
    Registra un nuevo usuario en el sistema.
    :param datos: Datos del sistema que contienen la lista de usuarios.
    :param nombre_usuario: Nombre de usuario del nuevo usuario.
    :param provincia: Provincia del usuario.
    :param tipo_usuario: Tipo de usuario ('colaborador' o 'cliente').
    """
    nuevo_usuario = {
        "nombre_usuario": nombre_usuario,
        "provincia": provincia,
        "tipo_usuario": tipo_usuario,
        "servicios_publicados": []
    }
    datos["usuarios"].append(nuevo_usuario)
    print(f"¡Te has registrado como {tipo_usuario} en {provincia}!")


def obtener_usuario_por_nombre(datos, nombre_usuario):
    """
    Busca un usuario por su nombre de usuario.
    :param datos: Datos del sistema que contienen la lista de usuarios.
    :param nombre_usuario: Nombre de usuario a buscar.
    :return: El usuario encontrado o None si no se encuentra.
    """
    return next((usuario for usuario in datos["usuarios"] if usuario["nombre_usuario"] == nombre_usuario), None)

# Función para iniciar sesión


def iniciar_sesion(datos):
    nombre_usuario = input("Nombre de usuario: ")
    clave = input("Clave de ingreso: ")

    # Verificación de credenciales
    for usuario in datos["usuarios"]:
        if usuario["nombre_usuario"] == nombre_usuario and usuario["clave_ingreso"] == clave:
            print(f"¡Bienvenido, {nombre_usuario}!")
            return nombre_usuario  # Devolvemos el nombre de usuario al menú principal
    print("Usuario o clave incorrectos.")
    return None


# usuario.py

# usuario.py

def registrar_servicio(datos, nombre_usuario):
    # Llamamos a la función para registrar un nuevo servicio
    servicio = input("Introduce el nombre del servicio: ")
    descripcion = input("Introduce la descripción del servicio: ")

    # Buscar al usuario en la base de datos
    for usuario in datos["usuarios"]:
        if usuario["nombre_usuario"] == nombre_usuario:
            # Añadir el servicio a la lista de servicios publicados
            usuario["servicios_publicados"].append({
                "servicio": servicio,
                "descripcion": descripcion
            })
            print(f"Servicio '{servicio}' registrado correctamente.")
            return
    
    print("Usuario no encontrado.")


    
def ver_servicios_publicados(datos, nombre_usuario):
    for usuario in datos["usuarios"]:
        if usuario["nombre_usuario"] == nombre_usuario:
            if usuario["servicios_publicados"]:
                print("Servicios publicados:")
                for servicio in usuario["servicios_publicados"]:
                    print(f"- {servicio['servicio']}: {servicio['descripcion']}")
            else:
                print("No has publicado servicios aún.")
            return
    print("Usuario no encontrado.")
    
def ver_servicios_solicitados(datos, nombre_usuario):
    for usuario in datos["usuarios"]:
        if usuario["nombre_usuario"] == nombre_usuario:
            if usuario["servicios_solicitados"]:
                print("Servicios solicitados:")
                for servicio in usuario["servicios_solicitados"]:
                    print(f"- {servicio['servicio']}: {servicio['descripcion']}")
            else:
                print("No has solicitado servicios aún.")
            return
    print("Usuario no encontrado.")
    
    # usuario.py

def solicitar_servicio(datos, nombre_usuario):
    # Mostrar los servicios disponibles
    print("Servicios disponibles para solicitar:")
    for usuario in datos["usuarios"]:
        for servicio in usuario["servicios_publicados"]:
            print(f"- {servicio['servicio']}: {servicio['descripcion']}")
    
    # Elegir un servicio para solicitar
    servicio_solicitado = input("Introduce el nombre del servicio que deseas solicitar: ")

    # Buscar el servicio y añadirlo a los servicios solicitados del usuario
    for usuario in datos["usuarios"]:
        if usuario["nombre_usuario"] == nombre_usuario:
            for servicio in usuario["servicios_publicados"]:
                if servicio_solicitado == servicio["servicio"]:
                    usuario["servicios_solicitados"].append(servicio)
                    print(f"Servicio '{servicio_solicitado}' solicitado correctamente.")
                    return
    
    print(f"Servicio '{servicio_solicitado}' no encontrado.")

# usuario.py

def cerrar_sesion():
    print("Sesión cerrada con éxito.")
    # Aquí se puede implementar la lógica para regresar al menú principal
    menu_principal()  # Regresar al menú principal
