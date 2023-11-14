import random

def exibir_palavra(palavra, letras_adivinhadas):
    return ' '.join([letra if letra.lower() in letras_adivinhadas else '_' for letra in palavra])

def desenhar_forca(tentativas_restantes):
    etapas = [
        '''
           -----
           |   |
               |
               |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        '''
    ]

    print(etapas[6 - tentativas_restantes])

def jogo_da_forca():
    palavras = ["Rapha","Isaias"]
    palavra = random.choice(palavras)
    letras_adivinhadas = []
    tentativas_restantes = 6

    print("Bem-vindo ao Jogo da Forca!")
    print(exibir_palavra(palavra, letras_adivinhadas))

    while True:
        palpite = input("Digite uma letra: ").lower()

        if palpite in letras_adivinhadas:
            print(f"Você já tentou a letra '{palpite}'. Tente outra.")
            continue

        if palpite.isalpha() and len(palpite) == 1:
            if palpite.lower() in palavra.lower():
                letras_adivinhadas.append(palpite.lower())
                print(f"Letra '{palpite}' encontrada!")
            else:
                tentativas_restantes -= 1
                desenhar_forca(tentativas_restantes)
                print(f"Letra '{palpite}' não está na palavra. Você tem {tentativas_restantes} tentativas restantes.")
                if tentativas_restantes == 0:
                    print("Você perdeu! A palavra era:", palavra)
                    break
        else:
            print("Por favor, digite uma letra válida.")

        exibicao_palavra = exibir_palavra(palavra, letras_adivinhadas)
        print(exibicao_palavra)

        if '_' not in exibicao_palavra:
            print("Parabéns! Você venceu!")
            break

jogo_da_forca()
