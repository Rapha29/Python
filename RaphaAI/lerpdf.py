import os
import pyttsx3
from pdfminer.high_level import extract_text

def ler_pdf_reproduzir_audio():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    for nome_arquivo in os.listdir(diretorio_atual):
        if nome_arquivo.lower().endswith('.pdf'):
            caminho_pdf = os.path.join(diretorio_atual, nome_arquivo)
            texto = extract_text(caminho_pdf)
            print(texto)
            reproduzir_audio(texto)

def reproduzir_audio(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)  # velocidade de reprodução
    engine.say(texto)
    engine.runAndWait()

ler_pdf_reproduzir_audio()
