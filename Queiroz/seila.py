import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time as tm
import pyautogui as pg
import pywhatkit as kit
import subprocess as sp

# Caminho da pasta de downloads do navegador
file_path = r'C:\Users\rapha\Downloads'

# Definir endereço do site
url = 'https://fhdistribuidora.tradepro.com.br/fhdistribuidora/login.jsf;jsessionid=8a607e2c07ea6d33f242c5bd7bce'

# Definir intervalo de datas
data_inicio = '01/11/2023'
data_final = '15/11/2023'

# Definir nomes a serem encontrados na planilha
promotores = ['Allisson',       # //*[@id="multSelectPromotor:multiSelectPromotor_panel"]/div[2]/ul/li[4]/label[1]
              'Daniel Silva',   # //*[@id="multSelectPromotor:multiSelectPromotor_panel"]/div[2]/ul/li[6]/label[1]
              'Jocirley Paulo'] # //*[@id="multSelectPromotor:multiSelectPromotor_panel"]/div[2]/ul/li[7]/label[1]
 
# Definir numero do whatsapp para quem enviar cada relatório
numero_whatsapp = "+559281529451"

# servico = Service(ChromeDriverManager().install())
# navegador = webdriver.Chrome(service=servico)

# # Abre o navegador com o endereço selecionado
# navegador.get(url)
# pg.hotkey('winleft', 'up')
# tm.sleep(2)

# # Efetua o login no site
# navegador.find_element('xpath', '//*[@id="j_username"]').send_keys('Loraynne Sales') 
# navegador.find_element('xpath', '//*[@id="j_password"]').send_keys('01031704Fh')
# navegador.find_element('xpath', '//*[@id="botaoAcaoBancoEntrar"]/span[2]').click()
# navegador.find_element('xpath', '//*[@id="consulta"]/a').click()
# pg.scroll(-100)

# # Seleciona o link roteiros
# navegador.find_element('xpath', '//*[@id="roteiros"]/a').click()
# tm.sleep(1)
# pg.scroll(-200)

# # Clica e modifica o texttobox de pesquisa entre datas
# navegador.find_element('xpath', '//*[@id="j_idt241"]/a').click()
# navegador.find_element('xpath', '//*[@id="dataInicial_input"]').click()
# pg.press('backspace', presses=10)
# tm.sleep(1)

# def alterar_datas():
#     # Define a Data inicial 
#     elemento = navegador.find_element('xpath', '//*[@id="dataInicial_input"]')
#     elemento.clear()
#     elemento.send_keys(data_inicio)
#     tm.sleep(1)
#     pg.press('tab')
#     pg.press('backspace', presses=10)
#     # Define a Data final
#     tm.sleep(2)
#     elemento = navegador.find_element('xpath', '//*[@id="dataFinal_input"]')
#     elemento.clear()
#     elemento.send_keys(data_final)
#     tm.sleep(2)


# for promotor in promotores:
#     if promotor == "Allisson":
#         navegador.find_element('xpath', '//*[@id="multSelectPromotor:multiSelectPromotor"]/div[3]/span').click()
#         alterar_datas()
#         tm.sleep(2)
#         navegador.find_element('xpath', '//*[@id="multSelectPromotor:multiSelectPromotor_panel"]/div[2]/ul/li[4]/label[1]').click()
#         tm.sleep(2)
#         navegador.find_element('xpath', '//*[@id="botaoAcaoBancoPesquisar"]').click()
#         tm.sleep(2)
#         navegador.find_element('xpath', '//*[@id="botaoAcaoBancoExcel_button"]').click()
#         tm.sleep(2)  
#     elif promotor == "Daniel Silva":
#         navegador.refresh()
#         tm.sleep(2)     
#         navegador.find_element('xpath', '//*[@id="multSelectPromotor:multiSelectPromotor"]/div[3]/span').click()
#         alterar_datas()
#         tm.sleep(2)
#         navegador.find_element('xpath', '//*[@id="multSelectPromotor:multiSelectPromotor_panel"]/div[2]/ul/li[6]/label[1]').click()
#         tm.sleep(2)
#         navegador.find_element('xpath', '//*[@id="botaoAcaoBancoPesquisar"]').click()
#         tm.sleep(2)
#         navegador.find_element('xpath', '//*[@id="botaoAcaoBancoExcel_button"]').click()
#         tm.sleep(2)     
#     elif promotor == "Jocirley Paulo":
#         navegador.refresh()
#         tm.sleep(2)     
#         navegador.find_element('xpath', '//*[@id="multSelectPromotor:multiSelectPromotor_label"]').click()
#         alterar_datas()
#         navegador.find_element('xpath', '//*[@id="multSelectPromotor:multiSelectPromotor_panel"]/div[2]/ul/li[7]/label[1]').click()
#         tm.sleep(2)
#         navegador.find_element('xpath', '//*[@id="botaoAcaoBancoPesquisar"]').click()
#         tm.sleep(2)
#         navegador.find_element('xpath', '//*[@id="botaoAcaoBancoExcel_button"]').click()
#         tm.sleep(2)  
#     else:
#         break     

# Envia cada arquivo para o número de WhatsApp especificado
def enviar_arquivos_whatsapp(numero):
    kit.sendwhatmsg_instantly(numero, f"Enviando planilha do intervalo de datas {data_inicio} até {data_final}...")
    sp.run(["explorer", file_path])
    
    # Define as coordenadas iniciais e finais para o movimento
    x_inicial, y_inicial = 100, 100  # coordenadas iniciais
    x_final, y_final = 300, 300      # coordenadas finais

    # Move o cursor para a posição inicial
    pg.moveTo(x_inicial, y_inicial)

    # Clica e segura o botão do mouse
    pg.mouseDown()

    # Move o cursor para a posição final ao longo de alguns segundos
    pg.moveTo(x_final, y_final, duration=2)

    # Solta o botão do mouse
    pg.mouseUp()

# Envio dos arquivos
enviar_arquivos_whatsapp(numero_whatsapp)