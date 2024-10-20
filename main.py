from flask import Flask, jsonify, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Cargar variables de entorno desde .env
load_dotenv()

# Inicializar el analizador de sentimientos
analyzer = SentimentIntensityAnalyzer()

# Obtener el token de autenticación desde .env
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

# Ruta para la raíz
@app.route('/')
def home():
    return "Bienvenido al análisis de sentimientos. Usa GET /sentiment/<texto> para analizar el estado de ánimo."

# Ruta para analizar el estado de ánimo con traducción al inglés y autenticación
@app.route('/sentiment/<text>')
def sentiment(text):
    # Obtener el token de la solicitud
    token = request.headers.get('Authorization')

    # Verificar si el token es correcto
    if token != f"Bearer {AUTH_TOKEN}":
        return jsonify({'error': 'No autorizado. Token inválido.'}), 401

    try:
        # Traducir el texto de cualquier idioma a inglés usando GoogleTranslator
        translation = GoogleTranslator(source='auto', target='en').translate(text)

        # Analizar el estado de ánimo en inglés
        sentiment_score = analyzer.polarity_scores(translation)

        return jsonify({
            'original_text': text,
            'translated_text': translation,
            'sentiment': sentiment_score
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Hubo un problema con la traducción o el análisis de sentimientos.'
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
