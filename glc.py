import telebot
import random
import requests
import time

# Token de acceso de tu bot de Telegram
bot_token = '6752175083:AAE4wliLk4ZKBbKJjHwoMEq0tXQtH071Rw0'
chat_id = '-4025175766'

gramatica_comentario = {
    "<inicio>": ["<frase> <hashtags>"],
    "<frase>": [
        "<sujeto> <verbo> <complemento> <complemento_extra> <complemento_final>",
        "<sujeto> <verbo> <complemento> y <sujeto> <verbo> <complemento_extra> <complemento_final>",
        "<sujeto> <verbo> <complemento> en <lugar> <complemento_extra> <complemento_final>",
        "<sujeto> <verbo> <complemento> a <sujeto> <complemento_extra> <complemento_final>",
    ],
    "<sujeto>": ["El Nano", "Alonso", "Fernando Alonso", "El alonsista", "El piloto asturiano"],
    "<verbo>": ["gana", "remonta", "avanza", "se clasifica", "impresiona", "conquista"],
    "<complemento>": [
        "el Gran Premio de Arabia",
        "en Mónaco",
        "por los pelos en la última vuelta",
        "con una maniobra impresionante",
        "en una actuación espectacular",
        "sorprendiendo a todos los fanáticos",
        "en una carrera histórica",
        "de manera brillante",
        "con un rendimiento impecable",
        "en una demostración de habilidad excepcional",
    ],
    "<complemento_extra>": [
        "ante la sorpresa de todos los espectadores",
        "demostrando su habilidad en la pista",
        "convirtiéndose en el centro de atención del día",
        "en una carrera llena de emoción y tensión",
        "en un emocionante duelo hasta el final",
        "mostrando un desempeño excepcional",
        "dando una lección de manejo",
        "haciendo historia en la F1",
        "sobrepasando todas las expectativas",
        "en un acto de valentía y determinación",
    ],
    "<complemento_final>": [
        "en una jornada que quedará grabada en la memoria de los aficionados.",
        "convirtiéndose en el favorito del público.",
        "dejando a todos boquiabiertos.",
        "para la alegría de sus seguidores.",
        "demostrando por qué es una leyenda de la Fórmula 1.",
        "demostrando su indudable talento en la pista.",
        "mostrando que es imparable.",
        "dejando una marca imborrable en la historia de la F1.",
        "en una actuación legendaria que perdurará en el tiempo.",
    ],
    "<hashtags>": [
        "#F1", "#Carrera", "#Emocionante", "#Automovilismo", "#Velocidad", "#FernandoAlonso", "#Formula1", "#33?", "#Asturias", "#Campeón", "#Motor",
        "#Adrenalina", "#Alpine", "#Emoción", "#Piloto", "#GrandesPremios", "#Español",
    ],
    "<lugar>": ["Madrid", "Barcelona", "Sao Paulo", "Monza", "Silverstone", "Montecarlo"],
}

# Función para generar un comentario aleatorio
def generar_comentario(simbolo="<inicio>"):
    if simbolo not in gramatica_comentario:
        return simbolo

    produccion = random.choice(gramatica_comentario[simbolo])
    return " ".join(generar_comentario(comp) for comp in produccion.split())

# Función para obtener una imagen aleatoria
def obtener_imagen_aleatoria():
    urls = [
        "https://www.estadiodeportivo.com/imagenes/20a08fcc-99f4-47f0-82ae-2207596c3929_1200x680.jpeg",
        "https://pbs.twimg.com/profile_images/1474390843310186502/yCmv-bQh_400x400.jpg",
        "https://i.etsystatic.com/22166537/r/il/0d5136/3524886263/il_340x270.3524886263_kkxz.jpg"
    ]
    return random.choice(urls)

# Función para obtener la fecha de la próxima carrera de Fórmula 1
def obtener_fecha_proxima_carrera():
    url = "https://ergast.com/api/f1/current/next.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        race_name = data['MRData']['RaceTable']['Races'][0]['raceName']
        date = data['MRData']['RaceTable']['Races'][0]['date']
        return f"La próxima carrera de Fórmula 1 es {race_name}, que se llevará a cabo el {date}. ¡No te la pierdas!"
    else:
        return "Lo siento, no pude obtener información sobre la próxima carrera en este momento."

# Función para enviar un mensaje al grupo
def enviar_mensaje_al_grupo():
    message = generar_comentario()
    image_url = obtener_imagen_aleatoria()
    bot.send_message(chat_id, message)
    bot.send_photo(chat_id, requests.get(image_url).content)

# Función para enviar un saludo
def enviar_saludo():
    saludo = "¡Hola a todos! ¡Espero que estén teniendo un gran día!"
    bot.send_message(chat_id, saludo)

# Iniciar el bot de Telegram
bot = telebot.TeleBot(token=bot_token)

# Uso de las funciones
enviar_mensaje_al_grupo()
time.sleep(5)  # Espera unos segundos antes de enviar el saludo
enviar_saludo()

# Obtener información de la próxima carrera y enviarla al grupo
informacion_proxima_carrera = obtener_fecha_proxima_carrera()
bot.send_message(chat_id, informacion_proxima_carrera)

# Iniciar el bot y mantenerlo en funcionamiento
bot.polling()