print("="*35)
print("          Descontos Starke         ")
print("="*35)
preco = float(input("Digite o preço do produto: R$ "))

print("[1] para 5% off")
print("[2] para 10% off")
print("[3] para 20% off")
d = int(input())

if d == 1:
    novopreco = preco - preco * (5/100)
    print("O preço desse produto com 5% de desconto é R$", format(novopreco, '.2f'))
elif d == 2:
    novopreco = preco - preco * (10/100)
    print("O preço desse produto com 10% de desconto é R$", format(novopreco, '.2f'))
elif d == 3:
    novopreco = preco - preco * (20/100)
    print("O preço desse produto com 20% de desconto é R$", format(novopreco, '.2f'))
else:
    print("Opção inválida!")
