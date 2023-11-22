# pip install opencv-python pyautogui

import cv2
import pyautogui
import os

# Lista de caminhos para os arquivos .png com os nomes das pessoas
caminhos_nomes = ['nome_pessoa1.png', 'nome_pessoa2.png', 'nome_pessoa3.png']

# Função para desenhar um retângulo com o nome da pessoa ou "Desconhecido"
def draw_rectangle_with_name(x, y, width, height, name):
    # Desenha um retângulo ao redor do rosto
    pyautogui.moveTo(x, y)
    pyautogui.dragTo(x + width, y + height, duration=0.25)

    # Define o texto a ser exibido abaixo do retângulo
    text = name if name else "Desconhecido"

    # Adiciona o texto com o nome da pessoa ou "Desconhecido"
    pyautogui.moveTo(x + (width // 2), y + height + 10)
    pyautogui.write(text, font=("Arial", 12), align='center')

# Inicializa a captura de vídeo da webcam
video_capture = cv2.VideoCapture(0)

# Carrega as imagens com os nomes das pessoas em uma lista
nomes_pessoas = [cv2.imread(nome_arquivo, cv2.IMREAD_UNCHANGED) for nome_arquivo in caminhos_nomes]

# Loop para procurar por rostos na webcam
while True:
    # Captura um frame da webcam
    ret, frame = video_capture.read()

    # Converte para escala de cinza para detecção de rosto
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Inicializa o classificador de detecção de rosto
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detecta rostos na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Se nenhum rosto for encontrado, exibe "Desconhecido"
    if len(faces) == 0:
        draw_rectangle_with_name(0, 0, 0, 0, None)
    else:
        # Itera sobre os rostos encontrados
        for (x, y, w, h), nome_pessoa in zip(faces, nomes_pessoas):
            draw_rectangle_with_name(x, y, w, h, "Pessoa")

            # Mostra o nome da pessoa acima do retângulo
            if nome_pessoa is not None:
                frame[y - nome_pessoa.shape[0]:y, x:x + nome_pessoa.shape[1]] = nome_pessoa

    # Mostra a imagem com os retângulos e nomes
    cv2.imshow('Detected Faces', frame)

    # Verifica se o usuário pressionou a tecla 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a captura de vídeo e fecha a janela ao finalizar
video_capture.release()