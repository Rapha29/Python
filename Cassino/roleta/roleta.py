import pyautogui
import cv2
import numpy as np
import telegram
import pandas as pd
from sklearn.linear_model import LinearRegression

# Chave do Token do Bot do Telegram
TOKEN = 'token+app+tlegram'

# ID do chat do grupo no Telegram
GROUP_CHAT_ID = 'id+grupo+telegram'

# Cria uma instância do bot do Telegram
bot = telegram.Bot(token=TOKEN)

# Lista de caminhos para as imagens dos números
caminhos_imagens = [
    "0.png", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png",
    "8.png", "9.png", "10.png", "11.png", "12.png", "13.png", "14.png", "15.png",
    "16.png", "17.png", "18.png", "19.png", "20.png", "21.png", "22.png", "23.png",
    "24.png", "25.png", "26.png", "27.png", "28.png", "29.png", "30.png", "31.png",
    "32.png", "33.png", "34.png", "35.png", "36.png"
]

# Dicionário para mapear os números às suas respectivas imagens
numeros_imagens = {
    str(i): cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
    for i, caminho in enumerate(caminhos_imagens)
}

# Lista para armazenar os números encontrados
numeros_encontrados = []

# Carrega a planilha de resultados
resultados = pd.read_csv('resultados.csv')

# Obtém os números na ordem em que caíram
numeros_caidos = resultados['Numero'].tolist()

# Cria um modelo de regressão linear
regressor = LinearRegression()

# Treina o modelo usando os números caídos como entrada e o próximo número como saída
X = np.array(numeros_caidos[:-1]).reshape(-1, 1)
y = np.array(numeros_caidos[1:])
regressor.fit(X, y)

# Loop contínuo para capturar a tela e procurar os números
while True:
    # Captura a tela
    imagem_tela = pyautogui.screenshot()

    # Converte a imagem capturada para o formato do OpenCV
    imagem_opencv = cv2.cvtColor(
        np.array(imagem_tela),
        cv2.COLOR_RGB2BGR
    )

    # Loop pelos números e procura cada um na tela
    for numero, imagem_numero in numeros_imagens.items():
        resultado = cv2.matchTemplate(imagem_opencv, imagem_numero, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

        # Verifica se o número foi encontrado
        if max_val >= 0.9 and numero not in numeros_encontrados:
            numeros_encontrados.append(numero)
            mensagem = f"Número {numero} encontrado!"
            bot.send_message(chat_id=GROUP_CHAT_ID, text=mensagem)

            # Adiciona o número encontrado à lista de números caídos
            numeros_caidos.append(int(numero))

            # Treina o modelo com os novos dados
            X = np.array(numeros_caidos[:-1]).reshape(-1, 1)
            y = np.array(numeros_caidos[1:])
            regressor.fit(X, y)

            # Prevê o próximo número
            proximo_numero = regressor.predict([[int(numero)]])

            mensagem_proximo = f"Próximo número: {int(proximo_numero[0])}"
            bot.send_message(chat_id=GROUP_CHAT_ID, text=mensagem_proximo)

            # Adiciona o número encontrado à planilha de resultados
            novo_registro = pd.DataFrame({'Numero': [int(numero)]})
            resultados = resultados.append(novo_registro, ignore_index=True)
            resultados.to_csv('resultados.csv', index=False)

    # Exibe a tela capturada em uma janela
    cv2.imshow('Captura de Tela', imagem_opencv)
    if cv2.waitKey(1) == ord('q'):
        break

# Fecha as janelas
cv2.destroyAllWindows()