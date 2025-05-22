import os
import requests
from dotenv import load_dotenv

# Cargar la clave desde el archivo .env
load_dotenv()
api_key = os.getenv("Api_key_digitalizacion")
 
# Modelo que deseas usar en OpenRouter
modelo = "openai/gpt-3.5-turbo"

# URL base de la API de OpenRouter
API_URL = "https://openrouter.ai/api/v1/chat/completions"


def chatbot_que_puedo_ofrecer():
    print("\n--- Chatbot: ¿Qué servicios puedes ofrecer? ---")
    mensaje_usuario = input("Describe tus habilidades, aficiones o lo que te gustaría ofrecer como servicio: ")

    # Construir payload
    payload = {
        "model": modelo,
        "messages": [
            {"role": "system", "content": (
                "Eres un asesor experto en ideas de servicios prácticos y creativos para una plataforma local de servico de todos los tipos ."
                "Sugiere servicios  que una persona use sus habilidades y preferencias dame 5una lista de 3 o 4 ."
            )},
            {"role": "user", "content": mensaje_usuario}
        ]
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        respuesta = response.json()

        sugerencia = respuesta["choices"][0]["message"]["content"]
        print(f"\n💡 Sugerencia del chatbot:\n{sugerencia}")
    except Exception as e:
        print("❌ Error al comunicarse con el chatbot:", str(e))
