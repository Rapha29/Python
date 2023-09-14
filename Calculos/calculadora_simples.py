def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Não é possível dividir por zero"
    return x / y

while True:
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == '5':
        print("Encerrando a calculadora.")
        break

    if escolha not in ('1', '2', '3', '4'):
        print("Opção inválida. Escolha uma operação válida (1/2/3/4).")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro de entrada. Certifique-se de inserir números válidos.")
        continue

    if escolha == '1':
        print("Resultado: ", adicao(num1, num2))
    elif escolha == '2':
        print("Resultado: ", subtracao(num1, num2))
    elif escolha == '3':
        print("Resultado: ", multiplicacao(num1, num2))
    elif escolha == '4':
        resultado = divisao(num1, num2)
        if isinstance(resultado, str):
            print(resultado)
        else:
            print("Resultado: ", resultado)
