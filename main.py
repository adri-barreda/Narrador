from flask import Flask, request, render_template, send_file, redirect, url_for
from openai import OpenAI
import os
from pydub import AudioSegment  # Necesitarás instalar pydub
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Crear el directorio para los archivos de audio si no existe
if not os.path.exists('static/audio'):
  os.makedirs('static/audio')


@app.route('/')
def index():
  return render_template('index.html')


def translate_to_spanish(api_key, text):
  client = OpenAI(api_key=api_key)
  response = client.chat.completions.create(
      model="gpt-3.5-turbo-16k",
      messages=[{
          "role":
          "system",
          "content":
          "Eres un traductor especializado en traducir de cualquier idioma al español. Traducirás cualquier cosa a español de España. Haz la mejor traducción que seas capaz de hacer."
      }, {
          "role": "user",
          "content": text
      }],
      max_tokens=8000,  # Ajustar el máximo de tokens aquí
  )
  translated_text = response.choices[0].message.content

  # Imprimir el texto traducido completo
  print("Texto traducido:", translated_text)

  return translated_text


def split_text(text, max_duration=100, words_per_second=2.5):
  if not text:
    return []  # Devuelve una lista vacía si el texto es None o vacío

  words = text.split()
  max_words = int(max_duration * words_per_second)
  segments = [
      ' '.join(words[i:i + max_words]) for i in range(0, len(words), max_words)
  ]

  print(f"Texto dividido en {len(segments)} segmentos.")
  return segments


def generate_tts_for_segments(api_key, segments):
  """
  Genera archivos de audio para cada segmento de texto.
  """
  audio_paths = []
  for i, segment in enumerate(segments):
    audio_file_path = f"static/audio/output_{i}.mp3"
    response = OpenAI(api_key=api_key).audio.speech.create(
        model="tts-1",
        voice="echo",
        input=segment,
    )
    response.stream_to_file(audio_file_path)

    # Verificar la duración del segmento de audio
    segment_audio = AudioSegment.from_mp3(audio_file_path)
    segment_duration = len(segment_audio) / 1000  # Duración en segundos
    print(f"Segmento {i} generado, duración: {segment_duration} segundos")

    audio_paths.append(audio_file_path)

  return audio_paths


def merge_audio_files(file_paths):
  combined = AudioSegment.empty()
  for file_path in file_paths:
    segment = AudioSegment.from_mp3(file_path)
    print(f"Combinando archivo: {file_path}, duración: {len(segment)} ms")
    combined += segment
  combined.export("static/audio/combined_output.mp3", format="mp3")
  return "static/audio/combined_output.mp3"


# Modifica tu función translate_and_read para manejar segmentos
@app.route('/translate_and_read', methods=['POST'])
def translate_and_read():
  api_key = request.form['api_key']
  user_input = request.form['text']
  translated_text = translate_to_spanish(api_key, user_input)

  # Verificar que el texto traducido no sea None
  if translated_text is None:
    print("Error: El texto traducido es None")
    return "Error en la traducción", 500  # O manejar el error de forma adecuada

  print(
      f"Longitud del texto traducido: {len(translated_text.split())} palabras")

  segments = list(split_text(translated_text))
  print(f"Número de segmentos generados: {len(segments)}")
  audio_paths = generate_tts_for_segments(api_key, segments)
  combined_audio_path = merge_audio_files(audio_paths)

  return redirect(url_for('play_audio', audio_path=combined_audio_path))


@app.route('/play_audio')
def play_audio():
  return render_template('play_audio.html')


def dividir_texto_en_segmentos(texto, max_palabras=125):
  palabras = texto.split()
  segmentos = [
      ' '.join(palabras[i:i + max_palabras])
      for i in range(0, len(palabras), max_palabras)
  ]
  return segmentos


@app.route('/url_page')
def url_page():
  return render_template('url.html')


def scrape_url(url):
  try:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = ' '.join(p.get_text().strip() for p in soup.find_all('p'))
    return text
  except Exception as e:
    print(f"Error al scrapear URL: {e}")
    return None


@app.route('/process_url', methods=['POST'])
def process_url():
  api_key = request.form['api_key']
  url = request.form['url']
  print(f"Procesando URL: {url}")

  scraped_content = scrape_url(url)
  if scraped_content:
    translated_text = translate_to_spanish(api_key, scraped_content)
    print(f"Texto traducido: {translated_text}")

    segments = split_text(translated_text)
    print(f"Número de segmentos generados: {len(segments)}")

    audio_paths = generate_tts_for_segments(api_key, segments)
    combined_audio_path = merge_audio_files(audio_paths)

    return redirect(url_for('play_audio', audio_path=combined_audio_path))
  else:
    return "Error al procesar la URL", 500


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
