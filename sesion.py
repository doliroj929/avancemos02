# sesion.py

# sesion.py

# Función para iniciar sesión
def iniciar_sesion(datos):
    print("\n--- Iniciar sesión ---")
    nombre_usuario = input("Nombre de usuario: ")
    clave_ingreso = input("Clave de ingreso: ")

    # Buscar el usuario en los datos
    usuario = next((usuario for usuario in datos["usuarios"] if usuario["nombre_usuario"] == nombre_usuario), None)

    if usuario:
        # Verificar la clave de ingreso
        if usuario["clave_ingreso"] == clave_ingreso:
            print(f"¡Bienvenido, {usuario['nombre_usuario']}!")
            # Aquí podemos redirigir al menú del usuario
            from menu import menu_usuario  # Importación local para evitar importación circular
            menu_usuario(usuario, datos)
        else:
            print("Clave de ingreso incorrecta. Intenta nuevamente.")
    else:
        print("Usuario no encontrado. Por favor, regístrate primero.")

