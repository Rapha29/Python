from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicialize o navegador
browser = webdriver.Chrome()
browser.get("https://web.whatsapp.com/")
input("Escaneie o código QR e pressione Enter para continuar...")

# Função para verificar e responder a novas mensagens
def check_and_respond():
    while True:
        # Espere até que a lista de conversas seja carregada
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="_1hI5g"]')))
        
        # Localize todas as conversas na lista
        conversations = browser.find_elements(By.XPATH, '//div[@class="_1hI5g"]')

        for conversation in conversations:
            # Clique na conversa para abri-la
            conversation.click()
            time.sleep(2)

            # Verifique se há novas mensagens não lidas na conversa
            unread_messages = browser.find_elements(By.XPATH, '//div[@class="_1VzZY"]/span[@data-icon="message-unread"]')

            if unread_messages:
                # Clique no ícone de mensagens não lidas para abrir as novas mensagens
                unread_messages[0].click()
                time.sleep(2)

                # Localize as mensagens não lidas
                new_messages = browser.find_elements(By.XPATH, '//div[contains(@class, "_3_7SH _3DFk6")]/div[contains(@class, "_3zb-j RwN9y")]')

                for message in new_messages:
                    # Clique na mensagem para abri-la
                    message.click()
                    time.sleep(2)

                    # Ler o conteúdo da mensagem e converter para minúsculas
                    message_content = message.text.lower()

                    # Verifique as condições e responda de acordo
                    response = ""
                    if "bom dia" in message_content:
                        response = "Bommm diaaaaaa!"
                    elif "oi" in message_content:
                        response = "Oie"
                    elif "aleluia" in message_content:
                        response = "Gloria a Deus!"

                    if response:
                        # Encontre o campo de entrada de texto
                        input_box = browser.find_element(By.XPATH, '//div[@class="_3u328 copyable-text selectable-text"]')
                        input_box.send_keys(response)
                        input_box.send_keys(Keys.ENTER)

                    # Volte para a lista de mensagens na conversa
                    browser.find_element(By.XPATH, '//button[@class="_3bF9q"]').click()
                    time.sleep(2)

                # Volte para a lista de conversas
                browser.find_element(By.XPATH, '//button[@class="_1qSbL _3ncH0 _1zIir"]').click()
                time.sleep(2)

        # Aguarde um tempo antes de verificar novamente (por exemplo, a cada 5 segundos)
        time.sleep(5)

# Exemplo de uso
check_and_respond()
