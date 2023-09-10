class ConstruirCasa(object):
    cor = ''
    altura = 0
    quartos = 0

    def __init__(self, cor, altura, quartos):
        self.cor = cor
        self.altura = altura
        self.quartos = quartos

    def pintar(self, cor):
        self.cor = cor

    def aumenta_quartos(self, quartos):
        self.quartos = quartos

    def imprime_casa(self):
        print(f"Sua casa é: {self.cor}, Com {self.altura}m de altura, e com {self.quartos} quartos.")

pedreiro = ConstruirCasa('branca', 1, 2)
pedreiro.imprime_casa()

