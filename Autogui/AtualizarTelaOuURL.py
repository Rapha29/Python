import pyautogui
import time

while True:
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(60)

##// ------------------------------------------

import pyautogui
import time

# Lista de URLs
urls = ["http://www1.com", "http://www2.com", "http://www3.com"]
current_url_index = 0

while True:
    current_url = urls[current_url_index]
    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite(current_url)
    pyautogui.press('enter')
    time.sleep(5)
    current_url_index = (current_url_index + 1) % len(urls)
    time.sleep(60)