# Función para el chatbot que recomienda categorías
def chatbot_recomendador():
    categorias = [
        "Clases y Formación",
        "Cuidado de Personas",
        "Hogar",
        "Mascotas",
        "Bienestar y Salud",
        "Creatividad y Diseño",
        "Tecnología y Reparaciones",
        "Transporte y Mudanzas",
        "Entrenamiento u ocio"
    ]
    print("¡Hola! ¿Qué tipo de servicio buscas?")
    for idx, categoria in enumerate(categorias, start=1):
        print(f"{idx}. {categoria}")
    opcion = int(input("Selecciona una categoría por número: "))
    categoria_seleccionada = categorias[opcion - 1]
    print(f"Te recomiendo la categoría: {categoria_seleccionada}")
    return categoria_seleccionada
