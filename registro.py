# registro.py

from datos import guardar_datos

PROVINCIAS_DISPONIBLES = [
    "Almería",
    "Cádiz",
    "Córdoba",
    "Granada",
    "Huelva",
    "Jaén",
    "Málaga",
    "Sevilla"
]

def registrarse(datos):
    nombre = input("Nombre de usuario: ")
    
    # Verificar si el usuario ya existe
    for usuario in datos:
        if usuario.get("nombre_usuario") == nombre:
            print("Ese nombre ya está en uso.")
            return

    contrasena = input("Contraseña: ")
    email = input("Email: ")

    print("\nSelecciona una provincia:")
    provincias = [
        "Almería", "Cádiz", "Córdoba", "Granada", 
        "Huelva", "Jaén", "Málaga", "Sevilla"
    ]
    for idx, provincia in enumerate(provincias, 1):
        print(f"{idx}. {provincia}")
    try:
        provincia_idx = int(input("Elige una provincia (número del 1 al 8): ")) - 1
        if 0 <= provincia_idx < len(provincias):
            provincia = provincias[provincia_idx]
        else:
            print("Número inválido. Registro cancelado.")
            return
    except ValueError:
        print("Entrada inválida. Registro cancelado.")
        return

    descripcion = input("Descripción personal (opcional): ")

    nuevo_usuario = {
        "nombre_usuario": nombre,
        "contrasena": contrasena,
        "email": email,
        "provincia": provincia,
        "descripcion": descripcion,
        "servicios": [],
        "solicitudes": []
    }

    datos.append(nuevo_usuario)  # Añade el nuevo usuario a la lista

    from datos import guardar_datos
    guardar_datos(datos)

    print("¡Registro exitoso!")



