# Bot de Telegram de Fórmula 1 de Fernando Alonso

Este es un bot de Telegram creado por [HectorCRZBQ](https://github.com/HectorCRZBQ) y [XxIMDARIOxX](https://github.com/XxIMDARIOxX) que proporciona información y entretenimiento relacionado con la Fórmula 1, centrándose en el piloto Fernando Alonso. El bot utiliza el módulo `telebot` para interactuar con la API de Telegram y ofrece diversas funcionalidades, como generar comentarios aleatorios sobre las actuaciones de Fernando Alonso, mostrar información sobre el equipo Alpine, obtener estadísticas del piloto y mucho más.

## Estructura del Código

### Gramática para Generar Comentarios Aleatorios
El bot utiliza una gramática definida en el diccionario `gramatica_comentario` para generar comentarios aleatorios sobre las actuaciones de Fernando Alonso en las carreras de Fórmula 1. La gramática está definida con etiquetas que se utilizan para construir frases de manera coherente y aleatoria.

### Funciones Principales

1. **`generar_comentario`**: Esta función toma una etiqueta inicial (`<inicio>`) y utiliza la gramática para generar un comentario aleatorio sobre la actuación de Fernando Alonso.

2. **`obtener_imagen_aleatoria`**: Devuelve una URL aleatoria de imágenes de Fernando Alonso para acompañar los comentarios.

3. **`obtener_fecha_proxima_carrera`**: Utiliza la API de Ergast para obtener la fecha y el nombre de la próxima carrera de Fórmula 1.

4. **`obtener_clasificacion_carrera_anterior`**: Utiliza la API de Ergast para obtener la clasificación de la última carrera de Fórmula 1.

5. **`obtener_ultima_publicacion_instagram`**: Utiliza la biblioteca `instaloader` para obtener la última publicación de Instagram de Fernando Alonso.

6. **`enviar_mensaje_inicial`**: Envia un mensaje inicial al inicio del bot, combinando un comentario aleatorio y una imagen aleatoria.

### Comandos de Telegram

El bot responde a varios comandos de Telegram, como `/mensaje` para obtener un nuevo comentario aleatorio, `/equipo` para obtener información sobre el equipo Alpine, `/estadisticas` para conocer las estadísticas de Fernando Alonso, y otros comandos relacionados con la Fórmula 1.

### Ejecución del Bot

El bot se inicia utilizando el token de acceso de Telegram y utiliza el módulo `telebot` para gestionar la interacción con la API de Telegram. Se mantiene en funcionamiento continuo mediante la función `bot.polling()`.

## Configuración y Uso

1. **Token de Acceso de Telegram**: Reemplace el valor de `bot_token` con el token de acceso de su bot de Telegram.

2. **API de Ergast**: El bot utiliza la API de Ergast para obtener información sobre las carreras de Fórmula 1. Asegúrese de tener una conexión a internet para acceder a esta API.

3. **Instalación de Dependencias**: Asegúrese de tener instaladas las bibliotecas necesarias ejecutando `pip install -r requirements.txt`.

4. **Ejecución del Bot**: Ejecute el script y el bot estará listo para responder a los comandos de Telegram.

## Comandos de Telegram

- **/mensaje**: Genera un nuevo comentario aleatorio sobre las actuaciones de Fernando Alonso.
- **/equipo**: Obtiene información sobre el equipo Alpine.
- **/estadisticas**: Muestra estadísticas impresionantes de Fernando Alonso.
- **/clasificacion**: Presenta la clasificación de la última carrera de Fórmula 1.
- **/temporada**: Informa sobre el estado actual de la temporada de Fórmula 1.
- **/gracias**: Agradece al bot por sus servicios.
- **/proximacarrera**: Ofrece la fecha de la próxima carrera de Fórmula 1.
- **/publicacion**: Muestra la última publicación de Fernando Alonso en Instagram.
- **/saludo**: Inicia una interacción personalizada saludando al usuario.

## Contribuciones y Problemas

Este proyecto está abierto a contribuciones. Si encuentras algún problema o tienes ideas para mejorar el bot, ¡no dudes en abrir un problema o enviar una solicitud de extracción!

---

