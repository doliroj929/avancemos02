# registro.py

from datos import guardar_datos  # Importamos desde datos.py

# Función de registro de usuarios
def registrarse(datos):
    print("\n--- Registrarse ---")
    
    # Pedir el nombre de usuario
    while True:
        nombre_usuario = input("Nombre de usuario: ")
        
        # Verificar si el nombre de usuario ya existe
        if any(usuario["nombre_usuario"] == nombre_usuario for usuario in datos["usuarios"]):
            print("Este nombre de usuario ya está en uso. Por favor, elige otro.")
        else:
            break
    
    # Pedir la clave de ingreso (contraseña)
    clave_ingreso = input("Clave de ingreso (contraseña): ")
    
    # Mostrar lista de provincias para que el usuario seleccione una
    provincias = [
    "Almeria", "Cadiz", "Cordoba", "Granada", 
    "Huelva", "Jaen", "Malaga", "Sevilla"
]

    
    print("\nSelecciona tu provincia:")
    for i, provincia in enumerate(provincias, 1):
        print(f"{i}. {provincia}")
    
    # Validar que el usuario ingrese una opción válida para la provincia
    while True:
        try:
            provincia_seleccionada = int(input("Introduce el número de tu provincia: "))
            if 1 <= provincia_seleccionada <= len(provincias):
                provincia = provincias[provincia_seleccionada - 1]
                break
            else:
                print("Por favor, selecciona un número válido entre 1 y 8.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    # Pedir el correo electrónico
    correo = input("Introduce tu correo electrónico: ")

    # Crear el nuevo usuario con la provincia, correo y la clave de ingreso
    nuevo_usuario = {
        "nombre_usuario": nombre_usuario,
        "clave_ingreso": clave_ingreso,  # Guardamos la clave de ingreso
        "provincia": provincia,
        "correo": correo,  # Añadimos el correo del usuario
        "tipo_usuario": "colaborador y cliente",  # Asumimos que puede ser ambos
        "servicios_publicados": []  # De momento no tiene servicios publicados
    }
    
    datos["usuarios"].append(nuevo_usuario)
    
    # Guardamos los datos en el archivo JSON
    print(f"Guardando los datos de {nuevo_usuario['nombre_usuario']}...")
    guardar_datos(datos)  # Ahora la función guardar_datos está importada y disponible
    print(f"¡Te has registrado como colaborador y cliente en {provincia}!")
