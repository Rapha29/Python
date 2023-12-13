from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

while True:
    # Abrir o WhatsApp Web
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    time.sleep(60)  # Aguarda o usuário fazer o scan do QR code

    # Verificar se há mensagens com a frase "pix ajuda ai"
    search_box = driver.find_element('xpath','//*[@id="side"]/div[1]/div/div[2]').click
    search_box.send_keys("pix ajuda ai" + Keys.RETURN)
    time.sleep(5)  # Aguarda os resultados da busca

    # Identificar a mensagem e abrir
    message = driver.find_element('xpath','//*[@id="pane-side"]/div[1]/div/div/div[2]')
    message.click()
    time.sleep(2)  # Aguarda a abertura da mensagem

    # Copiar nome e número da pessoa
    contact_info = driver.find_element('xpath','//span[@title]')
    contact_name = contact_info.get_attribute("title")
    contact_number = contact_info.get_attribute("data-pre-plain-text")

    # Salvar em um arquivo Excel
    data = {'Nome': [contact_name], 'Número': [contact_number]}
    df = pd.DataFrame(data)
    df.to_excel('contatos_whatsapp.xlsx', index=False)

