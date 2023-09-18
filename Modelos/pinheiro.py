linhas = int(input('Digite a quantidade de linhas: '))
for i in range(1, linhas + 1):
    for espace in range(linhas, i, -1):
        print(' ', end='')
    for j in range(1, 2*i):
        print('♥', end='')
    print()