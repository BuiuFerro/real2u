from PIL import Image, ImageFilter

import matplotlib.pyplot as plt

import requests
from io import BytesIO

def criar_filtro(url):
    
    # Recebendo a imagem de uma URL
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    # Salvando a imagem com filtro
    img_filter = img.filter(ImageFilter.CONTOUR)
    img_filter.save('img.png')

    # Mostrando a imagem com filtro
    img_filter.show()

    # Mostrando a imagem original
# img.show()