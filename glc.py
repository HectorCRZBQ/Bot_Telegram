import telebot 
from telebot import types  
import random
import requests
import instaloader #Para publicaciones de Instagram
from io import BytesIO #Mostrar la imagen


# Token de acceso a tu bot de Telegram
bot_token = '6752175083:AAE4wliLk4ZKBbKJjHwoMEq0tXQtH071Rw0'
chat_id = '-4025175766'

gramatica_comentario = {
    "<inicio>": ["<frase> <hashtags> <lugar>"],
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
        "ante la sorpresa de los espectadores",
        "demostrando su habilidad en la pista",
        "convirtiéndose en el centro de atención del día",
        "en una carrera llena de emoción y tensión",
        "en un emocionante duelo hasta el final",
        "mostrando un desempeño excepcional",
        "dando una lección magistral de manejo",
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
        "#F1", "#Carrera", "#Emoción", "#Automovilismo", "#Velocidad", "#FernandoAlonso", "#Formula1", "#Asturias", "#Campeón", "#Motor",
        "#Adrenalina", "#Alpine", "#Piloto", "#GrandesPremios", "#Español", "#CarreraHistorica", "#PasiónPorLasRuedas",
    ],
    "<lugar>": ["(Madrid)", "(Barcelona)", "(Sao Paulo)", "(Monza)", "(Silverstone)", "(Montecarlo)"],
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
        "https://i.etsystatic.com/22166537/r/il/0d5136/3524886263/il_340x270.3524886263_kkxz.jpg",
        "https://estaticos-cdn.prensaiberica.es/clip/5c3818fb-abb1-498f-aff3-c0fee7713f45_16-9-aspect-ratio_default_0.jpg",
        "https://fotografias.lasexta.com/clipping/cmsimages02/2023/04/03/028237A5-68DE-4E7A-921E-F47D2C5CFC32/fernando-alonso-lewis-hamilton_98.jpg?crop=4095,2304,x1,y0&width=1900&height=1069&optimize=low&format=webply",
        "https://editorialtelevisa.brightspotcdn.com/dims4/default/0a9d687/2147483647/strip/true/crop/627x353+9+0/resize/1000x563!/quality/90/?url=https%3A%2F%2Fk2-prod-editorial-televisa.s3.us-east-1.amazonaws.com%2Fbrightspot%2Fwp-content%2Fuploads%2F2018%2F06%2FGuapos-de-la-F1-Fernando-Alonso.jpg"
    ]
    return random.choice(urls)

# Función para obtener la fecha de la próxima carrera de F1
def obtener_fecha_proxima_carrera():
    try:
        url = "https://ergast.com/api/f1/current/next.json"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            race_name = data['MRData']['RaceTable']['Races'][0]['raceName']
            date = data['MRData']['RaceTable']['Races'][0]['date']
            return f"La próxima carrera de Fórmula 1 es {race_name}, que se llevará a cabo el {date}. ¡No te la pierdas!"
        else:
            print(f"Error en la solicitud a la API. Código de estado: {response.status_code}")
            print(response.text)  # Imprimir el contenido de la respuesta para diagnosticar problemas
            return "Lo siento, no pude obtener información sobre la próxima carrera en este momento."

    except Exception as e:
        print(f"Error al procesar la solicitud a la API: {str(e)}")
        return "Lo siento, ocurrió un error al obtener información sobre la próxima carrera."

# Función para obtener la clasificación de la última carrera
def obtener_clasificacion_carrera_anterior():
    try:
        # Obtener el ID de la última carrera
        url_ultima_carrera = "https://ergast.com/api/f1/current/last/results.json"
        response_ultima_carrera = requests.get(url_ultima_carrera)

        if response_ultima_carrera.status_code == 200:
            data_ultima_carrera = response_ultima_carrera.json()
            race_id = data_ultima_carrera['MRData']['RaceTable']['Races'][0]['round']

            # Obtener la clasificación de la última carrera
            url_clasificacion = f"https://ergast.com/api/f1/current/{race_id}/results.json"
            response_clasificacion = requests.get(url_clasificacion)

            if response_clasificacion.status_code == 200:
                data_clasificacion = response_clasificacion.json()
                clasificacion_texto = "Clasificación de la última carrera:\n"

                for result in data_clasificacion['MRData']['RaceTable']['Races'][0]['Results']:
                    position = result['position']
                    driver_name = result['Driver']['givenName'] + " " + result['Driver']['familyName']
                    constructor = result['Constructor']['name']
                    clasificacion_texto += f"{position}. {driver_name} ({constructor})\n"

                return clasificacion_texto
            else:
                print(f"Error en la solicitud de clasificación. Código de estado: {response_clasificacion.status_code}")
                print(response_clasificacion.text)
                return "Lo siento, no pude obtener la clasificación de la última carrera en este momento."
        else:
            print(f"Error en la solicitud de la última carrera. Código de estado: {response_ultima_carrera.status_code}")
            print(response_ultima_carrera.text)
            return "Lo siento, no pude obtener información sobre la última carrera en este momento."

    except Exception as e:
        print(f"Error al procesar la solicitud a la API: {str(e)}")
        return "Lo siento, ocurrió un error al obtener la clasificación de la última carrera."

# Función para obtener la última publicación de Fernando Alonso en Instagram
def obtener_ultima_publicacion_instagram():
    try:
        loader = instaloader.Instaloader()
        perfil = instaloader.Profile.from_username(loader.context, "fernandoalo_oficial")

        for post in perfil.get_posts():
            # Obtener la URL de la última publicación
            url_ultima_publicacion = post.url

            # Obtener la imagen de la última publicación
            response = requests.get(post.url)
            image_bytes = BytesIO(response.content)
            return image_bytes

    except Exception as e:
        print(f"Error al obtener la última publicación de Instagram: {str(e)}")
        return "Lo siento, no pude obtener la última publicación en este momento."


