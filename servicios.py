# Función para mostrar los servicios publicados
def servicios_publicados(datos):
    print("\n--- Servicios Publicados ---")
    for usuario in datos["usuarios"]:
        if usuario["tipo_usuario"] == "colaborador":
            for servicio in usuario["servicios_publicados"]:
                print(f"\nCategoría: {servicio['categoria']}")
                print(f"Descripción: {servicio['descripcion']}")
                print(f"Correo: {servicio['correo']}")
                print(f"Provincia: {servicio['provincia']}")

# Función para publicar un servicio
def publicar_servicio(usuario, datos):
    print("\n--- Publicar Servicio ---")
    categoria = chatbot_recomendador()
    descripcion = input("Describe el servicio que quieres ofrecer: ")
    correo = input("Introduce tu correo electrónico: ")

    servicio = {
        "categoria": categoria,
        "descripcion": descripcion,
        "correo": correo,
        "provincia": usuario["provincia"]
    }
    
    usuario["servicios_publicados"].append(servicio)
    print("Servicio publicado correctamente.")
