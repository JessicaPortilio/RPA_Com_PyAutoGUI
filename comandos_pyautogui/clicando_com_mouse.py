import pyautogui
from time import sleep

# sleep(4)
# print(pyautogui.position())

pyautogui.moveTo(x=263, y=1047, duration=1)
pyautogui.click()

# Quiser que o click no mouse seja no botão direito -> button = 'right'

# Realizar um clique duplo no local atual do mouse
# pyautogui.doubleClick()