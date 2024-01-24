Traductor y Lector TTS
Descripción
Este proyecto es una aplicación web desarrollada en Flask que utiliza la API de OpenAI para ofrecer servicios de traducción y lectura de texto. Permite a los usuarios ingresar texto en cualquier idioma y recibir una traducción al español, seguida de una conversión a texto hablado (TTS) utilizando modelos de voz avanzados.

Características
Traducción de texto: Capacidad para traducir texto de cualquier idioma al español.
Generación de voz: Convierte el texto traducido en audio mediante tecnología TTS.
Extracción de texto desde URLs: Permite ingresar una URL para extraer su contenido textual y procesarlo.
Segmentación de texto y audio: Divide el texto en segmentos manejables para una mejor conversión de texto a voz.
Interfaz de usuario: Interfaz web amigable para ingresar texto y visualizar resultados.
Tecnologías Utilizadas
Flask
OpenAI API
Pydub
BeautifulSoup
Bootstrap para frontend
Instalación
Clona el repositorio:
bash
Copy code
git clone [URL del repositorio]
Instala las dependencias:
Copy code
pip install -r requirements.txt
Configura tus credenciales de la API de OpenAI en un archivo .env o como variables de entorno.
Uso
Para ejecutar la aplicación:

css
Copy code
python main.py
Accede a la interfaz web a través de http://localhost:81.

Contribuciones
Las contribuciones al proyecto son bienvenidas. Si tienes ideas o mejoras, por favor crea un issue o una pull request.

Licencia
Este proyecto está bajo la licencia [especificar licencia].