import pyautogui as pa
import time

# time.sleep(5)
# print(pa.position())

pa. PAUSE = 1
pa.press('win')
pa.write("brave")
pa.press("ENTER")
pa.write("youtube.com")
pa.press('ENTER')
time.sleep(3)
pa.hotkey('winlleft','up')
pa.click(x=1700, y=210)
pa.write("duran duran ordinary world")
pa.press('ENTER')