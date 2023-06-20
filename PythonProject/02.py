# solicita ao usuário o número máximo da sequência de Fibonacci
maximo = int(input("Digite o número máximo da sequência de Fibonacci: "))

# inicializa os dois primeiros valores da sequência
fibonacci = [0, 1]

# calcula os valores da sequência até atingir o número máximo
while fibonacci[-1] < maximo:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# verifica se o número informado pertence à sequência
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
if numero in fibonacci:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
