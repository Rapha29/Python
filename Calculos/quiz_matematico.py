def conferir(indice, *args):
    resposta = args
    valor_indice = int(eval(resposta[0])[indice]) - 1
    return valor_indice

def perguntar():
    for i in perguntas:
        pergunta = i['Pergunta']
        print(pergunta)
        opcao = i['Opções']
        resposta_correta = int(i['Resposta']) - 1 
        for indice, valor in enumerate(opcao):
            print(f'{indice+1}) {valor}')

        while True:
            try:
                resposta_usuario = int(input('Escolha uma opção: '))
                if 1 <= resposta_usuario <= 4:
                    break
                else:
                    print('Opção inválida. Escolha um número de 1 a 4.')
            except ValueError:
                print('Opção inválida. Digite um número inteiro de 1 a 4.')

        valor_indice = conferir(resposta_usuario - 1, str(opcao))

        if valor_indice == resposta_correta:
            print('Você Acertou!\n')
        else:
            print('Você Errou! A resposta correta era a opção\n', resposta_correta + 1)

perguntas = [{
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },{
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },{
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]

print(perguntar())
