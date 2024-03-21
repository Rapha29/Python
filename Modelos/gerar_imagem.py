import openai
import requests
import os
from io import BytesIO
from PIL import Image

imagem = input("Digite a imagem que deseja gerar: ")

def gerar_imagem(prompt):
    openai.api_key = os.getenv("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")
    response = openai.Image.create(
        prompt = prompt,
        n=1,
        size = "1024x1024",
        response_format = "url"
    )
    image_url = response["data"][0]["url"]
    image_data = requests.get(image_url).content
    image = Image.open(BytesIO(image_data))
    image.show()
gerar_imagem(imagem)