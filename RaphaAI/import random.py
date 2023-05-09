import random

# lista de palavras
palavras = ['abacaxi', 'banana', 'laranja', 'morango', 'melancia']

# seleciona aleatoriamente uma palavra da lista
palavra = random.choice(palavras)

# define as variáveis iniciais
letras_certas = []
letras_erradas = []
tentativas = 6

# laço principal do jogo
while True:
    # mostra o estado atual da forca e das letras encontradas
    print('Forca:')
    print(' |-----|')
    print(' |     |')
    print(' |     {}'.format('O' if tentativas < 6 else ''))
    print(' |    {}{}'.format('/' if tentativas < 5 else '', '|' if tentativas < 4 else ''))
    print(' |    {} {}'.format('/' if tentativas < 3 else '', '\\' if tentativas < 2 else ''))
    print('_|_')
    print('')
    print('Palavra: ', end='')
    for letra in palavra:
        if letra in letras_certas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print('')
    print('Letras erradas: ', end='')
    for letra in letras_erradas:
        print(letra, end=' ')
    print('')
    print('Tentativas restantes: {}'.format(tentativas))
    print('')

    # verifica se o jogador acertou ou errou todas as letras
    if set(letras_certas) == set(palavra):
        print('Parabéns, você venceu!')
        break
    elif tentativas == 0:
        print('Game over! A palavra era "{}".'.format(palavra))
        break

    # solicita uma nova letra
    letra = input('Digite uma letra: ').lower()

    # verifica se a letra já foi tentada anteriormente
    if letra in letras_certas or letra in letras_erradas:
        print('Você já tentou essa letra. Tente outra.')
        continue

    # verifica se a letra está presente na palavra
    if letra in palavra:
        letras_certas.append(letra)
    else:
        letras_erradas.append(letra)
        tentativas -= 1