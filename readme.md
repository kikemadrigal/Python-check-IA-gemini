# ¿Que es Gemini-Kike?

Es un programa que se conecta a la IA de google para pasarle una imagen y que te la describa.

<img src="docs/image1.JPG" width="300" />

# Development

1. Escribe en el cmd: pip install requirements.txt

2. Ve a https://ai.google.dev/ y crea una API Key, sustituye la que hay en el archivo key.py por esa.

3. Para crear el ejecutable escribe en el cmd: 
python -m PyInstaller --windowed --onefile --icon=logo.ico --clean -y -n "gemini-kike" main.py

