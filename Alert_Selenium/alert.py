from selenium import webdriver
from selenium.webdriver.common.alert import Alert

# Inicialize o driver do Chrome (ou outro navegador)
driver = webdriver.Chrome()  # ou webdriver.Firefox() para Firefox, etc.

# Abra uma página web
driver.get("https://github.com/Rapha29")

# Localize o elemento usando o XPath
elemento = driver.find_element('xpath', '//*[@id="user-profile-frame"]/div/div[1]/div/article/h1')

# Clique no elemento para acionar o alerta
# elemento.click()

# Lide com o alerta
alerta = Alert(driver)
texto_do_alerta = alerta.text
print("Texto do alerta:", texto_do_alerta)

# Aceite o alerta (clique em OK)
alerta.accept()

# A página permanece aberta após lidar com o alerta
