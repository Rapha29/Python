numeros = []

for i in range(5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)

print("Soma: ", soma)
print("Maior número: ", maior)
print("Menor número: ", menor)