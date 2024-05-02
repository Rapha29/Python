import random
import msvcrt

frutas = ["Apple", "Watermelon", "Orange", "Strawberry", "Grape"]
traducao = ["maçã", "melancia", "laranja", "morango", "uva"]

def jogar_jogo():
    fruta = random.choice(frutas)
    traducao_correta = traducao[frutas.index(fruta)]
    
    opcoes = [traducao_correta]
    while len(opcoes) < 4:
        traducao_aleatoria = random.choice(traducao)
        if traducao_aleatoria not in opcoes:
            opcoes.append(traducao_aleatoria)
    
    random.shuffle(opcoes)
    
    print(f"Qual é a tradução da fruta '{fruta}'?")
    print("Opções:")
    for i, opcao in enumerate(opcoes):
        print(f"{i+1}. {opcao}")
    
    resposta = opcoes.index(traducao_correta) + 1
    palpite = int(input("Sua resposta (digite o número da opção): "))1
    
    if palpite == resposta:
        print("Parabéns! Você acertou, a Tradução de '{fruta}' é '{traducao_correta}'.")
    else:
        print("Oops! Você errou.")
        print(f"A resposta correta era o número {resposta}. a Tradução de '{fruta}' é '{traducao_correta}'.")
    
    print()
    print("Pressione qualquer tecla para continuar ou 'esc' para sair.")
    key = msvcrt.getch()
    if key != b'\x1b':  # Verifica se a tecla pressionada não é o 'esc'
        print()
        jogar_jogo()
    else:
        print("Obrigado por jogar!")

jogar_jogo()