import pyautogui
import time
import random

time.sleep(8)

animal=('topa','gadhe','gandu','lodu','chutiya','bsdk')

for i in range (20):
    msg=random.choice(animal)
    pyautogui.write("Kya be "+msg)
    pyautogui.press('enter')
