import random
import time
import pyautogui as pg

time.sleep(5)

animais = ('Cachorro', 'Gato', 'Porco', 'Girafa', 'Cavalo', 'Elefante', 'Tigre', 'Uso')

pg.press('winleft')
time.sleep(1)
pg.write('notepad')
time.sleep(1)
pg.press('enter')
time.sleep(1)

for i in range(100):
    a = random.choice(animais)
    pg.write('No Zoológico eu vi: ' + a)
    pg.press('Enter')
    
pg.hotkey('alt','f4')
pg.press('tab')
pg.press('enter')
time.sleep(1)