#1 instalar Pillow con pip install pillow
#2 instalar google-generativeai con pip install google-generativeai
import google.generativeai as gai
from PIL import Image
import key


gai.configure(api_key=key.clave)
model=gai.GenerativeModel(model_name="gemini-1.5-flash")

imagen=Image.open("images/planta2.jpg")
imagen.show()

#response=model.generate_content("¿Cuantas personas hay en la imagen?", imagen)
consulta="¿De que tipo es la planta de la imágen?"
response=model.generate_content([consulta, imagen])
print(response.text)

