# registro.py

from datos import guardar_datos

def registrarse(datos):
    print("\n--- Registrarse ---")
    print("Para volver al menú principal en cualquier momento, deja el campo vacío y presiona Enter.")

    while True:
        nombre_usuario = input("Nombre de usuario (vacío para volver): ")
        if nombre_usuario == "":
            print("Volviendo al menú principal...")
            return

        if any(u["nombre_usuario"] == nombre_usuario for u in datos["usuarios"]):
            print("Este nombre de usuario ya está en uso. Por favor, elige otro.")
        else:
            break

    clave_ingreso = input("Clave de ingreso (vacío para volver): ")
    if clave_ingreso == "":
        print("Volviendo al menú principal...")
        return

    provincias = ["Almería", "Cádiz", "Córdoba", "Granada", "Huelva", "Jaén", "Málaga", "Sevilla"]
    print("\nSelecciona tu provincia:")
    for i, provincia in enumerate(provincias, 1):
        print(f"{i}. {provincia}")

    while True:
        provincia_input = input("Introduce el número de tu provincia (vacío para volver): ")
        if provincia_input == "":
            print("Volviendo al menú principal...")
            return
        try:
            provincia_num = int(provincia_input)
            if 1 <= provincia_num <= len(provincias):
                provincia = provincias[provincia_num - 1]
                break
            else:
                print("Número inválido, intenta de nuevo.")
        except ValueError:
            print("Introduce un número válido.")

    correo = input("Introduce tu correo electrónico (vacío para volver): ")
    if correo == "":
        print("Volviendo al menú principal...")
        return

    nuevo_usuario = {
        "nombre_usuario": nombre_usuario,
        "clave_ingreso": clave_ingreso,
        "provincia": provincia,
        "correo": correo,
        "tipo_usuario": "colaborador y cliente",
        "servicios_publicados": [],
        "servicios_solicitados": []
    }

    datos["usuarios"].append(nuevo_usuario)
    guardar_datos(datos)
    print(f"¡Te has registrado como colaborador y cliente en {provincia}!")
