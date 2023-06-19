import requests
from kivy.app import App
from kivy.lang import Builder


GUI = Builder.load_file("tela.kv")


class cotacao(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.ids["txt1"].text = f"1,00 = USD Dólar = R$ {self.pegar_cotacao('USD')}"
        self.root.ids["txt2"].text = f"1,00 = EUR Euro R$ {self.pegar_cotacao('EUR')}"
        self.root.ids["txt3"].text = f"1,00 = BTC Bitcoin R$ {self.pegar_cotacao('BTC')}"
        self.root.ids["txt4"].text = f"1,00 = GBP Libra Esterlina R$ {self.pegar_cotacao('GBP')}"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


cotacao().run()
