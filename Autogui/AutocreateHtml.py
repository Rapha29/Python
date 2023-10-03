import pyautogui
import time


pyautogui.press('winleft')
pyautogui.write('cmd')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('cd desktop')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('mkdir Teste')
pyautogui.press('enter')
