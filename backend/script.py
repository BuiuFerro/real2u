from PIL import Image, ImageFilter

import requests
from io import BytesIO

import os

def gerar_img(url):
    # Recebendo a imagem de uma URL
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    # Salvando a imagem com filtro
    img_filter = img.filter(ImageFilter.CONTOUR)
    img_filter.save('img.png')
    
    # Mostrando a imagem com filtro
    img_filter.show()
    print("-----------------X--------------------")
    print("Imagem salva em: ", os.getcwd())
    print("-----------------X--------------------")