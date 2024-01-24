# Traductor y Lector TTS

## Descripción
Este proyecto es una aplicación web desarrollada en Flask que utiliza la API de OpenAI para ofrecer servicios de traducción y lectura de texto. Permite a los usuarios ingresar texto en cualquier idioma y recibir una traducción al español, seguida de una conversión a texto hablado (TTS) utilizando modelos de voz avanzados.

## Características
- **Traducción de texto:** Capacidad para traducir texto de cualquier idioma al español.
- **Generación de voz:** Convierte el texto traducido en audio mediante tecnología TTS.
- **Extracción de texto desde URLs:** Permite ingresar una URL para extraer su contenido textual y procesarlo.
- **Segmentación de texto y audio:** Divide el texto en segmentos manejables para una mejor conversión de texto a voz.
- **Interfaz de usuario:** Interfaz web amigable para ingresar texto y visualizar resultados.

## Tecnologías Utilizadas
- Flask
- OpenAI API
- Pydub
- BeautifulSoup
- Bootstrap para frontend

## Instalación
Para clonar y ejecutar este proyecto, necesitarás Git y Python instalados en tu máquina. Desde tu línea de comandos:

# Clona este repositorio
```bash
$ git clone https://github.com/adri-barreda/Narrador.git
```

# Ve al directorio del repositorio
```bash
$ cd nombre-del-repositorio
```

# Instala las dependencias
```bash
$ pip install -r requirements.txt
```

## Uso
Para ejecutar la aplicación, ejecuta el siguiente comando en tu terminal:

```bash
$ python main.py
```
Abre tu navegador y visita http://localhost:81 para ver la aplicación en acción.

## Contribuciones
Las contribuciones al proyecto son bienvenidas. Si tienes ideas o mejoras, por favor crea un issue o una pull request.
