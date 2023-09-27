import random
import time
import pyautogui as pg

time.sleep(5)

animais = ('Velhho','Idoso','Velhinho','Ancião','De Idade')

pg.press('winleft')
time.sleep(1)
pg.write('notepad')
time.sleep(1)
pg.press('enter')
time.sleep(1)

for i in range(100):
    a = random.choice(animais)
    pg.write('O Vini é: ' + a)
    pg.press('Enter')
    
time.sleep(3)
pg.hotkey('alt','f4')
pg.press('tab')
pg.press('enter')