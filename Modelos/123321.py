while True:
    num = int(input('Digite um número de 0 a 10: '))
    
    menos_gosto = [
    'calor.',
    'fazer comida',
    'multidão',
    'muito barulho',
    'ambiente desorganizado',
    ] 
    mais_gosto = [
        'friozin',
        'comer comidinhas gostosas',
        'assistir filmes e series',
        'meu gatinho',
        'dormir',
        'conversar com o rapha :D',
    ]

    if 0 <= num <= 4:
        print(menos_gosto[num])
    elif 5 <= num <= 10:
        print(mais_gosto[num - 5])
    else:
        print("Por favor, escolha um número entre 0 e 10.")
        
    resposta = input('Deseja verificar outro número (S/N)? ').lower()
    if resposta != 's':
        print('Encerrando.')
        break