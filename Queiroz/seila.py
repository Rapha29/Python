import os
import re
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time as tm
import pyautogui as pg
import xlrd
import xlwt
import pywhatkit as kit

pg.PAUSE = 1

file_path = r'C:\Users\Downloads\relatorio_roteiro.xls'

data_inicio = '01/11/2023'
data_final = '15/11/2023'

promotores = ['Aira Manuele', 
              'Allisson', 
              'Daniel Silva', 
              'Jocirley Paulo']

numero_whatsapp = "+55"

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://fhdistribuidora.tradepro.com.br/fhdistribuidora/login.jsf;jsessionid=8a607e2c07ea6d33f242c5bd7bce')
pg.hotkey('winleft', 'up')
tm.sleep(2)
navegador.find_element('xpath', '//*[@id="j_username"]').send_keys('') 
navegador.find_element('xpath', '//*[@id="j_password"]').send_keys('')
navegador.find_element('xpath', '//*[@id="botaoAcaoBancoEntrar"]/span[2]').click()
navegador.find_element('xpath', '//*[@id="consulta"]/a').click()
pg.moveTo(487, 534, 0.5)
pg.scroll(-100)
navegador.find_element('xpath', '//*[@id="roteiros"]/a').click()
tm.sleep(1)
pg.scroll(-200)
navegador.find_element('xpath', '//*[@id="j_idt241"]/a').click()
navegador.find_element('xpath', '//*[@id="dataInicial_input"]').click()
pg.press('backspace', presses=10)
# Data inicial 
navegador.find_element('xpath', '//*[@id="dataInicial_input"]').send_keys(data_inicio) 
tm.sleep(1)
pg.press('tab')
pg.press('backspace', presses=10)
# Data final
navegador.find_element('xpath', '//*[@id="dataFinal_input"]').send_keys(data_final)
pg.click(x=975, y=585)
tm.sleep(1)

# Baixa o arquivo excel
navegador.find_element('xpath', '//*[@id="botaoAcaoBancoExcel_button"]').click()
tm.sleep(2)

#Tratando Planilha por nomes 
book = xlrd.open_workbook(file_path)
sheet = book.sheet_by_index(0)  # Assume que os dados estão na primeira planilha

# Lendo o arquivo .xls e filtrando os dados para cada promotor
dados_promotores = {promotor: [] for promotor in promotores}

for rowx in range(1, sheet.nrows):  # Ignorando o cabeçalho, começando da segunda linha
    nome_na_coluna_b = sheet.cell_value(rowx, 1)  # Lendo a coluna 'B'
    for promotor in promotores:
        if nome_na_coluna_b == promotor:
            row_values = [sheet.cell_value(rowx, colx) for colx in range(sheet.ncols)]
            dados_promotores[promotor].append(row_values)

# Salvando os dados em arquivos .xls separados com o nome do promotor, data inicial e data final
diretorio_origem = os.path.dirname(file_path)
caminhos_arquivos = []

for promotor, dados in dados_promotores.items():
    if dados:
        novo_arquivo = xlwt.Workbook()
        planilha = novo_arquivo.add_sheet('Sheet1')

        for row_index, row in enumerate(dados):
            for col_index, value in enumerate(row):
                planilha.write(row_index, col_index, value)

        # Criando o nome do arquivo evitando caracteres inválidos
        nome_arquivo = f'{promotor}.xls'
        nome_arquivo = re.sub(r'[^\w_.-]', '', nome_arquivo)

        # Cria o caminho completo para salvar na mesma pasta do arquivo original com a extensão .xls
        caminho_arquivo = os.path.join(diretorio_origem, nome_arquivo)
        novo_arquivo.save(caminho_arquivo)
        caminhos_arquivos.append(caminho_arquivo)
        print(caminhos_arquivos)

# Envia cada arquivo para o número de WhatsApp especificado
for promotor, caminho_arquivo in zip(promotores, caminhos_arquivos):
    def enviar_arquivos_whatsapp(numero, caminhos_arquivos):
        kit.sendwhatmsg_instantly(numero, f"Enviando planilha do intervalo de datas {data_inicio} até {data_final}...")
        pg.press('enter')
        tm.sleep(2)
        pg.hotkey('shift', 'tab')
        tm.sleep(1)
        pg.press('space')
        tm.sleep(1)
        pg.press('down')
        tm.sleep(1)
        pg.press('space')
        tm.sleep(1)
        pg.write(caminho_arquivo)
        tm.sleep(1)
        pg.press('enter') 
        tm.sleep(1)
        pg.press('enter') 
        tm.sleep(2)

    # Envio dos arquivos
    enviar_arquivos_whatsapp(numero_whatsapp, caminhos_arquivos)
