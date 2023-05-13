import os
import pyttsx3
from pdfminer.high_level import extract_text

def ler_pdf_reproduzir_audio():
    # Obter o diretório atual
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    # Percorrer os arquivos do diretório atual
    for nome_arquivo in os.listdir(diretorio_atual):
        if nome_arquivo.lower().endswith('.pdf'):
            # Construir o caminho completo para o arquivo PDF
            caminho_pdf = os.path.join(diretorio_atual, nome_arquivo)

            # Extrair o texto do PDF
            texto = extract_text(caminho_pdf)

            # Imprimir o texto no terminal
            print(texto)

            # Reproduzir o texto em áudio
            reproduzir_audio(texto)

def reproduzir_audio(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Ajuste a velocidade de reprodução conforme necessário
    engine.say(texto)
    engine.runAndWait()

ler_pdf_reproduzir_audio()
