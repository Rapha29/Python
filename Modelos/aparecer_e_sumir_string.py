import random
import time
import pyautogui as pg

time.sleep(3)

frase = 'Raphael'
r = 0

pg.press('winleft')
time.sleep(1)
pg.write('notepad')
time.sleep(1)
pg.press('enter')
time.sleep(1)

for i in frase:
    r = r + 1
    pg.write(frase[0:r])
    pg.press('Enter')

for i in frase:
    r = r - 1
    pg.write(frase[0:r])
    pg.press('Enter')
    
''' 
# PARA FECHAR
time.sleep(3)
pg.hotkey('alt','f4')
pg.press('tab')
pg.press('enter')
time.sleep(1)
'''