import random
import tkinter as tk
from PIL import Image, ImageTk # pip install pillow
import os


frutas = ["maçã", "melancia", "laranja", "morango", "uva"]
traducao = ["Apple", "Watermelon", "Orange", "Strawberry", "Grape"]

def jogar_jogo():
    fruta = random.choice(frutas)
    traducao_correta = traducao[frutas.index(fruta)]
    opcoes = [traducao_correta]
    while len(opcoes) < 4:
        traducao_aleatoria = random.choice(traducao)
        if traducao_aleatoria not in opcoes:
            opcoes.append(traducao_aleatoria)
    random.shuffle(opcoes)
    janela = tk.Tk()
    janela.title("Jogo de Tradução de Frutas")
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    imagem_fruta = Image.open(os.path.join(diretorio_atual, f"{fruta.lower()}.png"))
    imagem_fruta = imagem_fruta.resize((200, 200))
    imagem_fruta = ImageTk.PhotoImage(imagem_fruta)
    label_fruta = tk.Label(janela, image=imagem_fruta)
    label_fruta.pack()

    for i, opcao in enumerate(opcoes):
        botao_opcao = tk.Button(janela, text=opcao, font=("Arial", 16), width=15, height=2, command=lambda x=i+1: verificar_resposta(x, traducao_correta, fruta, opcoes, janela))
        botao_opcao.pack()
    def fechar_janela():
        janela.destroy()
    janela.protocol("WM_DELETE_WINDOW", fechar_janela)
    janela.mainloop()

def verificar_resposta(palpite, traducao_correta, fruta, opcoes, janela):
    janela.destroy()  
    if palpite == opcoes.index(traducao_correta) + 1:
        mensagem = f"Parabéns! Você acertou, a tradução de '{fruta}' é '{traducao_correta}'."
        titulo = "Acertou!"
    else:
        mensagem = f"Oops! Você errou.\nA resposta correta era o número {opcoes.index(traducao_correta) + 1}. A tradução de '{fruta}' é '{traducao_correta}'."
        titulo = "Errou!"
    janela_resultado = tk.Tk()
    janela_resultado.title(titulo)
    label_resultado = tk.Label(janela_resultado, text=mensagem, font=("Arial", 14), padx=20, pady=20)
    label_resultado.pack()

    def jogar_novamente():
        janela_resultado.destroy()
        jogar_jogo()

    def fechar_jogo():
        janela_resultado.destroy()
    botao_jogar_novamente = tk.Button(janela_resultado, text="Jogar Novamente", font=("Arial", 12), width=15, command=jogar_novamente)
    botao_jogar_novamente.pack(pady=10)
    botao_fechar = tk.Button(janela_resultado, text="Fechar", font=("Arial", 12), width=10, command=fechar_jogo)
    botao_fechar.pack(pady=10)
    janela_resultado.mainloop()

jogar_jogo()