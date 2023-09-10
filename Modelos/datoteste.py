class concessionaria(object):
    carro1 = 'Bmw'  #estancia , atributos da classe 
    carro2 = 'brasilia'
    carro3 = 'fusca'
#-------------------------------------------------------
    def trocarcarro1(self, carro1):
        self.carro1 = carro1

    def trocarcarro2(self, carro2):
        self.carro2 = carro2

    def trocarcarro3(self, carro3):
        self.carro3 = carro3

    def quaiscarrostem(self):
        print(f"Tenho {self.carro1}, Tenho {self.carro2} Tenho {self.carro3}")
#-----------------------------------------------------------


print("ViniGostoso")