numeroDeSwitchs = input("Digite a quantidade de switchs: ")
n = int(numeroDeSwitchs)

print("O numero de links é:", ((n*(n-1))/2))
print("O numero de portas é:", ((n*(n-1))))
print("O numero de portas que cada switch usa é:", ((n*(n-1)))/n)
