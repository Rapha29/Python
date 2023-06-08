from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o navegador (certifique-se de ter o driver correto instalado: Chrome, Firefox, etc.)
driver = webdriver.Chrome()

# Abre o WhatsApp Web
driver.get('https://web.whatsapp.com')

# Aguarda o usuário fazer login manualmente no WhatsApp Web
input("Pressione Enter após fazer login no WhatsApp Web...")

# Localiza o campo de pesquisa e digita o nome do contato ou grupo
search_box = driver.find_element_by_xpath('//input[@title="Pesquisar ou começar uma nova conversa"]')
search_box.send_keys('Nome do Contato ou Grupo')

# Aguarda um tempo para que a lista de resultados seja atualizada
time.sleep(2)

# Seleciona o contato/grupo correto (geralmente o primeiro da lista)
contact = driver.find_element_by_xpath('//span[@title="Nome do Contato ou Grupo"]')
contact.click()

# Localiza o campo de digitação de mensagem
message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')

# Digita a mensagem
message_box.send_keys('Olá!')

# Envia a mensagem
message_box.send_keys(Keys.ENTER)

# Espera alguns segundos antes de fechar o navegador
time.sleep(3)

# Fecha o navegador
driver.quit()
