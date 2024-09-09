#1 instalar Pillow con pip install pillow
#2 instalar google-generativeai con pip install google-generativeai
import google.generativeai as gai
from PIL import Image
import key

def ask(consulta, imagen):
    gai.configure(api_key=key.clave)
    model=gai.GenerativeModel(model_name="gemini-1.5-flash")
    response=model.generate_content([consulta, imagen])
    return response.text
