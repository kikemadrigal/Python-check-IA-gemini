# Documentación: https://github.com/google-gemini/gemini-api-cookbook/
#1 instalamos enl api de gemini con  pip install google-generativeai: https://pypi.org/project/google-generativeai/
#2 vamos a por la clave a https://ai.google.dev/
import google.generativeai as gai
import key

gai.configure(api_key=key.clave)
model=gai.GenerativeModel(model_name="gemini-pro")

#Consulta simple

consulta="Dibujame en ascii otro logotipo del lenguaje de programación python"
response=model.generate_content(consulta)
print(response.text)

#Varias consultas
"""
consultas=[
    "¿Cual es la capital de Francia?",
    "¿Cual es la capital de Alemania?",
    "¿Cual es la capital de Argentina?",
    "¿Cual es la capital de Brasil?",
    "¿Cual es la capital de Estados Unidos?",
    "¿Cual es la capital de Canada?"
]
responses=model.generate_content(consultas)
for respuesta in responses:
    print(respuesta.text)
"""