import tkinter as tk
import random

# Lista de frases
frases = [
    "A persistência é o caminho do êxito.",
    "Só se pode alcançar um grande êxito quando nos mantemos fiéis a nós mesmos.",
    "Acredite em si próprio e chegará um dia em que os outros não terão outra escolha senão acreditar com você.",
    "Nada acontece a menos que sonhemos antes.",
    "O sucesso é a soma de pequenos esforços repetidos dia após dia.",
    "A persistência realiza o impossível.",
    "O otimismo é a fé em ação.",
    "O que não provoca minha morte faz com que eu fique mais forte.",
    "Quanto maior a dificuldade, maior é a glória."
]

# Função para gerar uma frase aleatória
def gerar_frase():
    frase = random.choice(frases)
    label_frase['text'] = frase

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerador de Frases")

# Criando e configurando widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_titulo = tk.Label(frame, text="Clique no botão para gerar uma frase:", font=("Arial", 12))
label_titulo.pack(padx=10, pady=10)

label_frase = tk.Label(frame, text="", font=("Arial", 10), wraplength=300)
label_frase.pack(padx=10, pady=10)

botao_gerar = tk.Button(frame, text="Gerar Frase", command=gerar_frase)
botao_gerar.pack(padx=10, pady=10)

# Iniciar o loop principal
root.mainloop()
