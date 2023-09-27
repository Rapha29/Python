import time
import pyautogui as pag
import keyboard
import time


time.sleep(5)

while True:
    pag.press('F5')
    time.sleep(0.2)
    
    if keyboard.is_pressed('esc'):
        break