def enviar_mensaje_inicial():
    message = generar_comentario()
    image_url = obtener_imagen_aleatoria()
    
    # Enviar el comentario aleatorio y la imagen
    bot.send_message(chat_id, message)
    bot.send_photo(chat_id, requests.get(image_url).content)


# Iniciar el bot de Telegram
bot = telebot.TeleBot(token=bot_token)

#Enviamos el primer mensaje
enviar_mensaje_inicial()

# Comando de ayuda actualizado
@bot.message_handler(commands=['ayuda'])
def ayuda(message):
    ayuda_texto = "Este bot está hecho por HectorCRZBQ y XxIMDARIOxX \n" \
                  "¡Hola! Soy un bot de Fórmula 1 de Fernando Alonso. \n" \
                  "Aquí tienes algunos comandos que puedes usar: \n" \
                  " - /mensaje - Generar un nuevo mensaje sobre F1 \n" \
                  " - /equipo - Obtener información sobre el equipo de Alonso \n" \
                  " - /estadisticas - Estado actual de la temporada de F1 \n" \
                  " - /clasificacion - Tabla de clasificación de la anterior carrera \n"\
                  " - /proximacarrera - Fecha proxima carrera de F1 \n" \
                  " - /gracias - Agradecer al bot por su servicio \n" \
                  " - /saludo - Saludo personalizado del mejor piloto ;) \n"\
                  " - /publicacion - Ultima publicacion subida por Fernando \n"
    bot.send_message(message.chat.id, ayuda_texto)    




# Comando para generar un nuevo mensaje sobre F1
@bot.message_handler(commands=['mensaje'])
def nuevo_mensaje_f1(message):
    nuevo_comentario = generar_comentario()
    image_url = obtener_imagen_aleatoria()
    bot.send_message(message.chat.id, nuevo_comentario)
    bot.send_photo(message.chat.id, requests.get(image_url).content)


# Comando para mostrar el equipo en el que esta Fernando Alonso
@bot.message_handler(commands=['equipo'])
def informacion_equipo(message):
    equipo_texto = "Fernando Alonso actualmente compite para el equipo Alpine en la Fórmula 1. " \
                   "Alpine es un equipo de carreras con una rica historia y una fuerte presencia en el automovilismo."
    bot.send_message(message.chat.id, equipo_texto)


# Comando para mostrar las estadisticas de Fernando Alonso
@bot.message_handler(commands=['estadisticas'])
def estadisticas_alonso(message):
    estadisticas_texto = "Fernando Alonso es uno de los pilotos más exitosos de la Fórmula 1. " \
                         "Aquí tienes algunas de sus estadísticas impresionantes:\n" \
                         "- Dos veces campeón del mundo (2005, 2006)\n" \
                         "- 32 victorias en Grandes Premios\n" \
                         "- 97 podios\n" \
                         "- 22 poles\n" \
                         "- Conduce para el equipo Alpine\n" \
                         "¡Un verdadero ícono de la F1!"
    bot.send_message(message.chat.id, estadisticas_texto)



# Comando para obtener la clasificación de la última carrera
@bot.message_handler(commands=['clasificacion'])
def clasificacion_carrera_anterior(message):
    clasificacion_texto = obtener_clasificacion_carrera_anterior()
    bot.send_message(message.chat.id, clasificacion_texto)



# Comando para obtener el estado actual de la temporada de F1
@bot.message_handler(commands=['temporada'])
def estado_temporada(message):
    temporada_texto = "La temporada actual de Fórmula 1 está en curso. Para obtener información detallada sobre " \
                      "la clasificación, los resultados y más, puedes visitar sitios web especializados como " \
                      "[F1 Official](https://www.formula1.com/). ¡Disfruta de la temporada!"
    bot.send_message(message.chat.id, temporada_texto, parse_mode='Markdown')



# Comando para agradecer al bot
@bot.message_handler(commands=['gracias'])
def agradecimiento(message):
    bot.send_message(message.chat.id, "¡De nada! ¡Estoy aquí para proporcionar información y entretenimiento sobre Fórmula 1!")



# Comando para obtener los datos de la próxima carrera de F1
@bot.message_handler(commands=['proximacarrera'])
def proxima_carrera(message):
    datos_proxima_carrera = obtener_fecha_proxima_carrera()
    bot.send_message(message.chat.id, datos_proxima_carrera)



# Comando para obtener la última publicación de Fernando Alonso en Instagram
@bot.message_handler(commands=['publicacion'])
def obtener_ultima_publicacion_comando(message):
    ultima_publicacion_image = obtener_ultima_publicacion_instagram()
    bot.send_photo(message.chat.id, ultima_publicacion_image)



# Comando de saludo personalizado
@bot.message_handler(commands=['saludo'])
def saludo_personalizado(message):
    markup = types.ForceReply(selective=False)
    bot.send_message(message.chat.id, "¡Hola! ¿Cómo te llamas?", reply_markup=markup)
    
# Manejador para obtener el nombre del usuario
@bot.message_handler(content_types=['text'])
def obtener_nombre(message):
    if message.reply_to_message and message.reply_to_message.text == "¡Hola! ¿Cómo te llamas?":
        nombre = message.text.strip()

        if nombre:
            saludo_personalizado = f"¡Hola, {nombre}! ¡Espero que estés teniendo un gran día! Fernando Alonso"
            bot.send_message(message.chat.id, saludo_personalizado)
        else:
            bot.send_message(message.chat.id, "Por favor, ingresa un nombre válido.")



# Iniciar el bot y mantenerlo en funcionamiento
bot.polling()