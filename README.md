# EmotionsAPI

EmotionsAPI es una API sencilla que utiliza Flask, vaderSentiment y GoogleTranslator para realizar análisis de sentimientos en cualquier idioma. Traduce el texto proporcionado al inglés y luego realiza el análisis de sentimiento.

## Características

- Traduce texto de varios idiomas al inglés usando Google Translator.
- Analiza los sentimientos utilizando el modelo vaderSentiment.
- Retorna una puntuación de sentimientos (positiva, neutral, negativa y compuesta).
- Utiliza autenticación por token.

## Instalación

### Requisitos

- Python 3.10 o superior
- Docker (si deseas usar el contenedor)
- Git

### Clonar el repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/pbrodriguezm/emotionsAPI.git
cd emotionsAPI
pip install -r requirements.txt
```

### Variables de entorno y Tokens
- Crea un archivo .env en la raíz del proyecto y define el token de autenticación:

```bash
AUTH_TOKEN=mi_token_secreto
```

### Ejecutar la API localmente
Después de instalar las dependencias y configurar el archivo .env, ejecuta el servidor Flask:

```bash
python main.py
```