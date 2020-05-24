from PIL import Image, ImageFilter

import matplotlib.pyplot as plt

import requests
from io import BytesIO

# Insira a URL da imagem desejada
url = 'https://i.pinimg.com/564x/dd/6c/cf/dd6ccf8f48adf1fcc7eab0b2a5495661.jpg'

# Recebendo a imagem de uma URL
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Salvando a imagem com filtro
img_filter = img.filter(ImageFilter.CONTOUR)
img_filter.save('img.png')

# Mostrando a imagem com filtro
img_filter.show()

# Mostrando a imagem original
img.show()