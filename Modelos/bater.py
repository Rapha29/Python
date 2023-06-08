import random

# Lista de palavras para o jogo
palavras = ['python', 'programacao', 'jogo']

# Seleciona uma palavra aleatoriamente da lista
palavra = random.choice(palavras)

# Converte a palavra em uma lista de letras
letras = list(palavra)

# Lista para acompanhar as letras já tentadas pelo jogador
letras_tentadas = []

# Número máximo de tentativas permitidas
tentativas_maximas = 6

# Número de tentativas já feitas
tentativas = 0

# Função para imprimir a forca e as letras já tentadas
def imprimir_forca():
    print("Palavra: ", end="")
    for letra in letras:
        if letra in letras_tentadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("\nLetras tentadas: ", letras_tentadas)

# Loop principal do jogo
while True:
    imprimir_forca()
    letra = input("Digite uma letra: ")
    if letra in letras_tentadas:
        print("Você já tentou essa letra antes.")
    else:
        letras_tentadas.append(letra)
        if letra in letras:
            print("Você acertou!")
            if set(letras_tentadas) == set(letras):
                print("Parabéns, você acertou a palavra!")
                break
        else:
            print("Você errou!")
            tentativas += 1
    if tentativas == tentativas_maximas:
        print("Você perdeu! A palavra era", palavra)
        break