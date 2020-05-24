from PIL import Image, ImageFilter

import matplotlib.pyplot as plt

import requests
from io import BytesIO

# Insira a URL da imagem desejada
url = 'https://i.pinimg.com/originals/2c/c8/d9/2cc8d9b4f4255e089ddf629bdadf18fc.jpg'

# Recebendo a imagem de uma URL
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Imagem com algum filtro
img.filter(ImageFilter.CONTOUR).show()

# Imagem original
img.show()