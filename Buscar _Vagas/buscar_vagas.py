import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import json

class VagasApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Vagas de Emprego")

        # Widgets para exibir as vagas de emprego
        self.vagas = tk.Listbox(self.root)
        self.vagas.pack()

        # Botões para navegar entre as vagas
        self.botao_anterior = tk.Button(self.root, text="Vaga Anterior", command=self.mostrar_vaga_anterior)
        self.botao_anterior.pack()

        self.botao_proximo = tk.Button(self.root, text="Vaga Proxima", command=self.mostrar_vaga_proxima)
        self.botao_proximo.pack()

        # Buscar vagas de emprego e atualizar o widget de vagas disponíveis
        self.buscar_vagas()

        # Índice da vaga atual
        self.indice_vaga_atual = 0

    def buscar_vagas(self):
        url = 'https://www.linkedin.com/jobs/search?currentJobId=3769280068&geoId=106057199&keywords=TI&location=Brasil&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        vagas = soup.find_all('li', class_='result-card')

        vagas_json = []
        for vaga in vagas:
            # Extrair informações das vagas de emprego
            titulo = vaga.find('h3', class_='result-card__title job-result-card__title').text.strip()
            empresa = vaga.find('a', class_='result-card__subtitle-link job-result-card__subtitle-link').text.strip()
            localizacao = vaga.find('span', class_='job-result-card__location').text.strip()
            
            # Criar um dicionário com as informações da vaga
            vaga_dict = {
                'titulo': titulo,
                'empresa': empresa,
                'localizacao': localizacao
            }
            vagas_json.append(vaga_dict)

        # Atualizar o widget de vagas disponíveis
        for vaga in vagas_json:
            self.vagas.insert(tk.END, f"{vaga['titulo']} - {vaga['empresa']} ({vaga['localizacao']})")
            print(vaga)

    def mostrar_vaga_anterior(self):
        if self.indice_vaga_atual > 0:
            self.indice_vaga_atual -= 1
            self.vagas.select_clear(0, tk.END)
            self.vagas.select_set(self.indice_vaga_atual)
            self.vagas.activate(self.indice_vaga_atual)
            self.vagas.see(self.indice_vaga_atual)

    def mostrar_vaga_proxima(self):
        if self.indice_vaga_atual < self.vagas.size() - 1:
            self.indice_vaga_atual += 1
            self.vagas.select_clear(0, tk.END)
            self.vagas.select_set(self.indice_vaga_atual)
            self.vagas.activate(self.indice_vaga_atual)
            self.vagas.see(self.indice_vaga_atual)

# Criar instância da classe VagasApp e iniciar o loop do evento
app = VagasApp()
app.root.mainloop()