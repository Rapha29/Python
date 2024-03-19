class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

carro_01 = Carro("Ferrari", "F40")
print("\n".join(f"{chave.capitalize()}: {valor}" for chave, valor in vars(carro_01).items()),"\n")

carro_02 = Carro("Fiat", "Uno")
print("\n".join(f"{chave.capitalize()}: {valor}" for chave, valor in vars(carro_02).items()))