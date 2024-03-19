import os
import time
import openpyxl
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

caminho_arquivo_excel = os.path.join(os.path.dirname(__file__), 'dados.xlsx')
wb = openpyxl.load_workbook(caminho_arquivo_excel)
planilha = wb.active
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
time.sleep(120)  # Aguarda o usuário fazer o scan do QR code

for row in planilha.iter_rows(min_row=2, values_only=True):
    nome = row[0]
    numero = "+55" + row[1]   
    url = f"https://wa.me/{numero}"
    driver.get(url)
    pyautogui.hotkey("shift","tab")
    pyautogui.press("space")
    time.sleep(1)
    driver.find_element('xpath','//*[@id="action-button"]/span').click
    time.sleep(5)
    driver.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').click
    pyautogui.click()
    time.sleep(1)
    mensagem_personalizada = (f"Olá {nome}, por gentileza, entre no nosso grupo do projeto AjudaAi"
                                f"Link https://chat.whatsapp.com/COqN2BMk10qHhDj3XgQVQz, "
                                f"atenciosamente Rapha®")
    pyautogui.write(mensagem_personalizada)
    time.sleep(20)            
    pyautogui.press("Enter")
    time.sleep(2)
    print(f"Mensagem Enviada com sucesso para: {nome}")